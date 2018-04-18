from graph_function import *

startTime = time.time()

list_post = getListFromFile("../files/list_comment_category.txt")
post_comments = list_post["post"]
list_loc = getListFromFile("../files/list_location.txt")

#to connect mongoDB
db = connectDB()
posts = db.newPhotos

#-----------------------------------define directed graph--------------------
G = snap.TNEANet.New()

# define int, float and str attributes on nodes
G.AddStrAttrN('NLabel', '0')
G.AddStrAttrN('NName', '0')
G.AddStrAttrN('NImage', '0')
G.AddStrAttrN('NObjectId', '0')
G.AddStrAttrN('NText', '0')
G.AddStrAttrN('NCommentId', '0')
G.AddStrAttrN('NType', '0')
G.AddStrAttrN('NAuthor', '0')
G.AddStrAttrN('NCity', '0')
G.AddStrAttrN('NCountry', '0')

# define an int attribute on edges
G.AddStrAttrE('ELabel', '0')
G.AddStrAttrE('ETime', '0')

userList = {}
userList['user'] = []

challengeList = {}
challengeList['challenge'] = []

locationList = {}
locationList['location'] = []

hashtagList = {}
hashtagList['hashtag'] = []

#----------------------------------------------------DB Iteration------------
m = 0
i = 0
e = 0
commID = 0
cursor = posts.find(no_cursor_timeout=True)
for data in cursor:
	print '--------iteration:',m

	#----------add Node Photo-----------------------------------------------------------
	i = i + 1
	iPhoto = i
	username = data['username']
	image = data['imageURL']	
	
	caption = data['raw']['caption']
	if caption is not None:
		caption = data['raw']['caption']['text']
	
	objId = str(data['_id'])

	G.AddNode(iPhoto)
	G.AddStrAttrDatN(iPhoto, 'photo', 'NLabel')
	G.AddStrAttrDatN(iPhoto, username, 'NAuthor')
	G.AddStrAttrDatN(iPhoto, image, 'NImage')
	G.AddStrAttrDatN(iPhoto, caption, 'NText')
	G.AddStrAttrDatN(iPhoto, objId, 'NObjectId')
		
	creationTimePhoto = None
	if 'created_time' in data['raw']:
		creationTimePhoto = data['raw']['created_time']
	else:
		creationTimePhoto = data['raw']['createdtime']
	creationTimePhoto = str(creationTimePhoto)

	#----------add Node Photo Author-----------------------------------------------------
	unique = isUniqueUser(userList, username)
	if unique:
		i = i + 1
		iUser = i
		G.AddNode(iUser)

		fullName = None
		if 'full_name' in data['raw']['user']:
			fullName = data['raw']['user']['full_name']
		elif 'fullname' in data['raw']['user']:
			fullName = data['raw']['user']['fullname']

		profilePicture = None
		if 'profile_picture' in data['raw']['user']:
			profilePicture = data['raw']['user']['profile_picture']
		elif 'profilepicture' in data['raw']['user']:
			profilePicture = data['raw']['user']['profilepicture']

		userList = addUserList(userList, iUser, username, fullName, profilePicture)

		G.AddStrAttrDatN(iUser, 'user', 'NLabel')
		G.AddStrAttrDatN(iUser, username, 'NName')
		G.AddStrAttrDatN(iUser, profilePicture, 'NImage')

	else:
		iUser = getUserId(userList, username)

	#add edge User-Photo
	G.AddEdge(iUser, iPhoto)
	eid = G.GetEId(iUser,iPhoto)
	G.AddStrAttrDatE(eid, 'write', 'ELabel')
	G.AddStrAttrDatE(eid, creationTimePhoto, 'ETime')

	#----------add Node User likers------------------------------------------------------
	likers = data['likers']
	if len(likers)>0:
		for liker in data['likers'][-1]['list']:			
			unique = isUniqueUser(userList,liker)
			if unique:
				i = i + 1
				iLiker = i

				G.AddNode(iLiker)

				G.AddStrAttrDatN(iLiker, 'user', 'NLabel')
				G.AddStrAttrDatN(iLiker, liker, 'NName')
				G.AddStrAttrDatN(iLiker, '0', 'NImage')

				userList = addUserList(userList, iLiker, liker)

			else:
				iLiker = getUserId(userList, liker)
			
			#add edge UserLiker-Photo			
			G.AddEdge(iLiker, iPhoto)
			eid = G.GetEId(iLiker,iPhoto)			
			G.AddStrAttrDatE(eid, 'like', 'ELabel')
			G.AddStrAttrDatE(eid, '0', 'ETime')

	#----------add Node Challenge--------------------------------------------------------
	challengeName = data['tag']	
	unique = isUniqueChallenge(challengeList, challengeName)
	if unique:
		i = i + 1
		iChal = i

		G.AddNode(iChal)

		G.AddStrAttrDatN(iChal, 'challenge', 'NLabel')
		G.AddStrAttrDatN(iChal, challengeName, 'NName')
			
		challengeList = addChallengeList(challengeList, iChal, challengeName)	

	else:
		iChal = getChallengeId(challengeList, challengeName)
	
	#add edge Photo-Challenge	
	G.AddEdge(iPhoto, iChal)	
	eid = G.GetEId(iPhoto,iChal)
	G.AddStrAttrDatE(eid, 'participate', 'ELabel')
	G.AddStrAttrDatE(eid, creationTimePhoto, 'ETime')

	#----------add Node Comment	---------------------------------------------------------
	comments = post_comments[m]["comments"]	
	tempCommentList = {}
	tempCommentList['comment'] = []	
	if len(comments)>0:
		c = 0
		prev_iCom = -1
		for com in comments:
			c = c + 1
			i = i + 1
			iCom = i

			G.AddNode(iCom)
			commID = commID + 1
			name = 'C'+`commID`
			
			G.AddStrAttrDatN(iCom, 'comment', 'NLabel')
			G.AddStrAttrDatN(iCom, name, 'NName')
			G.AddStrAttrDatN(iCom, com['text'], 'NText')
			G.AddStrAttrDatN(iCom, com['from']['username'], 'NAuthor')
			G.AddStrAttrDatN(iCom, com['category'],'NType')
			G.AddStrAttrDatN(iCom, com['id'], 'NCommentId')
			
			creationTime = None
			if 'created_time' in com:
				creationTime = com['created_time']
			else:
				creationTime = com['createdtime']
			
			creationTime = str(creationTime)

			tempCommentList = addTempCommentList(tempCommentList, iCom, com['text'], creationTime, com['from']['username'])
			
			#add edge Photo-Comment			
			G.AddEdge(iPhoto, iCom)
			eid = G.GetEId(iPhoto,iCom)
			G.AddStrAttrDatE(eid, 'contain', 'ELabel')
			G.AddStrAttrDatE(eid, creationTime, 'ETime')
			
			#add edge Comment-Photo
			G.AddEdge(iCom, iPhoto)
			eid = G.GetEId(iCom,iPhoto)
			G.AddStrAttrDatE(eid, 'about', 'ELabel')
			G.AddStrAttrDatE(eid, creationTime, 'ETime')

			#add edge to the prev comment
			if prev_iCom != -1:
				#add edge Comment-Photo
				G.AddEdge(iCom, prev_iCom)
				eid = G.GetEId(iCom,prev_iCom)
				G.AddStrAttrDatE(eid, 'sequence', 'ELabel')
				G.AddStrAttrDatE(eid, creationTime, 'ETime')
			prev_iCom = iCom
			
			
			#----------add User Comments (Owner)---------------------------------------------------
			username = com['from']['username']
			unique = isUniqueUser(userList, username)
			if unique:
				i = i + 1
				iUserComment = i				
				
				G.AddNode(iUserComment)
				
				fullName = None
				if 'full_name' in com['from']:
					fullName = com['from']['full_name']
				elif 'fullname' in com['from']:
					fullName = com['from']['fullname']
				profilePicture = None
				if 'profile_picture' in com['from']:
					profilePicture = com['from']['profile_picture']
				elif 'profilepicture' in com['from']:
					profilePicture = com['from']['profilepicture']
				
				userList = addUserList(userList, iUserComment, username, fullName, profilePicture)

				G.AddStrAttrDatN(iUserComment, 'user', 'NLabel')
				G.AddStrAttrDatN(iUserComment, username, 'NName')
				G.AddStrAttrDatN(iUserComment, profilePicture, 'NImage')

			else:
				iUserComment = getUserId(userList, username)
			
			#add edge User - Comment --> owner comment
			G.AddEdge(iUserComment, iCom)
			eid = G.GetEId(iUserComment,iCom)
			G.AddStrAttrDatE(eid, 'write', 'ELabel')
			G.AddStrAttrDatE(eid, creationTime, 'ETime')

			#----------add Node user mentioned in the comment-------------------------------
			hashtags, userMentioned = getHashtagAndUser(com['text'])
			if len(userMentioned)>0:
				for u in userMentioned:
					#u = u.encode('utf-8')
					#print 'u:',u			
					unique = isUniqueUser(userList, u)
					if unique:
						i = i + 1;
						iUserMC = i				
						G.AddNode(iUserMC)

						G.AddStrAttrDatN(iUserMC, 'user', 'NLabel')
						G.AddStrAttrDatN(iUserMC, u, 'NName')
						G.AddStrAttrDatN(iUserMC, '0', 'NImage')

						userList = addUserList(userList, iUserMC, u)						
					else:
						iUserMC = getUserId(userList, u)

					#add edge Comment mention a User
					G.AddEdge(iCom, iUserMC)
					eid = G.GetEId(iCom,iUserMC)
					G.AddStrAttrDatE(eid, 'mention', 'ELabel')
					G.AddStrAttrDatE(eid, creationTime, 'ETime')

					#add edge REPLY User to previous comment
					#the concept is adding all list of comments
					#then find mentioned user in a comment (User A)
					#check whether User A sent a comment before
					idCommentToReply = getCommentIdFromSender(tempCommentList, u)
					#print 'idCommentToReply: ', idCommentToReply					
					
					# current comment id with id comment to reply
					if idCommentToReply != 0:
						G.AddEdge(iCom, idCommentToReply)
						eid = G.GetEId(iCom,idCommentToReply)
						G.AddStrAttrDatE(eid, 'reply', 'ELabel')
						G.AddStrAttrDatE(eid, creationTime, 'ETime')

			#----------add Node Hashtag in the comment---------------------------------------------
			#hashtags = getHashtag(com['text'])
			if len(hashtags)>0:
				for h in hashtags:					
					unique = isUniqueHashtag(hashtagList, h)
					if unique:
						i = i + 1
						iHashtag = i
						G.AddNode(iHashtag)

						#print 'hashtag',i,':', h 
						G.AddStrAttrDatN(iHashtag, 'hashtag', 'NLabel')
						G.AddStrAttrDatN(iHashtag, h, 'NName')

 						hashtagList = addHashtag(hashtagList, iHashtag, h)

					else:
						iHashtag = getHashtagId(hashtagList, h)
					
					#add edge Comment - Hashtag
					eComHas = e
					e+=1
					G.AddEdge(iCom, iHashtag, eComHas)
					G.AddStrAttrDatE(eComHas, 'tag', 'ELabel')
					G.AddStrAttrDatE(eComHas, creationTime, 'ETime')

	#----------add Node HashTag in the photo caption------------------------------------------------------
	if caption is not None:
		#hashtags = getHashtag(caption)
		hashtags, userMentioned = getHashtagAndUser(caption)
		if len(hashtags)>0:
			for h in hashtags:				
				unique = isUniqueHashtag(hashtagList, h)
				if unique:
					i = i + 1
					iHashtag = i
					G.AddNode(iHashtag)

					G.AddStrAttrDatN(iHashtag, 'hashtag', 'NLabel')
					G.AddStrAttrDatN(iHashtag, h, 'NName')

					hashtagList = addHashtag(hashtagList, iHashtag, h)
				else:
					iHashtag = getHashtagId(hashtagList, h)
				#add edge Photo - Hashtag
				G.AddEdge(iPhoto, iHashtag)
				eid = G.GetEId(iPhoto,iHashtag)
				G.AddStrAttrDatE(eid, 'tag', 'ELabel')
				G.AddStrAttrDatE(eid, creationTimePhoto, 'ETime')

	#----------add Node User that is mentioned in the photo caption--------------------------------------
		if len(userMentioned)>0:
			for u in userMentioned:
				unique = isUniqueUser(userList, u)
				if unique:
					i = i + 1;
					iUserMCp = i				
					G.AddNode(iUserMCp)

					G.AddStrAttrDatN(iUserMCp, 'user', 'NLabel')
					G.AddStrAttrDatN(iUserMCp, u, 'NName')
					G.AddStrAttrDatN(iUserMCp, '0', 'NImage')

					userList = addUserList(userList, iUserMCp, u)				
				else:
					iUserMCp = getUserId(userList, u)
				
				#add edge Photo - User
				G.AddEdge(iPhoto, iUserMCp)
				eid = G.GetEId(iPhoto,iUserMCp)
				G.AddStrAttrDatE(eid, 'mention', 'ELabel')
				G.AddStrAttrDatE(eid, creationTimePhoto, 'ETime')

	#----------add Node Location--------------------------------------------------------
	for loc in list_loc['location']:
		if loc['id'] == objId:
			i = i + 1
			iLoc = i
			city = loc['city']
			country = loc['country']
			
			unique = isUniqueLocation(locationList, city)
			if unique:
				G.AddNode(iLoc)
				nameLoc = city +', '+country
				G.AddStrAttrDatN(iLoc, 'location', 'NLabel')
				G.AddStrAttrDatN(iLoc, city, 'NCity')
				G.AddStrAttrDatN(iLoc, country, 'NCountry')

				locationList = addLocation(locationList, iLoc, city, country)
				
			else:
				iLoc = getLocationId(locationList, city)
			
			#add edge to Photo - Location
			G.AddEdge(iPhoto, iLoc)
			eid = G.GetEId(iPhoto,iLoc)
			G.AddStrAttrDatE(eid, 'located', 'ELabel')
			G.AddStrAttrDatE(eid, creationTimePhoto, 'ETime')
	m+=1

#---------------save Graph as an output file
snap.SaveEdgeList(G, "../files/G.txt", "Save as tab-separated list of edges")

#---------------save binary 
FOut = snap.TFOut("../files/G.graph")
G.Save(FOut)
print '-- start time: ', startTime
print '-- end time: ', time.time()
print '--- total: ', (time.time() - startTime), ' seconds'

cursor.close()

#-- start time:  1521025814.48
#-- end time:  1521046396.91
#--- total:  20582.4339998  seconds
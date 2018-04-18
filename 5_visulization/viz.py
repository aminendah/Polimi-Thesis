import snap

#----------Get Graph------------------------------------------------
def getGraph(filename):
	FIn = snap.TFIn(filename)
	G = snap.TNEANet.Load(FIn)

	print "Get nodes: ",G.GetNodes()
	print "Get edges: ",G.GetEdges()

	return G;


def vizxample():
	graphml = open('files/example.graphml','a')
	graphml.write('<?xml version="1.0" encoding="UTF-8"?><graphml xmlns="http://graphml.graphdrawing.org/xmlns">\n')
	graphml.write('<key attr.name="label" attr.type="string" for="node" id="label"/>\n')
	graphml.write('<key attr.name="Edge Label" attr.type="string" for="edge" id="edgelabel"/>\n')
	graphml.write('<key attr.name="weight" attr.type="double" for="edge" id="weight"/>\n')
	graphml.write('<key attr.name="r" attr.type="int" for="node" id="r"/>\n')
	graphml.write('<key attr.name="g" attr.type="int" for="node" id="g"/>\n')
	graphml.write('<key attr.name="b" attr.type="int" for="node" id="b"/>\n')
	graphml.write('<key attr.name="size" attr.type="float" for="node" id="size"/>\n')
	graphml.write('<graph edgedefault="directed">\n')

	#photo
	graphml.write('<node id="1">\n')
	graphml.write('<data key="label">Photo</data>\n')
	graphml.write('<data key="size">0</data>\n')
	graphml.write('<data key="r">0</data>\n')
	graphml.write('<data key="g">162</data>\n')
	graphml.write('<data key="b">232</data>\n')			
	graphml.write('</node>\n')

	#photo autor
	graphml.write('<node id="2">\n')
	graphml.write('<data key="label">'+"User 1"+'</data>\n')
	graphml.write('<data key="size">20</data>\n')
	graphml.write('<data key="r">247</data>\n')
	graphml.write('<data key="g">125</data>\n')
	graphml.write('<data key="b">180</data>\n')			
	graphml.write('</node>\n')

	graphml.write('<edge id="1" source="2" target="1">\n')
	graphml.write('<data key="edgelabel">write</data>\n')
	graphml.write('</edge>\n')

	#liker
	graphml.write('<node id="3">\n')
	graphml.write('<data key="label">User 2</data>\n')
	graphml.write('<data key="size">20</data>\n')
	graphml.write('<data key="r">247</data>\n')
	graphml.write('<data key="g">125</data>\n')
	graphml.write('<data key="b">180</data>\n')			
	graphml.write('</node>\n')
					
	graphml.write('<edge id="2" source="3" target="1">\n')
	graphml.write('<data key="edgelabel">like</data>\n')
	graphml.write('</edge>\n')

	#comment
	graphml.write('<node id="4">\n')
	graphml.write('<data key="label">Comment 1</data>\n')
	graphml.write('<data key="size">20</data>\n')
	graphml.write('<data key="r">50</data>\n')
	graphml.write('<data key="g">185</data>\n')
	graphml.write('<data key="b">11</data>\n')			
	graphml.write('</node>\n')
					
	graphml.write('<edge id="3" source="4" target="1">\n')
	graphml.write('<data key="edgelabel">about</data>\n')
	graphml.write('</edge>\n')

	#comment author
	graphml.write('<node id="5">\n')
	graphml.write('<data key="label">User 3</data>\n')
	graphml.write('<data key="size">20</data>\n')
	graphml.write('<data key="r">247</data>\n')
	graphml.write('<data key="g">125</data>\n')
	graphml.write('<data key="b">180</data>\n')			
	graphml.write('</node>\n')
							
	graphml.write('<edge id="4" source="5" target="4">\n')
	graphml.write('<data key="edgelabel">write</data>\n')
	graphml.write('</edge>\n')

	#comment hahstag
	graphml.write('<node id="6">\n')
	graphml.write('<data key="label">#hashtag</data>\n')
	graphml.write('<data key="size">20</data>\n')
	graphml.write('<data key="r">255</data>\n')
	graphml.write('<data key="g">128</data>\n')
	graphml.write('<data key="b">0</data>\n')			
	graphml.write('</node>\n')
						
	graphml.write('<edge id="5" source="4" target="6">\n')
	graphml.write('<data key="edgelabel">tag</data>\n')
	graphml.write('</edge>\n')

	#comment reply
	graphml.write('<node id="7">\n')
	graphml.write('<data key="label">Comment 2</data>\n')
	graphml.write('<data key="size">20</data>\n')
	graphml.write('<data key="r">50</data>\n')
	graphml.write('<data key="g">185</data>\n')
	graphml.write('<data key="b">11</data>\n')			
	graphml.write('</node>\n')
					
	graphml.write('<edge id="6" source="7" target="1">\n')
	graphml.write('<data key="edgelabel">about</data>\n')
	graphml.write('</edge>\n')
	
	graphml.write('<edge id="7" source="7" target="4">\n')
	graphml.write('<data key="edgelabel">reply</data>\n')
	graphml.write('</edge>\n')
	
	#comment author
	graphml.write('<edge id="8" source="2" target="7">\n')
	graphml.write('<data key="edgelabel">write</data>\n')
	graphml.write('</edge>\n')

	#comment	
	graphml.write('<node id="8">\n')
	graphml.write('<data key="label">Comment 3</data>\n')
	graphml.write('<data key="size">20</data>\n')
	graphml.write('<data key="r">50</data>\n')
	graphml.write('<data key="g">185</data>\n')
	graphml.write('<data key="b">11</data>\n')			
	graphml.write('</node>\n')
					
	graphml.write('<edge id="9" source="8" target="1">\n')
	graphml.write('<data key="edgelabel">about</data>\n')
	graphml.write('</edge>\n')

	#comment author
	graphml.write('<node id="9">\n')
	graphml.write('<data key="label">User 4</data>\n')
	graphml.write('<data key="size">20</data>\n')
	graphml.write('<data key="r">247</data>\n')
	graphml.write('<data key="g">125</data>\n')
	graphml.write('<data key="b">180</data>\n')			
	graphml.write('</node>\n')
							
	graphml.write('<edge id="10" source="9" target="8">\n')
	graphml.write('<data key="edgelabel">write</data>\n')
	graphml.write('</edge>\n')

	#location
	graphml.write('<node id="10">\n')
	graphml.write('<data key="label">Location</data>\n')
	graphml.write('<data key="size">20</data>\n')
	graphml.write('<data key="r">128</data>\n')
	graphml.write('<data key="g">0</data>\n')
	graphml.write('<data key="b">128</data>\n')			
	graphml.write('</node>\n')

	graphml.write('<edge id="11" source="1" target="10">\n')
	graphml.write('<data key="edgelabel">location</data>\n')
	graphml.write('</edge>\n')

	#liker
	graphml.write('<node id="11">\n')
	graphml.write('<data key="label">User 5</data>\n')
	graphml.write('<data key="size">20</data>\n')
	graphml.write('<data key="r">247</data>\n')
	graphml.write('<data key="g">125</data>\n')
	graphml.write('<data key="b">180</data>\n')			
	graphml.write('</node>\n')
					
	graphml.write('<edge id="12" source="11" target="1">\n')
	graphml.write('<data key="edgelabel">like</data>\n')
	graphml.write('</edge>\n')

	#liker
	graphml.write('<node id="12">\n')
	graphml.write('<data key="label">User 6</data>\n')
	graphml.write('<data key="size">20</data>\n')
	graphml.write('<data key="r">247</data>\n')
	graphml.write('<data key="g">125</data>\n')
	graphml.write('<data key="b">180</data>\n')			
	graphml.write('</node>\n')
					
	graphml.write('<edge id="13" source="12" target="1">\n')
	graphml.write('<data key="edgelabel">like</data>\n')
	graphml.write('</edge>\n')

	#liker
	graphml.write('<node id="13">\n')
	graphml.write('<data key="label">User 7</data>\n')
	graphml.write('<data key="size">20</data>\n')
	graphml.write('<data key="r">247</data>\n')
	graphml.write('<data key="g">125</data>\n')
	graphml.write('<data key="b">180</data>\n')			
	graphml.write('</node>\n')
					
	graphml.write('<edge id="14" source="13" target="1">\n')
	graphml.write('<data key="edgelabel">like</data>\n')
	graphml.write('</edge>\n')

	graphml.write('</graph>\n')
	graphml.write('</graphml>\n')

def viz3Photos(G):
	graphml = open('files/3photos.graphml','a')
	graphml.write('<?xml version="1.0" encoding="UTF-8"?><graphml xmlns="http://graphml.graphdrawing.org/xmlns">\n')
	graphml.write('<key attr.name="label" attr.type="string" for="node" id="label"/>\n')
	graphml.write('<key attr.name="Edge Label" attr.type="string" for="edge" id="edgelabel"/>\n')
	graphml.write('<key attr.name="weight" attr.type="double" for="edge" id="weight"/>\n')
	graphml.write('<key attr.name="r" attr.type="int" for="node" id="r"/>\n')
	graphml.write('<key attr.name="g" attr.type="int" for="node" id="g"/>\n')
	graphml.write('<key attr.name="b" attr.type="int" for="node" id="b"/>\n')
	graphml.write('<key attr.name="size" attr.type="float" for="node" id="size"/>\n')
	graphml.write('<graph edgedefault="directed">\n')

	i = 0
	for NI in G.Nodes():
		nid = NI.GetId()
		NLabel = G.GetStrAttrDatN(nid, "NLabel")	
		
		if NLabel == 'photo':
			i+=1
			NObjectId = G.GetStrAttrDatN(nid, "NObjectId")	
			
			#-------------PHOTO
			if i==1 or i == 14 or i == 15:
				iPhoto = nid				
				NAuthor_photo = G.GetStrAttrDatN(nid, "NAuthor")
				graphml.write('<node id="'+`iPhoto`+'">\n')
				graphml.write('<data key="label">Photo by '+NAuthor_photo+'</data>\n')
				graphml.write('<data key="size">50</data>\n')
				graphml.write('<data key="r">0</data>\n')
				graphml.write('<data key="g">162</data>\n')
				graphml.write('<data key="b">232</data>\n')			
				graphml.write('</node>\n')

				#------------------------------------------------IN EDGES------------------------------------------------
				for nid1 in NI.GetInEdges():
					NLabel1 = G.GetStrAttrDatN(nid1, "NLabel")
					NName1 = G.GetStrAttrDatN(nid1, "NName")								

					#-------------PHOTO AUTHOR
					if NLabel1 == "user" and NName1 == NAuthor_photo:
						
						iUser = nid1
						graphml.write('<node id="'+`iUser`+'">\n')
						graphml.write('<data key="label">'+NAuthor_photo+'</data>\n')
						graphml.write('<data key="size">20</data>\n')
						graphml.write('<data key="r">247</data>\n')
						graphml.write('<data key="g">125</data>\n')
						graphml.write('<data key="b">180</data>\n')			
						graphml.write('</node>\n')
						
						iEdge = G.GetEId(iUser,iPhoto)
						graphml.write('<edge id="'+`iEdge`+'" source="'+`iUser`+'" target="'+`iPhoto`+'">\n')
						graphml.write('<data key="edgelabel">write</data>\n')
						graphml.write('</edge>\n')

					#--------------LIKERS
					eid = G.GetEId(nid1,nid)
					ELabel_subnode = G.GetStrAttrDatE(eid, "ELabel")
					if ELabel_subnode == "like":
						iUser = nid1
						graphml.write('<node id="'+`iUser`+'">\n')
						graphml.write('<data key="label">'+NName1+'</data>\n')
						graphml.write('<data key="size">20</data>\n')
						graphml.write('<data key="r">247</data>\n')
						graphml.write('<data key="g">125</data>\n')
						graphml.write('<data key="b">180</data>\n')			
						graphml.write('</node>\n')
						
						iEdge = eid
						graphml.write('<edge id="'+`iEdge`+'" source="'+`iUser`+'" target="'+`iPhoto`+'">\n')
						graphml.write('<data key="edgelabel">like</data>\n')
						graphml.write('</edge>\n')


					#------------COMMENT
					if NLabel1 == "comment":
						NAuthor_comment = G.GetStrAttrDatN(nid1, "NAuthor")
						NCategory = G.GetStrAttrDatN(nid1, "NCategory")
						comment_name = NName1 + " " + NCategory
						id_comment = nid1

						iCom = nid1
						graphml.write('<node id="'+`iCom`+'">\n')
						graphml.write('<data key="label">'+comment_name+'</data>\n')
						graphml.write('<data key="size">20</data>\n')
						graphml.write('<data key="r">50</data>\n')
						graphml.write('<data key="g">185</data>\n')
						graphml.write('<data key="b">11</data>\n')			
						graphml.write('</node>\n')
						
						iEdge = eid
						graphml.write('<edge id="'+`iEdge`+'" source="'+`iCom`+'" target="'+`iPhoto`+'">\n')
						graphml.write('<data key="edgelabel">about</data>\n')
						graphml.write('</edge>\n')
						
						NI_c = G.GetNI(id_comment)
						
						for nid_c in NI_c.GetInEdges():						
							NName_subnode = G.GetStrAttrDatN(nid_c, "NName")
							NLabel_subnode = G.GetStrAttrDatN(nid_c, "NLabel")						
							
							eid_c = G.GetEId(nid_c,nid1)

							#--------------COMMENT AUTHOR
							if NLabel_subnode == 'user' and NName_subnode == NAuthor_comment:							
	#							
								iUser = nid_c
								graphml.write('<node id="'+`iUser`+'">\n')
								graphml.write('<data key="label">'+NAuthor_comment+'</data>\n')
								graphml.write('<data key="size">20</data>\n')
								graphml.write('<data key="r">247</data>\n')
								graphml.write('<data key="g">125</data>\n')
								graphml.write('<data key="b">180</data>\n')			
								graphml.write('</node>\n')#
								
								iEdge = eid_c
								graphml.write('<edge id="'+`iEdge`+'" source="'+`iUser`+'" target="'+`iCom`+'">\n')
								graphml.write('<data key="edgelabel">write</data>\n')
								graphml.write('</edge>\n')
						
						for nid_c in NI_c.GetOutEdges():
							NName_subnode = G.GetStrAttrDatN(nid_c, "NName")
							NLabel_subnode = G.GetStrAttrDatN(nid_c, "NLabel")

							eid_c = G.GetEId(nid1,nid_c)
							ELabel_subnode = G.GetStrAttrDatE(eid_c, "ELabel")
							
							#--------------COMMENT MENTION USER
							if ELabel_subnode == "mention":							
								iUser = nid_c
								graphml.write('<node id="'+`iUser`+'">\n')
								graphml.write('<data key="label">'+NName_subnode+'</data>\n')
								graphml.write('<data key="size">20</data>\n')
								graphml.write('<data key="r">247</data>\n')
								graphml.write('<data key="g">125</data>\n')
								graphml.write('<data key="b">180</data>\n')			
								graphml.write('</node>\n')
								
								iEdge = eid_c
								graphml.write('<edge id="'+`iEdge`+'" source="'+`iCom`+'" target="'+`iUser`+'">\n')
								graphml.write('<data key="edgelabel">mention</data>\n')
								graphml.write('</edge>\n')

							#--------------COMMENT HASHTAG
							if NLabel_subnode == "hashtag":							
								iTag = nid_c
								graphml.write('<node id="'+`iTag`+'">\n')
								graphml.write('<data key="label">'+NName_subnode+'</data>\n')
								graphml.write('<data key="size">20</data>\n')
								graphml.write('<data key="r">255</data>\n')
								graphml.write('<data key="g">128</data>\n')
								graphml.write('<data key="b">0</data>\n')			
								graphml.write('</node>\n')
								
								iEdge = eid_c
								graphml.write('<edge id="'+`iEdge`+'" source="'+`iCom`+'" target="'+`iTag`+'">\n')
								graphml.write('<data key="edgelabel">tag</data>\n')
								graphml.write('</edge>\n')

							#----------------COMMENT REPLY						
							if ELabel_subnode == "reply":
								iSource = nid1
								iTarget = nid_c						
								iEdge = eid_c
								graphml.write('<edge id="'+`iEdge`+'" source="'+`iSource`+'" target="'+`iTarget`+'">\n')
								graphml.write('<data key="edgelabel">reply</data>\n')
								graphml.write('<data key="weight">1.0</data>\n')
								graphml.write('</edge>\n')



				#------------------------------------------------OUT EDGES------------------------------------------------
				for nid1 in NI.GetOutEdges():									
					NLabel1 = G.GetStrAttrDatN(nid1, "NLabel")
					NName1 = G.GetStrAttrDatN(nid1, "NName")				

					eid = G.GetEId(nid,nid1)
					
					#--------------------PHOTO CHALLENGE
					if NLabel1 == "challenge":
						iChal = nid1
						graphml.write('<node id="'+`iChal`+'">\n')
						graphml.write('<data key="label">'+NName1+'</data>\n')
						graphml.write('<data key="size">20</data>\n')
						graphml.write('<data key="r">0</data>\n')
						graphml.write('<data key="g">0</data>\n')
						graphml.write('<data key="b">0</data>\n')			
						graphml.write('</node>\n')

						iEdge = eid
						graphml.write('<edge id="'+`iEdge`+'" source="'+`iPhoto`+'" target="'+`iChal`+'">\n')
						graphml.write('<data key="edgelabel">participate</data>\n')
						graphml.write('</edge>\n')

					#--------------------PHOTO MENTION USER
					if NLabel1 == "user":
						iUser = nid1
						graphml.write('<node id="'+`iUser`+'">\n')
						graphml.write('<data key="label">'+NName1+'</data>\n')
						graphml.write('<data key="size">20</data>\n')
						graphml.write('<data key="r">247</data>\n')
						graphml.write('<data key="g">125</data>\n')
						graphml.write('<data key="b">180</data>\n')			
						graphml.write('</node>\n')

						iEdge = eid
						graphml.write('<edge id="'+`iEdge`+'" source="'+`iPhoto`+'" target="'+`iUser`+'">\n')
						graphml.write('<data key="edgelabel">mention</data>\n')
						graphml.write('</edge>\n')

					#--------------------PHOTO TAG HASHTAG
					if NLabel1 == "hashtag":
						iTag = nid1
						graphml.write('<node id="'+`iTag`+'">\n')
						graphml.write('<data key="label">'+NName1+'</data>\n')
						graphml.write('<data key="size">20</data>\n')
						graphml.write('<data key="r">255</data>\n')
						graphml.write('<data key="g">128</data>\n')
						graphml.write('<data key="b">0</data>\n')			
						graphml.write('</node>\n')

						iEdge = eid
						graphml.write('<edge id="'+`iEdge`+'" source="'+`iPhoto`+'" target="'+`iTag`+'">\n')
						graphml.write('<data key="edgelabel">tag</data>\n')
						graphml.write('</edge>\n')

					#--------------------PHOTO LOCATION
					if NLabel1 == "location":
						iLoc = nid1
						graphml.write('<node id="'+`iLoc`+'">\n')
						graphml.write('<data key="label">'+NName1+'</data>\n')
						graphml.write('<data key="size">20</data>\n')
						graphml.write('<data key="r">128</data>\n')
						graphml.write('<data key="g">0</data>\n')
						graphml.write('<data key="b">128</data>\n')			
						graphml.write('</node>\n')

						iEdge = eid
						graphml.write('<edge id="'+`iEdge`+'" source="'+`iPhoto`+'" target="'+`iLoc`+'">\n')
						graphml.write('<data key="edgelabel">located</data>\n')
						graphml.write('</edge>\n')

	graphml.write('</graph>\n')
	graphml.write('</graphml>\n')

def vizCoversation(G, ID):
	graphml = open('files/conv_'+`ID`+'.graphml','a')
	graphml.write('<?xml version="1.0" encoding="UTF-8"?><graphml xmlns="http://graphml.graphdrawing.org/xmlns">\n')
	graphml.write('<key attr.name="label" attr.type="string" for="node" id="label"/>\n')
	graphml.write('<key attr.name="Edge Label" attr.type="string" for="edge" id="edgelabel"/>\n')
	graphml.write('<key attr.name="weight" attr.type="double" for="edge" id="weight"/>\n')
	graphml.write('<key attr.name="r" attr.type="int" for="node" id="r"/>\n')
	graphml.write('<key attr.name="g" attr.type="int" for="node" id="g"/>\n')
	graphml.write('<key attr.name="b" attr.type="int" for="node" id="b"/>\n')
	graphml.write('<key attr.name="size" attr.type="float" for="node" id="size"/>\n')
	graphml.write('<graph edgedefault="directed">\n')

	i = 0
	for NI in G.Nodes():
		nid = NI.GetId()
		NLabel = G.GetStrAttrDatN(nid, "NLabel")	
		
		if NLabel == 'photo':
			i+=1
			NObjectId = G.GetStrAttrDatN(nid, "NObjectId")	
			
			#-------------PHOTO
			#if NObjectId == objID:
			if i == ID:
				iPhoto = nid				
				NAuthor_photo = G.GetStrAttrDatN(nid, "NAuthor")
				graphml.write('<node id="'+`iPhoto`+'">\n')
				graphml.write('<data key="label">Photo by '+NAuthor_photo+'</data>\n')
				graphml.write('<data key="size">50</data>\n')
				graphml.write('<data key="r">0</data>\n')
				graphml.write('<data key="g">162</data>\n')
				graphml.write('<data key="b">232</data>\n')			
				graphml.write('</node>\n')

				#------------------------------------------------IN EDGES------------------------------------------------
				for nid1 in NI.GetInEdges():
					NLabel1 = G.GetStrAttrDatN(nid1, "NLabel")
					NName1 = G.GetStrAttrDatN(nid1, "NName")								

					#-------------PHOTO AUTHOR
					if NLabel1 == "user" and NName1 == NAuthor_photo:
						
						iUser = nid1
						graphml.write('<node id="'+`iUser`+'">\n')
						graphml.write('<data key="label">'+NAuthor_photo+'</data>\n')
						graphml.write('<data key="size">20</data>\n')
						graphml.write('<data key="r">247</data>\n')
						graphml.write('<data key="g">125</data>\n')
						graphml.write('<data key="b">180</data>\n')			
						graphml.write('</node>\n')
						
						iEdge = G.GetEId(iUser,iPhoto)
						graphml.write('<edge id="'+`iEdge`+'" source="'+`iUser`+'" target="'+`iPhoto`+'">\n')
						graphml.write('<data key="edgelabel">write</data>\n')
						graphml.write('</edge>\n')


					eid = G.GetEId(nid1,nid)
					#------------COMMENT
					if NLabel1 == "comment":
						NAuthor_comment = G.GetStrAttrDatN(nid1, "NAuthor")
						NCategory = G.GetStrAttrDatN(nid1, "NCategory")
						comment_name = NName1 + " " + NCategory
						id_comment = nid1

						#comment color:
						rgb = [0,0,0]
						if NCategory == "thank":
							rgb[0] = 192
						elif NCategory == "congratulation":
							rgb[0] = 192
							rgb[1] = 80
							rgb[2] = 77
						elif NCategory == "agreement":
							rgb[0] = 247
							rgb[1] = 150
							rgb[2] = 70
						elif NCategory == "positive":
							rgb[0] = 255
							rgb[1] = 192
							rgb[2] = 0
						elif NCategory == "invitation":
							rgb[0] = 148
							rgb[1] = 208
							rgb[2] = 80
						elif NCategory == "food":
							rgb[0] = 0
							rgb[1] = 176
							rgb[2] = 80
						elif NCategory == "greeting":
							rgb[0] = 0
							rgb[1] = 112
							rgb[2] = 192
						elif NCategory == "question":
							rgb[0] = 0
							rgb[1] = 32
							rgb[2] = 96
						elif NCategory == "hahstag":
							rgb[0] = 112
							rgb[1] = 48
							rgb[2] = 160
						else:
							rgb[0] = 255
							rgb[1] = 192
							rgb[2] = 0


						iCom = nid1
						graphml.write('<node id="'+`iCom`+'">\n')
						graphml.write('<data key="label">'+comment_name+'</data>\n')
						graphml.write('<data key="size">20</data>\n')
						graphml.write('<data key="r">'+`rgb[0]`+'</data>\n')
						graphml.write('<data key="g">'+`rgb[1]`+'</data>\n')
						graphml.write('<data key="b">'+`rgb[2]`+'</data>\n')			
						graphml.write('</node>\n')
						
						iEdge = eid
						graphml.write('<edge id="'+`iEdge`+'" source="'+`iCom`+'" target="'+`iPhoto`+'">\n')
						graphml.write('<data key="edgelabel">about</data>\n')
						graphml.write('</edge>\n')
						
						NI_c = G.GetNI(id_comment)
						
						for nid_c in NI_c.GetInEdges():						
							NName_subnode = G.GetStrAttrDatN(nid_c, "NName")
							NLabel_subnode = G.GetStrAttrDatN(nid_c, "NLabel")						
							
							eid_c = G.GetEId(nid_c,nid1)

							#--------------COMMENT AUTHOR
							if NLabel_subnode == 'user' and NName_subnode == NAuthor_comment:							
	#							
								iUser = nid_c
								graphml.write('<node id="'+`iUser`+'">\n')
								graphml.write('<data key="label">'+NAuthor_comment+'</data>\n')
								graphml.write('<data key="size">20</data>\n')
								graphml.write('<data key="r">247</data>\n')
								graphml.write('<data key="g">125</data>\n')
								graphml.write('<data key="b">180</data>\n')			
								graphml.write('</node>\n')#
								
								iEdge = eid_c
								graphml.write('<edge id="'+`iEdge`+'" source="'+`iUser`+'" target="'+`iCom`+'">\n')
								graphml.write('<data key="edgelabel">write</data>\n')
								graphml.write('</edge>\n')
						
						for nid_c in NI_c.GetOutEdges():
							NName_subnode = G.GetStrAttrDatN(nid_c, "NName")
							NLabel_subnode = G.GetStrAttrDatN(nid_c, "NLabel")

							eid_c = G.GetEId(nid1,nid_c)
							ELabel_subnode = G.GetStrAttrDatE(eid_c, "ELabel")
							
							#--------------COMMENT MENTION USER
							if ELabel_subnode == "mention":							
								iUser = nid_c
								graphml.write('<node id="'+`iUser`+'">\n')
								graphml.write('<data key="label">'+NName_subnode+'</data>\n')
								graphml.write('<data key="size">20</data>\n')
								graphml.write('<data key="r">247</data>\n')
								graphml.write('<data key="g">125</data>\n')
								graphml.write('<data key="b">180</data>\n')			
								graphml.write('</node>\n')
								
								iEdge = eid_c
								graphml.write('<edge id="'+`iEdge`+'" source="'+`iCom`+'" target="'+`iUser`+'">\n')
								graphml.write('<data key="edgelabel">mention</data>\n')
								graphml.write('</edge>\n')


							#----------------COMMENT REPLY						
							if ELabel_subnode == "reply":
								iSource = nid1
								iTarget = nid_c						
								iEdge = eid_c
								graphml.write('<edge id="'+`iEdge`+'" source="'+`iSource`+'" target="'+`iTarget`+'">\n')
								graphml.write('<data key="edgelabel">reply</data>\n')
								graphml.write('<data key="weight">1.5</data>\n')
								graphml.write('</edge>\n')


	graphml.write('</graph>\n')
	graphml.write('</graphml>\n')

if __name__ == '__main__':
	G = getGraph("../files/G_3.graph")
	#vizExample()
	#viz3Photos(G)
	vizCoversation(G, 12100)

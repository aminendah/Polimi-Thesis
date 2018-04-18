import snap
import json
import time
from pprint import pprint

cats = ["thank","positive","food","greeting","congratulation","agreement","invitation","hashtag"]

#----------Get Graph------------------------------------------------
def getGraph(filename):
	FIn = snap.TFIn(filename)
	G = snap.TNEANet.Load(FIn)

	print "Get nodes: ",G.GetNodes()
	print "Get edges: ",G.GetEdges()

	return G;

#----------Graph Comment Pattern
def findCommentPattern2(G, source, target):
	count = 0
	for NI in G.Nodes():
		nid = NI.GetId()
		NLabel = G.GetStrAttrDatN(nid, "NLabel")	
		
		if NLabel == 'comment':
			NCategorySource = G.GetStrAttrDatN(nid, "NCategory")
			#------------------------------------------------OUT EDGES------------------------------------------------
			for nidout in NI.GetOutEdges():
				NLabelOut = G.GetStrAttrDatN(nidout, "NLabel")				
				eid = G.GetEId(nid,nidout)				
				ELabel = G.GetStrAttrDatE(eid, "ELabel")
				if NLabelOut == "comment" and ELabel == "reply":
					NCategoryTarget = G.GetStrAttrDatN(nidout, "NCategory")
					#print NCategorySource,"--->",NCategoryTarget
					if NCategorySource == source and NCategoryTarget == target:
						count +=1
	return count

def findCommentPattern3(G, source, target1, target2):
	count = 0
	for NI in G.Nodes():
		nid = NI.GetId()
		NLabel = G.GetStrAttrDatN(nid, "NLabel")	
		
		if NLabel == 'comment':
			NCategorySource = G.GetStrAttrDatN(nid, "NCategory")
			
			#------------------------------------------------OUT EDGES------------------------------------------------
			for nidout in NI.GetOutEdges():
				NLabelOut = G.GetStrAttrDatN(nidout, "NLabel")				
				eid = G.GetEId(nid,nidout)
				ELabel = G.GetStrAttrDatE(eid, "ELabel")
				if NLabelOut == "comment" and ELabel == "reply":
					NCategoryTarget1 = G.GetStrAttrDatN(nidout, "NCategory")

					NI2 = G.GetNI(nidout)
					#----------------------------------------OUT EDGES------------------------------------------------
					for nidout2 in NI2.GetOutEdges():
						NLabelOut2 = G.GetStrAttrDatN(nidout2, "NLabel")				
						eid2 = G.GetEId(nidout,nidout2)
						ELabel2 = G.GetStrAttrDatE(eid, "ELabel")
						if NLabelOut2 == "comment" and ELabel2 == "reply":
							NCategoryTarget2 = G.GetStrAttrDatN(nidout2, "NCategory")
							if NCategorySource == source and NCategoryTarget1 == target1 and NCategoryTarget2 == target2:
								count += 1
	return count

def findCommentPattern4(G, source, target1, target2, target3):
	count = 0
	for NI in G.Nodes():
		nid = NI.GetId()
		NLabel = G.GetStrAttrDatN(nid, "NLabel")	
		
		if NLabel == 'comment':
			NCategorySource = G.GetStrAttrDatN(nid, "NCategory")
			#------------------------------------------------OUT EDGES------------------------------------------------
			for nidout in NI.GetOutEdges():
				NLabelOut = G.GetStrAttrDatN(nidout, "NLabel")				
				eid = G.GetEId(nid,nidout)				
				ELabel = G.GetStrAttrDatE(eid, "ELabel")
				if NLabelOut == "comment" and ELabel == "reply":
					NCategoryTarget1 = G.GetStrAttrDatN(nidout, "NCategory")
					NI2 = G.GetNI(nidout)
					#----------------------------------------OUT EDGES------------------------------------------------
					for nidout2 in NI2.GetOutEdges():
						NLabelOut2 = G.GetStrAttrDatN(nidout2, "NLabel")				
						eid2 = G.GetEId(nidout,nidout2)
						ELabel2 = G.GetStrAttrDatE(eid2, "ELabel")
						if NLabelOut2 == "comment" and ELabel2 == "reply":
							NCategoryTarget2 = G.GetStrAttrDatN(nidout2, "NCategory")
							NI3 = G.GetNI(nidout2)
							#----------------------------------------OUT EDGES------------------------------------------------
							for nidout3 in NI3.GetOutEdges():
								NLabelOut3 = G.GetStrAttrDatN(nidout3, "NLabel")				
								eid3 = G.GetEId(nidout2,nidout3)
								ELabel3 = G.GetStrAttrDatE(eid3, "ELabel")
								if NLabelOut3 == "comment" and ELabel3 == "reply":
									NCategoryTarget3 = G.GetStrAttrDatN(nidout3, "NCategory")
									if NCategorySource == source and NCategoryTarget1 == target1 and NCategoryTarget2 == target2 and NCategoryTarget3 == target3:
										count += 1
	return count

def getMatrix2D(G):
	w, h = 8, 8;
	matrix = [[0 for x in range(w)] for y in range(h)] 

	file_txt = open('count_pattern.txt','a')

	for i in range(0,h):
		for j in range(0,w):
			matrix[i][j]=0
	pprint(matrix)
	for i in range(0,h):
		for j in range(0,w):
			count = findCommentPattern2(G, cats[i], cats[j])
			print cats[i], cats[j], count
			matrix[i][j]=count
	pprint(matrix)
	with open('matrix2D.txt', 'w') as outfile:  
	    json.dump(matrix, outfile)

def getMatrix3D(G):
	matrix = []
	matrix.append(["thank","positive"])
	matrix.append(["positive","positive"])
	matrix.append(["positive","food"])
	matrix.append(["food","positive"])
	matrix.append(["thank","food"])
	matrix.append(["thank","thank"])
	matrix.append(["thank","greeting"])
	matrix.append(["greeting","positive"])
	matrix.append(["food","food"])
	matrix.append(["positive","thank"])


	pprint(matrix)

	for i in range(0,8): 
		for j in range(0,10):
			count = findCommentPattern3(G, cats[i], matrix[j][0], matrix[j][1])
			#file_txt.write(cats[i]+"->"+matrix[j][0]+"->"+matrix[j][1]+"="+`count`+"\n")
			print cats[i],"->",matrix[j][0],"->",matrix[j][1],"=",count
		
			count = findCommentPattern3(G, matrix[j][0], matrix[j][1], cats[i])
			#file_txt.write(matrix[j][0]+"->"+matrix[j][1]+"->"+cats[i]+"="+`count`+"\n")
			print matrix[j][0],"->",matrix[j][1],"->",cats[i],"=",count

def getMatrix4D(G):
	matrix = []
	matrix.append(["thank","thank","positive"])
	matrix.append(["positive","positive","positive"])
	matrix.append(["thank","positive","positive"])
	matrix.append(["positive","thank","positive"])
	matrix.append(["thank","thank","thank"])
	matrix.append(["thank","positive","thank"])
	matrix.append(["thank","positive","food"])
	matrix.append(["positive","positive","food"])
	matrix.append(["positive","food","positive"])
	matrix.append(["food","positive","positive"])

	pprint(matrix)

	file_txt = open('4D.txt','a')

	for i in range(0,8):	
		for j in range(0,10):
			count = findCommentPattern4(G, cats[i], matrix[j][0], matrix[j][1], matrix[j][2])		
			print cats[i],"->",matrix[j][0],"->",matrix[j][1],"->",matrix[j][2],"=",count
			file_txt.write(cats[i]+"->"+matrix[j][0]+"->"+matrix[j][1]+"->"+matrix[j][2]+"="+`count`+"\n")		
			
			count = findCommentPattern4(G, matrix[j][0], matrix[j][1], matrix[j][2], cats[i])
			print matrix[j][0],"->",matrix[j][1],"->",matrix[j][2],"->",cats[i],"=",count
			file_txt.write(matrix[j][0]+"->"+matrix[j][1]+"->"+matrix[j][2]+"->"+cats[i]+"="+`count`+"\n")

def countDuration(l_count_duration, minutes):
	#0=5min, 1=15min, 2=0.5h, 3=1h, 4=>2h, 5=>3h, 6=>6h, 7=>12h, 8=>1day, 9=>1w
	if minutes<=5:
		l_count_duration[0]+=1		
	elif minutes>5 and minutes<=15:
		l_count_duration[1]+=1		
	elif minutes>15 and minutes<=30:
		l_count_duration[2]+=1		
	elif minutes>30 and minutes<=60:
		l_count_duration[3]+=1		
	elif minutes>60 and minutes<=120:
		l_count_duration[4]+=1		
	elif minutes>120 and minutes<=180:
		l_count_duration[5]+=1		
	elif minutes>180 and minutes<=360:
		l_count_duration[6]+=1		
	elif minutes>360 and minutes<=720:
		l_count_duration[7]+=1
	elif minutes>720 and minutes<=1440:
		l_count_duration[8]+=1		
	elif minutes>1440 and minutes<=10080:
		l_count_duration[9]+=1		
	elif minutes>1080:
		l_count_duration[10]+=1	

	return l_count_duration;

def getDurationUser3D(G,source, target1, target2):
	count = 0
	list_user = []
	list_duration = []
	#max1 = 80827
	#max2 = 64973
	sumMinutes1 = 0
	sumMinutes2 = 0

	#0=5min, 1=15min, 2=0.5h, 3=1h, 4=>2h, 5=>3h, 6=>6h, 7=>12h, 8=>1day, 9=>1w
	l_count_duration1 = []
	l_count_duration2 = []

	for i in range(0,11):
		l_count_duration1.append(0)
		l_count_duration2.append(0)

	for NI in G.Nodes():
		nid = NI.GetId()
		NLabel = G.GetStrAttrDatN(nid, "NLabel")	
		
		if NLabel == 'comment':
			NCategorySource = G.GetStrAttrDatN(nid, "NCategory")
			NAuthorSource = G.GetStrAttrDatN(nid, "NAuthor")
			
			#time
			ETime_=0
			for nidin in NI.GetInEdges():
				NLabel_ = G.GetStrAttrDatN(nidin, "NLabel")
				eid_ = G.GetEId(nidin,nid)
				ELabel_ = G.GetStrAttrDatE(eid_, "ELabel")
				if NLabel_ == "user" and ELabel_ == "write":
					ETime_ = G.GetStrAttrDatE(eid_, "ETime")
			ETimeSource = ETime_
			
			#------------------------------------------------OUT EDGES------------------------------------------------
			for nidout in NI.GetOutEdges():
				NLabelOut = G.GetStrAttrDatN(nidout, "NLabel")				
				eid = G.GetEId(nid,nidout)
				ELabel = G.GetStrAttrDatE(eid, "ELabel")
				if NLabelOut == "comment" and ELabel == "reply":
					NCategoryTarget1 = G.GetStrAttrDatN(nidout, "NCategory")
					NAuthorTarget1 = G.GetStrAttrDatN(nidout, "NAuthor")
					
					NI2 = G.GetNI(nidout)					

					#time
					ETime_=0
					for nidin in NI2.GetInEdges():
						NLabel_ = G.GetStrAttrDatN(nidin, "NLabel")
						eid_ = G.GetEId(nidin,nidout)
						ELabel_ = G.GetStrAttrDatE(eid_, "ELabel")
						if NLabel_ == "user" and ELabel_ == "write":
							ETime_ = G.GetStrAttrDatE(eid_, "ETime")
					ETimeTarget1 = ETime_
					
					#----------------------------------------OUT EDGES------------------------------------------------
					for nidout2 in NI2.GetOutEdges():
						NLabelOut2 = G.GetStrAttrDatN(nidout2, "NLabel")				
						eid2 = G.GetEId(nidout,nidout2)
						ELabel2 = G.GetStrAttrDatE(eid, "ELabel")

						if NLabelOut2 == "comment" and ELabel2 == "reply":
							NCategoryTarget2 = G.GetStrAttrDatN(nidout2, "NCategory")
							NAuthorTarget2 = G.GetStrAttrDatN(nidout2, "NAuthor")


							NI3 = G.GetNI(nidout2)
							#time
							ETime_=0
							for nidin in NI3.GetInEdges():
								NLabel_ = G.GetStrAttrDatN(nidin, "NLabel")
								eid_ = G.GetEId(nidin,nidout2)
								ELabel_ = G.GetStrAttrDatE(eid_, "ELabel")
								if NLabel_ == "user" and ELabel_ == "write":
									ETime_ = G.GetStrAttrDatE(eid_, "ETime")
							ETimeTarget2 = ETime_

							if NCategorySource == source and NCategoryTarget1 == target1 and NCategoryTarget2 == target2:
								count += 1															
								listU = [NAuthorSource, NAuthorTarget1, NAuthorTarget2]
								setU = set(listU)
								list_user.append(len(setU))

								duration1 = float(ETimeSource) - float(ETimeTarget1)
								duration2 = float(ETimeTarget1) - float(ETimeTarget2)
								
								minutes1, seconds = divmod(duration1, 60)
								minutes2, seconds = divmod(duration2, 60)
								
								sumMinutes1 = sumMinutes1 + minutes1
								sumMinutes2 = sumMinutes2 + minutes2
								
								list_duration.append([minutes1,minutes2])
								l_count_duration1 = countDuration(l_count_duration1, minutes1)
								l_count_duration2 = countDuration(l_count_duration2, minutes2)
								
								 
	#print count
	#print sumMinutes1/count
	#print sumMinutes2/count
	pprint(list_user)
	#pprint(list_duration)
	#pprint(l_count_duration1)
	#pprint(l_count_duration2)
	

	
def getDurationUser4D(G,source, target1, target2, target3):
	count = 0
	list_user = []
	list_duration = []
	#max1 = 80827
	#max2 = 64973
	sumMinutes1 = 0
	sumMinutes2 = 0
	sumMinutes3 = 0

	#0=5min, 1=15min, 2=0.5h, 3=1h, 4=>2h, 5=>3h, 6=>6h, 7=>12h, 8=>1day, 9=>1w
	l_count_duration1 = []
	l_count_duration2 = []
	l_count_duration3 = []

	for i in range(0,11):
		l_count_duration1.append(0)
		l_count_duration2.append(0)
		l_count_duration3.append(0)

	for NI in G.Nodes():
		nid = NI.GetId()
		NLabel = G.GetStrAttrDatN(nid, "NLabel")	
		
		if NLabel == 'comment':
			NCategorySource = G.GetStrAttrDatN(nid, "NCategory")
			NAuthorSource = G.GetStrAttrDatN(nid, "NAuthor")

			#time
			ETime_=0
			for nidin in NI.GetInEdges():
				NLabel_ = G.GetStrAttrDatN(nidin, "NLabel")
				eid_ = G.GetEId(nidin,nid)
				ELabel_ = G.GetStrAttrDatE(eid_, "ELabel")
				if NLabel_ == "user" and ELabel_ == "write":
					ETime_ = G.GetStrAttrDatE(eid_, "ETime")
			ETimeSource = ETime_

			#------------------------------------------------OUT EDGES------------------------------------------------
			for nidout in NI.GetOutEdges():
				NLabelOut = G.GetStrAttrDatN(nidout, "NLabel")				
				eid = G.GetEId(nid,nidout)				
				ELabel = G.GetStrAttrDatE(eid, "ELabel")
				if NLabelOut == "comment" and ELabel == "reply":
					NCategoryTarget1 = G.GetStrAttrDatN(nidout, "NCategory")
					NAuthorTarget1 = G.GetStrAttrDatN(nidout, "NAuthor")
					
					NI2 = G.GetNI(nidout)

					#time
					ETime_=0
					for nidin in NI2.GetInEdges():
						NLabel_ = G.GetStrAttrDatN(nidin, "NLabel")
						eid_ = G.GetEId(nidin,nidout)
						ELabel_ = G.GetStrAttrDatE(eid_, "ELabel")
						if NLabel_ == "user" and ELabel_ == "write":
							ETime_ = G.GetStrAttrDatE(eid_, "ETime")
					ETimeTarget1 = ETime_

					#----------------------------------------OUT EDGES------------------------------------------------
					for nidout2 in NI2.GetOutEdges():
						NLabelOut2 = G.GetStrAttrDatN(nidout2, "NLabel")				
						eid2 = G.GetEId(nidout,nidout2)
						ELabel2 = G.GetStrAttrDatE(eid2, "ELabel")
						if NLabelOut2 == "comment" and ELabel2 == "reply":
							NCategoryTarget2 = G.GetStrAttrDatN(nidout2, "NCategory")
							NAuthorTarget2 = G.GetStrAttrDatN(nidout2, "NAuthor")
							
							NI3 = G.GetNI(nidout2)

							#time
							ETime_=0
							for nidin in NI3.GetInEdges():
								NLabel_ = G.GetStrAttrDatN(nidin, "NLabel")
								eid_ = G.GetEId(nidin,nidout2)
								ELabel_ = G.GetStrAttrDatE(eid_, "ELabel")
								if NLabel_ == "user" and ELabel_ == "write":
									ETime_ = G.GetStrAttrDatE(eid_, "ETime")
							ETimeTarget2 = ETime_

							#----------------------------------------OUT EDGES------------------------------------------------
							for nidout3 in NI3.GetOutEdges():
								NLabelOut3 = G.GetStrAttrDatN(nidout3, "NLabel")				
								eid3 = G.GetEId(nidout2,nidout3)
								ELabel3 = G.GetStrAttrDatE(eid3, "ELabel")

								if NLabelOut3 == "comment" and ELabel3 == "reply":
									NCategoryTarget3 = G.GetStrAttrDatN(nidout3, "NCategory")
									NAuthorTarget3 = G.GetStrAttrDatN(nidout3, "NAuthor")

									NI4 = G.GetNI(nidout3)

									#time
									ETime_=0
									for nidin in NI4.GetInEdges():
										NLabel_ = G.GetStrAttrDatN(nidin, "NLabel")
										eid_ = G.GetEId(nidin,nidout3)
										ELabel_ = G.GetStrAttrDatE(eid_, "ELabel")
										if NLabel_ == "user" and ELabel_ == "write":
											ETime_ = G.GetStrAttrDatE(eid_, "ETime")
									ETimeTarget3 = ETime_
							
									if NCategorySource == source and NCategoryTarget1 == target1 and NCategoryTarget2 == target2 and NCategoryTarget3 == target3:
										count += 1
										listU = [NAuthorSource, NAuthorTarget1, NAuthorTarget2, NAuthorTarget3]
										setU = set(listU)
										list_user.append(len(setU))
										
										print ETimeSource, ETimeTarget1, ETimeTarget2, ETimeTarget3
										duration1 = float(ETimeSource) - float(ETimeTarget1)
										duration2 = float(ETimeTarget1) - float(ETimeTarget2)
										duration3 = float(ETimeTarget2) - float(ETimeTarget3)
										minutes1, seconds = divmod(duration1, 60)
										minutes2, seconds = divmod(duration2, 60)
										minutes3, seconds = divmod(duration3, 60)

										sumMinutes1 = sumMinutes1 + minutes1
										sumMinutes2 = sumMinutes2 + minutes2
										sumMinutes3 = sumMinutes3 + minutes3
										
										list_duration.append([minutes1,minutes2, minutes3])
										l_count_duration1 = countDuration(l_count_duration1, minutes1)
										l_count_duration2 = countDuration(l_count_duration2, minutes2)
										l_count_duration3 = countDuration(l_count_duration3, minutes3)
	#print count
	pprint(list_user)
	#pprint(l_count_duration1)
	#pprint(l_count_duration2)
	#pprint(l_count_duration3)
	#print sumMinutes1/count
	#print sumMinutes2/count
	#print sumMinutes3/count

if __name__ == '__main__':
	G = getGraph("../files/G_3.graph")
	#getMatrix2D(G)
	#getMatrix3D(G)
	#getMatrix4D(G)
	#getDurationUser3D(G, "thank", "thank", "positive")
	getDurationUser4D(G, "thank", "thank", "thank", "positive")
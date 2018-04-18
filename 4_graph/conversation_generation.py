import snap
import json
import time
import sys
from pprint import pprint

#----------Get Graph------------------------------------------------
def getGraph(filename):
	FIn = snap.TFIn(filename)
	G = snap.TNEANet.Load(FIn)

	print "Get nodes: ",G.GetNodes()
	print "Get edges: ",G.GetEdges()

	return G;

#----------Read Json File
def getListFromFile(filename):
	with open(filename) as data_file:
		listData = json.load(data_file)

	return listData;

#----------Get Conversation
def isCommentExist(listC, name):
	exist = False
	id = -1
	i = 0
	for d in listC:
		if name in d:
			exist = True
			id = i
		i+=1
	return id, exist;

def addConv(listC, source, target):
	exist_t = False
	exist_s = False
	id_t, exist_t = isCommentExist(listC, target)
	id_s, exist_s = isCommentExist(listC, source)

	if exist_t and exist_s == False:
		listC[id_t].append(source)		

	elif exist_s and exist_t == False:
		listC[id_s].append(target)		

	elif exist_s== False and exist_t==False:
		listC.append([target, source])
		n = len(listC)		
	else:
		listC[id_t].append(source)
	
	n_l = []
	#print listC
	for ll in listC:
		ll = list(set(ll))
		n_l.append(ll)
	#print "new",n_l
	return n_l;

def mergeList(data):
	union = set()
	for d in data:
		union = union.union(d)
	data_unique = sorted(list(union))
	
	temp_data = data
	j = 0
	for d in data_unique:
		j+=1		
		l_index = []
		i = 0		
		for l in data:			
			if d in l:
				l_index.append(i)				
			i+=1		
		n = len(l_index)		
		if n>1:
			temp = []		
			for li in l_index:
				temp = temp+data[li]
			temp_list = sorted(list(set(temp)))
			flag = 0
			for li in l_index:
				if flag==0:									
					del data[li]					
				else:					
					del data[li-flag]
				flag+=1			
			data.append(temp_list)
	return data;

def getConvObject(list_c, list_c_one):
	new_list = []
	union = set()
	for d in list_c:
		union = union.union(d)
	data_unique = sorted(list(union))

	for d in list_c: #per conversation
		conv_obj = []
		c_count = len(d)
		c_data = []
		for c in d: # each conversation has many comments
			c_name = ""
			c_category = ""
			c_time = ""
			for oc in list_c_one: # to find comment within conversation in list all conversation to get the obj info
				if c == oc["name"]:
					c_name = oc["name"]
					c_category = oc["category"]
					c_time = oc["time"]
					c_text = oc["text"]
			c_data.append({
				"name":c_name,
				"category":c_category,
				"time":c_time,
				"text":c_text
				})
		
		new_list.append({
			"count":c_count,
			"data": c_data
			})

	tot_one = 0
	for d in list_c_one:
		if d["name"] not in data_unique:
			tot_one +=1
			c_name = d["name"]
			c_category = d["category"]
			c_time = d["time"]
			c_text = d["text"]
			
			new_list.append({
			"count":1,
			"data": [{
				"name":c_name,
				"category":c_category,
				"time":c_time,
				"text": c_text
				}]
			})
			
	return new_list;

def setConversation():
	G = getGraph("../files/G_3.graph")

	outfile1 = open('nconv_perpost.csv','a')
	outfile2 = open("ncom_perconv.csv","a")

	id_num_conv = []
	for i in range(0,200):
		#print i
		id_num_conv.append(0)

	list_conv = {}
	list_conv["conv"] = []

	i = 0
	for NI in G.Nodes():	
		nid = NI.GetId()
		NLabel = G.GetStrAttrDatN(nid, "NLabel")	
		
		#-------------PHOTO
		if NLabel == 'photo':
			NObjectId = G.GetStrAttrDatN(nid, "NObjectId")	
			
			list_c = []		

			
			list_c_one = []
			n_comments = 0
			#------------------------------------------------IN EDGES------------------------------------------------
			for nid1 in NI.GetInEdges():
				NLabel1 = G.GetStrAttrDatN(nid1, "NLabel")
				NName1 = G.GetStrAttrDatN(nid1, "NName")
				eid = G.GetEId(nid1,nid)
				ETime = G.GetStrAttrDatE(eid, "ETime")
				#------------COMMENT				
				if NLabel1 == "comment":
					n_comments+=1
					NAuthor_comment = G.GetStrAttrDatN(nid1, "NAuthor")
					NCategory = G.GetStrAttrDatN(nid1, "NCategory")
					NText = G.GetStrAttrDatN(nid1, "NText")
					#print NText
					comment_name = NName1 + " " + NCategory
					iCom = nid1	
					NI_c = G.GetNI(iCom)
					list_c_one.append({
						"name": NName1,
						"category": NCategory,
						"time": ETime,
						"text": NText
						})
					for nid_c in NI_c.GetOutEdges():
						NName_subnode = G.GetStrAttrDatN(nid_c, "NName")
						NLabel_subnode = G.GetStrAttrDatN(nid_c, "NLabel")
						eid_c = G.GetEId(nid1,nid_c)
						ELabel_subnode = G.GetStrAttrDatE(eid_c, "ELabel")
						#----------------COMMENT REPLY						
						if ELabel_subnode == "reply":
							iSource = nid1
							iTarget = nid_c						
							iEdge = eid_c
							nSource = G.GetStrAttrDatN(iSource, "NName")
							nTarget = G.GetStrAttrDatN(iTarget, "NName")							
							#print nSource, nTarget
							#outfile.write(nSource+" "+nTarget+"\n")
							list_c = addConv(list_c, nSource, nTarget)	
							textSource = NName_subnode = G.GetStrAttrDatN(iSource, "NName")
							textTarget = NName_subnode = G.GetStrAttrDatN(iTarget, "NName")
				
			#list conversation with at least two comments
			list_c = mergeList(list_c)
			#combine comment with no reply and just 1 conversation
			#print "len all c:", len(list_c_one)
			#print "len conversation:", len(list_c)
			new_list = getConvObject(list_c, list_c_one)

			list_conv["conv"].append({
				"object_id": NObjectId,
				"conversation": new_list,
				"count": len(new_list)
				})
			i+=1
			n_conv = len(new_list)
			n_conv_2 = 0
			
			for c in new_list:
				n_c = len(c["data"])
				print "n_c:", n_c		
				id_num_conv[n_c] += 1
				if c["count"]>1:
					n_conv_2+=1
			print i,n_comments,n_conv,n_conv_2
			outfile1.write(`n_comments`+","+`n_conv`+","+`n_conv_2`+"\n")


	with open('conv_obj_all.txt', 'w') as outfile:  
	    json.dump(list_conv, outfile)

	for i in id_num_conv:
		#print i
		outfile2.write(`i`+"\n")


def testStatistic():
	G = getGraph("../files/G_3.graph")
	#listConv = getListFromFile("../files/conv_obj_all.txt")
	listConv = getListFromFile("../files/conv_obj_all.txt")
	listCom = getListFromFile("../files/list_comment_SVM.txt")
	sum1 = 0
	sum2 = 0
	i=0	
	for lc in listConv["conv"]:
		n1 = lc["count_comment"]
		n2 = listCom["post"][i]["count"]
		#if n1 != n2:
		print i, n1,n2
		sum1 = sum1 + n1
		sum2 = sum2 + n2
		i+=1
	print "sum1:", sum1, "sum2:", sum2
	j=0
	for com in listCom["post"]:
		j+=1
		#print j

def testGraphC():
	G = getGraph("../files/G_3.graph")
	list_conv = {}
	list_conv["conv"] = []
	i = 0
	for NI in G.Nodes():	
		nid = NI.GetId()
		NLabel = G.GetStrAttrDatN(nid, "NLabel")	
		
		#-------------PHOTO
		if NLabel == 'photo':
			NObjectId = G.GetStrAttrDatN(nid, "NObjectId")	
			list_c = []		
			list_c_one = []
			#if i==10502:
			if i>=0:
				print "--------------------------------------",i
				#------------------------------------------------IN EDGES------------------------------------------------
				for nid1 in NI.GetInEdges():
					NLabel1 = G.GetStrAttrDatN(nid1, "NLabel")
					NName1 = G.GetStrAttrDatN(nid1, "NName")
					eid = G.GetEId(nid1,nid)
					ETime = G.GetStrAttrDatE(eid, "ETime")
					#------------COMMENT				
					if NLabel1 == "comment":
						NAuthor_comment = G.GetStrAttrDatN(nid1, "NAuthor")
						NCategory = G.GetStrAttrDatN(nid1, "NCategory")
						NText = G.GetStrAttrDatN(nid1, "NText")						
						#print NName1, NAuthor_comment, ":",NText
						iCom = nid1	
						NI_c = G.GetNI(iCom)
						list_c_one.append({
							"name": NName1,
							"category": NCategory,
							"time": ETime,
							"text": NText
							})
						rr = 0
						for nid_c in NI_c.GetOutEdges():
							NName_subnode = G.GetStrAttrDatN(nid_c, "NName")
							NLabel_subnode = G.GetStrAttrDatN(nid_c, "NLabel")
							eid_c = G.GetEId(nid1,nid_c)
							ELabel_subnode = G.GetStrAttrDatE(eid_c, "ELabel")
							#----------------COMMENT REPLY						
							if ELabel_subnode == "reply" and rr == 0:
								#rr =1
								iSource = nid1
								iTarget = nid_c						
								iEdge = eid_c
								nSource = G.GetStrAttrDatN(iSource, "NName")
								nTarget = G.GetStrAttrDatN(iTarget, "NName")														
								#print "--",nSource, nTarget
								if nSource != nTarget:
									list_c = addConv(list_c, nSource, nTarget)
								textSource = G.GetStrAttrDatN(iSource, "NName")
								textTarget = G.GetStrAttrDatN(iTarget, "NName")
				#list conversation with at least two comments
				list_c = mergeList(list_c)
				#print "List c", list_c
				#for ll in list_c:
				#	print len(ll)
				new_list = getConvObject(list_c, list_c_one)
				all_comments = []
				for n in new_list:
					for nn in n["data"]:
						all_comments.append(nn["name"])
				count_all_comment = len(all_comments)
				#print "all list:", count_all_comment, all_comments

				list_conv["conv"].append({
				"object_id": NObjectId,
				"conversation": new_list,
				"count": len(new_list),
				"count_comment": count_all_comment
				})

			i+=1
	with open('conv_obj_all_c.txt', 'w') as outfile:  
	    json.dump(list_conv, outfile)

if __name__ == '__main__':
	#setConversation()
	#testStatistic()
	testGraphC()
	
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

def setCategorys():
	G = getGraph("../files/G.graph")

	list_post = getListFromFile("../files/list_comment_category_nbsvm_1.txt")
	post_comments = list_post["post"]

	print "post_comments:", len(post_comments)
	i=0
	m=0

	for NI in G.Nodes():	
		nid = NI.GetId()
		NLabel = G.GetStrAttrDatN(nid, "NLabel")	
		
		#-------------PHOTO
		if NLabel == 'photo':			
			c=0
			comments = post_comments[i]["comments"]
			
			#------------------------------------------------IN EDGES------------------------------------------------
			for nid1 in NI.GetInEdges():
				NLabel1 = G.GetStrAttrDatN(nid1, "NLabel")
				NName1 = G.GetStrAttrDatN(nid1, "NName")
				NCategory = G.GetStrAttrDatN(nid1, "NCategory")
				eid = G.GetEId(nid1,nid)
				ETime = G.GetStrAttrDatE(eid, "ETime")
				#------------COMMENT				
				if NLabel1 == "comment":					
					if NCategory == "text":
						G.AddStrAttrDatN(nid1, "other",'NCategory')
					newCategory = comments[c]['category']
					G.AddStrAttrDatN(nid1, newCategory,'NCategory')
					NCategory_1 = G.GetStrAttrDatN(nid1, "NCategory")
					print c,NCategory_1,"--",newCategory
					c+=1
			
			
			print i,"-->",len(comments),"=",c
			i+=1
	#---------------save Graph as an output file
	snap.SaveEdgeList(G, "../files/new_G.txt", "Save as tab-separated list of edges")

	#---------------save binary 
	FOut = snap.TFOut("../files/new_G.graph")
	G.Save(FOut)

def getCommentCategory():
	c_name = ["thank", "congratulation", "agreement", "positive", "invitation", "food", "greeting", "question","hashtag","other"]
	n_cat = [0,0,0,0,0,0,0,0,0,0]
	G = getGraph("../files/new_G.graph")

	for NI in G.Nodes():
		nid = NI.GetId()
		NLabel = G.GetStrAttrDatN(nid, "NLabel")	
		
		#-------------PHOTO
		if NLabel == 'photo':			
			
			#------------------------------------------------IN EDGES------------------------------------------------
			for nid1 in NI.GetInEdges():
				NLabel1 = G.GetStrAttrDatN(nid1, "NLabel")				
				NCategory = G.GetStrAttrDatN(nid1, "NCategory")

				#------------COMMENT				
				if NLabel1 == "comment":
					for i in range(0,10):
						if NCategory == c_name[i]:
							n_cat[i]+=1
	print n_cat

def setComThank():
	G = getGraph("../files/new_G.graph")
	G_2 = G

	i=0
	j=0
	m=0
	for NI in G.Nodes():
		nid = NI.GetId()
		NLabel = G.GetStrAttrDatN(nid, "NLabel")	
		
		#-------------PHOTO
		if NLabel == 'photo':			
			print "----------",m
			m+=1
			prev_c = -1
			#------------------------------------------------IN EDGES------------------------------------------------
			for nid1 in NI.GetInEdges():
				NLabel1 = G.GetStrAttrDatN(nid1, "NLabel")				
				NCategory = G.GetStrAttrDatN(nid1, "NCategory")
				eid1 = G.GetEId(nid1,nid)
				ETime = G.GetStrAttrDatE(eid1, "ETime")
				
				rep = False				
				#------------COMMENT		
				if NLabel1 == "comment":
					iCom = nid1
					print iCom, NCategory
					
					if NCategory == "thank":
						NI_c = G.GetNI(iCom)
						#print "--",i, NI_c.GetOutDeg()

						for nid_c in NI_c.GetInEdges():
							NName_subnode = G.GetStrAttrDatN(nid_c, "NName")
							NLabel_subnode = G.GetStrAttrDatN(nid_c, "NLabel")

							eid_c = G.GetEId(nid_c,nid1)
							ELabel_subnode = G.GetStrAttrDatE(eid_c, "ELabel")

							#----------------COMMENT REPLY						
							if ELabel_subnode == "reply":
								print nid_c, "reply to", nid1
								rep = True
								j+=1
					
						if rep == False and prev_c != -1:
							G_2.AddEdge(iCom, prev_c)
							eid_reply = G_2.GetEId(iCom,prev_c)
							G_2.AddStrAttrDatE(eid_reply, 'reply', 'ELabel')
							G_2.AddStrAttrDatE(eid_reply, ETime, 'ETime')
							j+=1
						i+=1
					prev_c = iCom
					
	print i,j;
	#---------------save Graph as an output file
	snap.SaveEdgeList(G_2, "../files/G_2.txt", "Save as tab-separated list of edges")

	#---------------save binary 
	FOut = snap.TFOut("../files/G_2.graph")
	G_2.Save(FOut)

def newCategoryFromSVM():
	G = getGraph("../files/G_2.graph")

	list_post = getListFromFile("../files/list_comment_SVM.txt")
	post_comments = list_post["post"]

	print "post_comments:", len(post_comments)
	i=0
	m=0

	for NI in G.Nodes():	
		nid = NI.GetId()
		NLabel = G.GetStrAttrDatN(nid, "NLabel")	
		
		#-------------PHOTO
		if NLabel == 'photo':			
			c=0
			comments = post_comments[i]["comments"]
			
			#------------------------------------------------IN EDGES------------------------------------------------
			for nid1 in NI.GetInEdges():
				NLabel1 = G.GetStrAttrDatN(nid1, "NLabel")
				NName1 = G.GetStrAttrDatN(nid1, "NName")
				NCategory = G.GetStrAttrDatN(nid1, "NCategory")
				eid = G.GetEId(nid1,nid)
				ETime = G.GetStrAttrDatE(eid, "ETime")
				#------------COMMENT				
				if NLabel1 == "comment":					
					if NCategory == "text":
						G.AddStrAttrDatN(nid1, "other",'NCategory')
					newCategory = comments[c]['category']					
					NCategory_1 = G.GetStrAttrDatN(nid1, "NCategory")
					print c,NCategory_1,"--",newCategory
					G.AddStrAttrDatN(nid1, newCategory,'NCategory')
					c+=1

			print i,"-->",len(comments),"=",c
			i+=1
	#---------------save Graph as an output file
	snap.SaveEdgeList(G, "../files/G_3.txt", "Save as tab-separated list of edges")

	#---------------save binary 
	FOut = snap.TFOut("../files/G_3.graph")
	G.Save(FOut)

if __name__ == '__main__':
	#setCategorys()
	#getCommentCategory()
	#setComThank()
	newCategoryFromSVM()
	getGraph("../files/G_3.graph")

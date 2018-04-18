import json
import numpy as np

#----------Read Json File
def getListFromFile(filename):
	with open(filename) as data_file:
		listData = json.load(data_file)

	return listData;


def getConvCat():
	list_conv = getListFromFile("../files/conv_obj_all_c.txt")

	categories = ["thank","congratulation","agreement","positive","invitation","food","greeting","hashtag"]

	id_num_conv1 = []
	tot_num_conv1 = []
	id_num_conv2 = []
	tot_num_conv2 = []

	for i in range(0,100):		
		id_num_conv1.append(i)
		tot_num_conv1.append([0,0,0,0,0,0,0,0])
		id_num_conv2.append(i)
		tot_num_conv2.append([0,0,0,0,0,0,0,0])
	
	i = 0	
	for data in list_conv["conv"]:
		n_comment = data["count_comment"]		
		if n_comment>=7 and n_comment<=29:
			for c in data["conversation"]:
				n = len(c["data"])
				for d in c["data"]:
					category = d["category"]
					type_id = categories.index(category)
					tot_num_conv1[n-1][type_id]+=1
		elif n_comment>=30:
			for c in data["conversation"]:
				n = len(c["data"])
				for d in c["data"]:
					category = d["category"]
					type_id = categories.index(category)
					tot_num_conv2[n-1][type_id]+=1
		i+=1
	
	with open('nconv_ncat_7-29.txt', 'w') as outfile:
		json.dump(tot_num_conv1, outfile)

	with open('nconv_ncat_min_30.txt', 'w') as outfile:
		json.dump(tot_num_conv2, outfile)

#1)Mean, Q1, Q2, Q3, Min, Max:
#	-number of comments per photo
#	-number of conversations (with c>=2) per photo
#	-number of comments per conversation
def getStatistics():
	listConv = getListFromFile("../files/conv_obj_all_c.txt")

	id_nconv = []
	count_nconv = []
	list_ncom_ncov = [] #number of frequency for each i number of conversation
	list_member_ncov = []
	for i in range(0,101):		
		id_nconv.append(i)
		count_nconv.append(0)
		list_ncom_ncov.append(0)
		list_member_ncov.append(0)
	
	#outfile1 = open('statistics_1.csv','a')
	list_ncom = [] #number of comments per photo
	list_nconv = [] #number of convervations appear with all comments in a photo with at min conv member = 1
	list_nconv_2 = [] #number of convervations appear with all comments in a photo with at min conv member = 2
	list_ncom_conv = [] #number of comments per all conversations with min conv member = 1

	i = 0
	for lc in listConv["conv"]:
		n_comments = lc["count_comment"]

		if n_comments>0:
			n_conv = lc["count"]
			n_conv_2 = 0
			for d in lc["conversation"]:
				if d["count"]>1:
					n_conv_2 +=1
					list_ncom_conv.append(d["count"])
				ii = d["count"]
				list_ncom_ncov[ii]=list_ncom_ncov[ii]+1
				list_member_ncov[ii] = list_member_ncov[ii] + ii
			
			list_ncom.append(n_comments)
			list_nconv.append(n_conv)			
			list_nconv_2.append(n_conv_2)
			#outfile1.write(`n_comments`+","+`n_conv`+","+`n_conv_2`+"\n")
		i+=1

	print list_ncom_ncov
	print list_member_ncov
	print "SUM member:",sum(list_member_ncov)
	print "MAX:",max(list_ncom),max(list_nconv), max(list_nconv_2), max(list_ncom_conv)
	print "MIN:",min(list_ncom),min(list_nconv), min(list_nconv_2), min(list_ncom_conv)
	mean1 = sum(list_ncom)/float(len(list_ncom))
	mean2 = sum(list_nconv)/float(len(list_nconv))
	mean3 = sum(list_nconv_2)/float(len(list_nconv_2))
	mean4 = sum(list_ncom_conv)/float(len(list_ncom_conv))
	print "MEAN: %.2f, %.2f, %.2f, %.2f" % (mean1, mean2, mean3, mean4)
	q1_1 = np.percentile(list_ncom, 25)
	q1_2 = np.percentile(list_nconv, 25)
	q1_3 = np.percentile(list_nconv_2, 25)
	q1_4 = np.percentile(list_ncom_conv, 25)
	print "Q1:", q1_1, q1_2, q1_3, q1_4
	q2_1 = np.percentile(list_ncom, 50)
	q2_2 = np.percentile(list_nconv, 50)
	q2_3 = np.percentile(list_nconv_2, 50)
	q2_4 = np.percentile(list_ncom_conv, 50)
	print "MEDIAN:", q2_1, q2_2, q2_3, q2_4
	q3_1 = np.percentile(list_ncom, 75)
	q3_2 = np.percentile(list_nconv, 75)
	q3_3 = np.percentile(list_nconv_2, 75)
	q3_4 = np.percentile(list_ncom_conv, 75)
	print "Q3:", q3_1, q3_2, q3_3, q3_4

def finalCategoryResult():
	result_thank = open('files/result_thank','a')
	result_congratulation = open('files/result_congratulation','a')
	result_agreement = open('files/result_agreement','a')
	result_positive = open('files/result_positive','a')
	result_invitation = open('files/result_invitation','a')
	result_food = open('files/result_food','a')
	result_greeting = open('files/result_greeting','a')
	result_question = open('files/result_question','a')
	result_hashtag = open('files/result_hashtag','a')
	result_other = open('files/result_other','a')


	list_conv = getListFromFile("../files/list_comment_category_nbsvm_1.txt")
	i = 0
	for post in list_conv["post"]:
		for com in post["comments"]:
			i+=1
			print i, com["category"]
			cat = com["category"]
			if cat == "thank":
				result_thank.write(com["text"].encode('utf8')+"\n")
			elif cat == "congratulation":
				result_congratulation.write(com["text"].encode('utf8')+"\n")
			elif cat == "agreement":
				result_agreement.write(com["text"].encode('utf8')+"\n")
			elif cat == "positive":
				result_positive.write(com["text"].encode('utf8')+"\n")
			elif cat == "invitation":
				result_invitation.write(com["text"].encode('utf8')+"\n")
			elif cat == "food":
				result_food.write(com["text"].encode('utf8')+"\n")
			elif cat == "greeting":
				result_greeting.write(com["text"].encode('utf8')+"\n")
			elif cat == "question":
				result_question.write(com["text"].encode('utf8')+"\n")
			elif cat == "hashtag":
				result_hashtag.write(com["text"].encode('utf8')+"\n")
			elif cat == "other":
				result_other.write(com["text"].encode('utf8')+"\n")


def getNcomment():
	listConv = getListFromFile("../files/conv_obj_all_c.txt")
	outfile = open('files/ncomment_cov_ID.csv','a')

	i = 0
	for lc in listConv["conv"]:
		i+=1
		n_comments = lc["count_comment"]
		if n_comments>0:
			n_conv = lc["count"]
			n_conv_2 = 0
			max_nc = 0
			for d in lc["conversation"]:
				if d["count"]>max_nc:
					max_nc = d["count"]
				if d["count"]>1:
					n_conv_2 +=1
			outfile.write(`i`+","+`n_comments`+","+`n_conv`+","+`n_conv_2`+","+`max_nc`+"\n")

if __name__ == '__main__':
	#getStatistics()
	getConvCat()
	#finalCategoryResult()
	#getNcomment()
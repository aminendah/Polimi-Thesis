import json
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import metrics
from sklearn import svm
import numpy as np

#----------Read Json File
def getListFromFile(filename):
	with open(filename) as data_file:
		listData = json.load(data_file)
	return listData;


def getTrainingAndTest(filename):
	c_name = ["thank", "congratulation", "agreement", "positive", "invitation", "food", "greeting","hashtag","other"]
	print c_name
	n_cat_t = [0,0,0,0,0,0,0,0,0]
	n_cat_s = [0,0,0,0,0,0,0,0,0]

	dataT = []
	targetT = []
	dataS = []
	targetS = []
	
	list_comment = getListFromFile(filename)

	len_n = 0
	for post in list_comment["post"]:
		for c in post["comments"]:
			len_n+=1
	
	#len_n = len(list_comment["post"])
	len_n = int(round(len_n/2)) #n = 50%
	len_t = int(round(len_n*0.8))
	len_s = int(round(len_n*0.2))
	print len_n, len_t, len_s
	
	j = 0
	idComment = 0
	for post in list_comment["post"]:
		for c in post["comments"]:
			idComment = j
			if j<len_n:
				if j<len_t:
					if c["category"] != "other" and c["category"] != "question":
						dataT.append(c["stemmed_text"])
						targetT.append(c["category"])						
					for i in range(0,9):
						if c["category"] == c_name[i]:												
							n_cat_t[i]+=1
				else:
					if c["category"] != "other" and c["category"] != "question":
						dataS.append(c["stemmed_text"])
						targetS.append(c["category"])						
					for i in range(0,9):
						if c["category"] == c_name[i]:												
							n_cat_s[i]+=1
			j+=1
				

	print n_cat_t, len(dataT)
	print n_cat_s, len(dataS)

	return dataT, targetT, dataS, targetS


def orderData(xt,yt):
	new_xt = []
	new_yt = []

	i = 0	
	for label in yt:
		if label == "thank":			
			new_xt.append(xt[i])
			new_yt.append(yt[i])
		i+=1	
	i = 0	
	for label in yt:
		if label == "congratulation":			
			new_xt.append(xt[i])
			new_yt.append(yt[i])
		i+=1	
	i = 0
	for label in yt:
		if label == "agreement":
			new_xt.append(xt[i])
			new_yt.append(yt[i])
		i+=1
	i = 0
	for label in yt:
		if label == "positive":
			new_xt.append(xt[i])
			new_yt.append(yt[i])			
		i+=1
	i = 0
	for label in yt:
		if label == "invitation":
			new_xt.append(xt[i])
			new_yt.append(yt[i])
		i+=1
	i = 0
	for label in yt:
		if label == "food":
			new_xt.append(xt[i])
			new_yt.append(yt[i])
		i+=1
	i = 0
	for label in yt:
		if label == "greeting":
			new_xt.append(xt[i])
			new_yt.append("greeting")			
		i+=1
	i = 0
	for label in yt:
		if label == "hashtag":
			new_xt.append(xt[i])
			new_yt.append(yt[i])
		i+=1

	return new_xt, new_yt

def limitData(xt,yt,lim):
	new_xt = []
	new_yt = []

	i = 0
	j = 0
	for label in yt:
		if label == "thank" and j<lim:			
			new_xt.append(xt[i])
			new_yt.append(yt[i])
			j+=1
		i+=1	
	i = 0
	j = 0	
	for label in yt:
		if label == "congratulation" and j<lim:			
			new_xt.append(xt[i])
			new_yt.append(yt[i])
			j+=1
		i+=1	
	i = 0
	j = 0
	for label in yt:
		if label == "agreement" and j<lim:
			new_xt.append(xt[i])
			new_yt.append(yt[i])
			j+=1
		i+=1
	i = 0
	j = 0
	for label in yt:
		if label == "positive" and j<lim: 
			new_xt.append(xt[i])
			new_yt.append(yt[i])
			j+=1			
		i+=1
	i = 0
	j = 0
	for label in yt:
		if label == "invitation" and j<lim:
			new_xt.append(xt[i])
			new_yt.append(yt[i])
			j+=1
		i+=1
	i = 0
	j = 0
	for label in yt:
		if label == "food" and j<lim:
			new_xt.append(xt[i])
			new_yt.append(yt[i])
			j+=1
		i+=1
	i = 0
	j = 0
	for label in yt:
		if label == "greeting" and j<lim:
			new_xt.append(xt[i])
			new_yt.append("greeting")
			j+=1			
		i+=1
	i = 0
	j = 0
	for label in yt:
		if label == "hashtag" and j<lim:
			new_xt.append(xt[i])
			new_yt.append(yt[i])
			j+=1
		i+=1

	return new_xt, new_yt

def classificationModel(xt,yt,xs,ys,algorithm):
	c_name_8 = ["agreement","congratulation","food","greeting","hashtag","invitation","positive","thank"]

	if algorithm == 'nb':
		print "\n\n-----------------------NAIVE BAYES--------------------------"
		clf_model = MultinomialNB()
	
	elif algorithm == 'svm':
		print "\n\n-----------------SUPPORT VECTORE MACHINES-------------------"
		#clf_model = SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, random_state=42, max_iter=5, tol=None)
		#clf_model = SGDClassifier(loss='hinge')
		clf_model = svm.LinearSVC() #0.893278668158

	#-----------------------------PIPELINE-----------------------------
	text_clf = Pipeline([('vect', CountVectorizer()),
							('tfidf', TfidfTransformer()),
							('clf', clf_model),
						])
	text_clf.fit(xt, yt)

	#----------------------------EVALUATION---------------------------
	predicted = text_clf.predict(xs)
	print np.mean(predicted == ys)

	#-----------------------detailed performance-----------------------
	cats = c_name_8

	print metrics.classification_report(ys, predicted, target_names=cats)
	print metrics.confusion_matrix(ys, predicted)

	#NB
	#accuracy with 7 classes: 0.790284507392
	#SVM
	#accuracy with 7 classes: 0.760342899739

	return text_clf;

def getTestData(filename):
	list_comment = getListFromFile(filename)
	
	len_n = 0
	for post in list_comment["post"]:
		for c in post["comments"]:
			len_n+=1
	
	len_n = int(round(len_n/2)) #n = 50%

	data = []
	idComment = []
	i = 0
	for post in list_comment["post"]:
		for c in post["comments"]:
			if i<len_n and c["category"] == "other":
				data.append(c["stemmed_text"])
				idComment.append(i)
			if i<len_n and c["category"] == "question":
				data.append(c["stemmed_text"])
				idComment.append(i)
			if i>= len_n:
				data.append(c["stemmed_text"])
				idComment.append(i)
			i+=1

	return data,idComment;

def setNewClass(idComment,predicted):
	filename = "../files/list_comment_kb_2.txt"
	list_comment = getListFromFile(filename)

	name_cat = ["thank", "congratulation", "agreement", "positive", "invitation", "food", "greeting", "question","hashtag","other"]
	n_cat = [0,0,0,0,0,0,0,0,0,0]

	i = 0
	for post in list_comment["post"]:
		for c in post["comments"]:
			print "-----------------------",i
			if i in idComment:
				index = idComment.index(i)
				c["category"] = predicted[index]
			cat = c["category"]
			for ii in range(0,10):
				if name_cat[ii] == cat:
					n_cat[ii]+=1
			i+=1
	print n_cat
	with open('../files/list_comment_SVM.txt', 'w') as outfile:
		json.dump(list_comment, outfile)

def classificationTesting(model, data):
	predicted = model.predict(data)
	
	result_thank = open('result_thank.txt','a')
	result_congratulation = open('result_congratulation.txt','a')
	result_agreement = open('result_agreement.txt','a')
	result_positive = open('result_positive.txt','a')
	result_invitation = open('result_invitation.txt','a')
	result_food = open('result_food.txt','a')
	result_greeting = open('result_greeting.txt','a')
	result_hashtag = open('result_hashtag.txt','a')

	n_cat = [0,0,0,0,0,0,0,0]
	j=0
	for x in predicted:
		if x == "thank":
			n_cat[0]+=1
			result_thank.write(data[j].encode('utf8')+"\n")
		elif x == "congratulation":
			n_cat[1]+=1
			result_congratulation.write(data[j].encode('utf8')+"\n")
		elif x == "agreement":
			n_cat[2]+=1
			result_agreement.write(data[j].encode('utf8')+"\n")
		elif x == "positive":
			n_cat[3]+=1
			result_positive.write(data[j].encode('utf8')+"\n")
		elif x == "invitation":
			n_cat[4]+=1
			result_invitation.write(data[j].encode('utf8')+"\n")
		elif x == "food":
			n_cat[5]+=1
			result_food.write(data[j].encode('utf8')+"\n")
		elif x == "greeting":
			n_cat[6]+=1
			result_greeting.write(data[j].encode('utf8')+"\n")
		elif x == "hashtag":
			n_cat[7]+=1
			result_hashtag.write(data[j].encode('utf8')+"\n")
		j+=1
	print n_cat
	return predicted


def countCategory(filename):
	category_name = ["thank", "congratulation", "agreement", "positive", "invitation", "food", "greeting", "hashtag", "other"]
	list_comment = getListFromFile(filename)
	len_n = 0
	for post in list_comment["post"]:
		for c in post["comments"]:
			len_n+=1
	len_n = int(len_n/2)
	n_cat = [0,0,0,0,0,0,0,0,0]
	i=0
	for post in list_comment["post"]:
		for c in post["comments"]:
			if i<len_n:
				label = c["category"]
				for ii in range(0,9):
					if category_name[ii] == label:
						n_cat[ii]+=1
			i+=1
	print category_name
	print n_cat

if __name__ == '__main__':
	#filename = "../files/list_comment_category_nbsvm_1.txt"
	#filename = "../files/list_comment_category_keywordbased.txt"
	filename = "../files/list_comment_kb_2.txt"
	countCategory(filename)
	xt,yt,xs,ys = getTrainingAndTest(filename)
	xt,yt = orderData(xt,yt)
	xs,ys = orderData(xs,ys)
	#xt,yt = limitData(xt,yt,8000)
	#xs,ys = limitData(xs,ys,2000)
	#modelNB = classificationModel(xt,yt,xs,ys,"nb")
	modelSVM = classificationModel(xt,yt,xs,ys,"svm")
	#all: 0.879653053849
	#500: 0.661473087819
	#1000: 0.740428790199
	#2000: 0.807320151451
	#5000: 0.863892239646
	#10000: 0.871476736345

	data,idComment = getTestData(filename)
	predicted = classificationTesting(modelSVM, data)
	predicted = modelSVM.predict(data)
	#predicted = classificationTesting(modelNB, data)
	#predicted = modelNB.predict(data)

	#setNewClass(idComment,predicted)
	filename = "../files/list_comment_SVM.txt"
	countCategory(filename)
	#[11718, 392, 869, 50855, 2384, 19265, 3969, 8714, 0]
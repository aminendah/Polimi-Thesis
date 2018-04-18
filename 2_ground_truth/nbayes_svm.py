import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
from sklearn import svm
from sklearn import metrics
from pre_processing import *

category_name_8 = ["thank", "congratulation", "agreement", "positive", "invitation", "food", "greeting", "question"]
category_name_5 = ['thank', 'positive', 'invitation', 'food', 'question']

def getTrainingData(n_target):
    print "Perform classification to %d classes" % n_target

    data = []
    target = []
    
    #filename = "../files/list_comment_category_keywordbased.txt"
    filename = "../files/list_comment_category_nbsvm.txt"
    list_comment = getListFromFile(filename)
    
    count_category = []
    for i in range(1,11):       
        count_category.append(0)
    
    i=0
    for post in list_comment["post"]:
        i+=1
        for c in post["comments"]:
            cat_name = c["category"]
            text = c["stemmed_text"]
            #text = c["text"]

            if n_target == 8:
                if cat_name == "thank":
                    data.append(text)
                    target.append(0)
                elif cat_name == "congratulation":
                    data.append(text)
                    target.append(1)
                elif cat_name == "agreement":
                    data.append(text)
                    target.append(2)
                elif cat_name == "positive":
                    data.append(text)
                    target.append(3)
                elif cat_name == "invitation":
                    data.append(text)
                    target.append(4)
                elif cat_name == "food":
                    data.append(text)
                    target.append(5)
                elif cat_name == "greeting":
                    data.append(text)
                    target.append(6)
                elif cat_name == "question":
                    data.append(text)
                    target.append(7)
            else:
                if cat_name == "thank":
                    data.append(text)
                    target.append(0)
                elif cat_name == "congratulation":
                    data.append(text)
                    target.append(1)
                elif cat_name == "agreement":
                    data.append(text)
                    target.append(1)
                elif cat_name == "positive":
                    data.append(text)
                    target.append(1)
                elif cat_name == "greeting":
                    data.append(text)
                    target.append(1)
                elif cat_name == "invitation":
                    data.append(text)
                    target.append(2)
                elif cat_name == "food":
                    data.append(text)
                    target.append(3)
                elif cat_name == "question":
                    data.append(text)
                    target.append(4)
                
    return data, target;

def getTrainingAndTest(X,y,n_class):
    xt = []
    yt = []
    xs = []
    ys = []

    j=0
    for i in X:
        if n_class == 8:  
            #if j<=8000: #10000 #-------------------thank 
            #if j<=400: #500
            #if j<=800: #1000
            #if j<=1600: #2000
            #if j<=4000: #5000
            #if j<=8823: #no limit
            #if j<=8554: #no limit final
            if j<=9070: #no limit final 1
                xt.append(X[j])
                yt.append(y[j])
            #elif j>8823 and j<=10823: #10000
            #elif j>8823 and j<=8154: #500
            #elif j>8823 and j<=8023: #1000
            #elif j>8823 and j<=9223: #2000
            #elif j>8823 and j<=9823: #5000
            #elif j>8823 and j<=11029: #no limit
            #elif j>8554 and j<=10692: #no limit final
            elif j>9070 and j<=11337: #no limit final 1
                xs.append(X[j])
                ys.append(y[j])
            #elif j>11029 and j<=11366: #all #-------------------congratulation
            #elif j>10692 and j<=11012: #all final
            elif j>11337 and j<=11657: #all final 1
                xt.append(X[j])
                yt.append(y[j])
            #elif j>11366 and j<=11450:
            #elif j>11012 and j<=11092: #final
            elif j>11657 and j<=11737: #final 1
                xs.append(X[j])
                ys.append(y[j])
            #elif j>11450 and j<=12027: #>=1000#-------------------agreement
            #elif j>11450 and j<=10738: #500
            #elif j>11092 and j<=11700: #>=1000 final
            elif j>11737 and j<=12345: #>=1000 final 1
                xt.append(X[j])
                yt.append(y[j])
            #elif j>12027 and j<=12171: #>=1000
            #elif j>12027 and j<=11665: #500
            #elif j>11700 and j<=11852: #>=1000 final
            elif j>12345 and j<=12497: #>=1000 final 1
                xs.append(X[j])
                ys.append(y[j])
            #elif j>12171 and j<=20171: #10000 #-------------------positive
            #elif j>12171 and j<=12260: #500
            #elif j>12171 and j<=12971: #1000
            #elif j>12171 and j<=13771: #2000
            #elif j>12171 and j<=16171: #5000
            #elif j>12171 and j<=30245: #no limit
            #elif j>11852 and j<=35148: #no limit final
            elif j>12497 and j<=35793: #no limit final 1
                xt.append(X[j])
                yt.append(y[j])
            #elif j>30245 and j<=32245: #10000
            #elif j>30245 and j<=39106: #500
            #elif j>30245 and j<=30445: #1000
            #elif j>30245 and j<=30645: #2000
            #elif j>30245 and j<=31245: #5000
            #elif j>30245 and j<=34764: #no limit
            #elif j>35148 and j<=40972: #no limit final
            elif j>35793 and j<=41617: #no limit final 1
                xs.append(X[j])
                ys.append(y[j])
            #elif j>34764 and j<=36720: #>=2000 #-------------------invitation
            #elif j>45793 and j<=46193: #>=500
            #elif j>34764 and j<=35564: #>=1000
            #elif j>40972 and j<=42833: #>=2000 final
            elif j>41617 and j<=43478: #>=2000 final 1
                xt.append(X[j])
                yt.append(y[j])
            #elif j>36720 and j<=37209: #>=2000
            #elif j>48239 and j<=48339: #>=500
            #elif j>36720 and j<=36920: #>=1000
            #elif j>42833 and j<=43298: #>=2000 final
            elif j>43478 and j<=43943: #>=2000 final 1
                xs.append(X[j])
                ys.append(y[j])
            #elif j>37209 and j<=45209: #10000 #-------------------food
            #elif j>37209 and j<=49251: #500
            #elif j>37209 and j<=38009: #1000
            #elif j>37209 and j<=38809: #2000
            #elif j>37209 and j<=41209: #5000
            #elif j>37209 and j<=51971: #no limit
            #elif j>43298 and j<=58252: #no limit final
            elif j>43943 and j<=58897: #no limit final 1
                xt.append(X[j])
                yt.append(y[j])
            #elif j>51971 and j<=53971: #10000
            #elif j>51971 and j<=60135: #500
            #elif j>51971 and j<=52171: #1000
            #elif j>51971 and j<=52371: #2000
            #elif j>51971 and j<=52971: #5000
            #elif j>51971 and j<=55661: #no limit
            #elif j>58252 and j<=61990: #no limit final
            elif j>58252 and j<=62635: #no limit final 1
                xs.append(X[j])
                ys.append(y[j])
            #elif j>55661 and j<=62250: #>=10000 #-------------------greeting
            #elif j>55661 and j<=63231: #500
            #elif j>55661 and j<=56461: #1000
            #elif j>55661 and j<=57261: #2000
            #elif j>55661 and j<=59661 : #5000
            #elif j>61990 and j<=67873: #>=10000 final
            elif j>62635 and j<=68558: #>=10000 final 1
                xt.append(X[j])
                yt.append(y[j])
            #elif j>62250 and j<=63897: #>=10000
            #elif j>62250 and j<=67192: #>=500
            #elif j>62250 and j<=62450: #>=1000
            #elif j>62250 and j<=62650: #>=2000
            #elif j>62250 and j<=63250: #>=5000
            #elif j>67873 and j<=69344: #>=10000 final
            elif j>68558 and j<=70039: #>=10000 final 1
                xs.append(X[j])
                ys.append(y[j])
            #elif j>63897 and j<=67275: #>=5000 #-------------------question
            #elif j>63897 and j<=68558: #500
            #elif j>63897 and j<=64697: #1000
            #elif j>63897 and j<=65497: #2000            
            #elif j>69344 and j<=72722: #>=5000 final
            elif j>70039 and j<=73417: #>=5000 final 1
                xt.append(X[j])
                yt.append(y[j])
            #elif j>67275: #>=5000
            #elif j>67275 and j<=71634: #>=500
            #elif j>67275 and j<=67475: #>=1000
            #elif j>67275 and j<=68875: #>=2000
            #elif j>72722: #>=5000 final
            elif j>73417: #>=5000 final 1
                xs.append(X[j])
                ys.append(y[j])

        else:
            #if j<=8000: #10000 -----------------------------#thank
            if j<=8823: #no limit
                xt.append(X[j])
                yt.append(y[j])
            #elif j>8054 and j<=10054: #10000
            elif j>8823 and j<=11029: #no limit
                xs.append(X[j])
                ys.append(y[j])
            #elif j>10068 and j<=18068: #10000 --------------#positive
            elif j>11029 and j<=36606: #no limit
                xt.append(X[j])
                yt.append(y[j])
            #elif j>42909 and j<=44909: #10000
            elif j>36606 and j<=43000: #no limit
                xs.append(X[j])
                ys.append(y[j])
            elif j>43000 and j<=44956: #>=10000 ------------#invitation
                xt.append(X[j])
                yt.append(y[j])
            elif j>44956 and j<=45445: #>=10000
                xs.append(X[j])
                ys.append(y[j])
            #elif j>54178 and j<=62178: #10000---------------#food
            elif j>45445 and j<=60207: #no limit
                xt.append(X[j])
                yt.append(y[j])
            #elif j>65362 and j<=67362: #10000
            elif j>60207 and j<=63897: #no limit
                xs.append(X[j])
                ys.append(y[j])
            elif j>63897 and j<=67275: #>=10000-------------#question
                xt.append(X[j])
                yt.append(y[j])
            elif j>67275 and j<=68119:
                xs.append(X[j])
                ys.append(y[j])
        j+=1
    return xt,yt,xs,ys;


def getNewTestData():
    data = []

    #filename = "../files/list_comment_category_keywordbased.txt"
    filename = "../files/list_comment_category_nbsvm.txt"
    list_comment = getListFromFile(filename)

    i=0
    for post in list_comment["post"]:
        i+=1
        for c in post["comments"]:
            cat_name = c["category"]
            text = c["stemmed_text"]
            #text = c["text"]

            if cat_name == "hashtag" or cat_name == "other":
                data.append(text)
    
    return data;

def classificationModel(xt,yt,xs,ys,n_class,algorithm):
    if algorithm == 'nb':
        print "\n\n-----------------------NAIVE BAYES--------------------------"
        
        clf_model = MultinomialNB()

    elif algorithm == 'svm':
        print "\n\n-----------------SUPPORT VECTORE MACHINES-------------------"
        
        clf_model = SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, random_state=42, max_iter=5, tol=None)
        

	#-----------------------------PIPELINE-----------------------------
    text_clf = Pipeline([('vect', CountVectorizer()),
                            ('tfidf', TfidfTransformer()),
                            ('clf', clf_model),
                        ])

    text_clf.fit(xt, yt)


    #----------------------------EVALUATION---------------------------
    docs_test = xs
    predicted = text_clf.predict(docs_test)    
    print np.mean(predicted == ys)     

    #-----------------------detailed performance-----------------------
    if n_class == 8:
        cats = category_name_8
    else:
        cats = category_name_5
    
    print metrics.classification_report(ys, predicted, target_names=cats)
    print metrics.confusion_matrix(ys, predicted)

    return text_clf;

def classificationTesting(n_class,alg,model,data):
    predicted = model.predict(data)

    print "test data:", len(data)
    print "predicted:", len(predicted)
    
    if n_class == 8 and alg == "nb":
        print "\n\n----------Testing: Naive Bayes (8 classes)-----------------"
        NB_0 = open('NB_0.txt','a')
        #NB_0 = open('NBall_0.txt','a')
        NB_1 = open('NB_1.txt','a')
        NB_2 = open('NB_2.txt','a')
        NB_3 = open('NB_3.txt','a')
        NB_4 = open('NB_4.txt','a')
        NB_5 = open('NB_5.txt','a')
        NB_6 = open('NB_6.txt','a')
        NB_7 = open('NB_7.txt','a')

        ti = [0,0,0,0,0,0,0,0]
        n_cat = [0,0,0,0,0,0,0,0]
        j = 0
        for x in predicted:
            if x == 0:
                n_cat[0]+=1
                ti[0]+=1
                #if ti[0]<=100:
                NB_0.write(data[j].encode('utf8')+"\n")
                print "thank index:",j
            elif x == 1:
                n_cat[1]+=1
                ti[1]+=1
                #if ti[1]<=100:
                NB_1.write(data[j].encode('utf8')+"\n")
            elif x == 2:
                n_cat[2]+=1
                ti[2]+=1
                #if ti[2]<=100:
                NB_2.write(data[j].encode('utf8')+"\n")
            elif x == 3:
                n_cat[3]+=1
                ti[3]+=1
                #if ti[3]<=100:
                NB_3.write(data[j].encode('utf8')+"\n")
            elif x == 4:
                n_cat[4]+=1
                ti[4]+=1
                #if ti[4]<=100:
                NB_4.write(data[j].encode('utf8')+"\n")
            elif x == 5:
                n_cat[5]+=1
                ti[5]+=1
                #if ti[5]<=100:
                NB_5.write(data[j].encode('utf8')+"\n")
            elif x == 6:
                n_cat[6]+=1
                ti[6]+=1
                #if ti[6]<=100:
                NB_6.write(data[j].encode('utf8')+"\n")
                print "greeting index:",j
            elif x == 7:
                n_cat[7]+=1
                ti[7]+=1
                #if ti[7]<=100:
                NB_7.write(data[j].encode('utf8')+"\n")
            j+=1
            
        print n_cat
    elif n_class == 8 and alg == "svm":
        print "\n\n----------Testing: SVM (8 classes)-----------------"
        SVM_0 = open('SVM_0.txt','a')
        SVM_1 = open('SVM_1.txt','a')
        SVM_2 = open('SVM_2.txt','a')
        SVM_3 = open('SVM_3.txt','a')
        SVM_4 = open('SVM_4.txt','a')
        SVM_5 = open('SVM_5.txt','a')
        SVM_6 = open('SVM_6.txt','a')
        SVM_7 = open('SVM_7.txt','a')

        ti = [0,0,0,0,0,0,0,0]
        n_cat = [0,0,0,0,0,0,0,0]
        j = 0
        for x in predicted:
            if x == 0:
                n_cat[0]+=1
                ti[0]+=1
                #if ti[0]<=100:
                SVM_0.write(data[j].encode('utf8')+"\n")
            elif x == 1:
                n_cat[1]+=1
                ti[1]+=1
                #if ti[1]<=100:
                SVM_1.write(data[j].encode('utf8')+"\n")
            elif x == 2:
                n_cat[2]+=1
                ti[2]+=1
                #if ti[2]<=100:
                SVM_2.write(data[j].encode('utf8')+"\n")
            elif x == 3:
                n_cat[3]+=1
                ti[3]+=1
                #if ti[3]<=100:
                SVM_3.write(data[j].encode('utf8')+"\n")
            elif x == 4:
                n_cat[4]+=1
                ti[4]+=1
                #if ti[4]<=100:
                SVM_4.write(data[j].encode('utf8')+"\n")
            elif x == 5:
                n_cat[5]+=1
                ti[5]+=1
                #if ti[5]<=100:
                SVM_5.write(data[j].encode('utf8')+"\n")
            elif x == 6:
                n_cat[6]+=1
                ti[6]+=1
                #if ti[6]<=100:
                SVM_6.write(data[j].encode('utf8')+"\n")                
            elif x == 7:
                n_cat[7]+=1
                ti[7]+=1
                #if ti[7]<=100:
                SVM_7.write(data[j].encode('utf8')+"\n")
            j+=1
            
        print n_cat

    elif n_class == 5 and alg == "nb":
        print "\n\n----------Testing: Naive Bayes (5 classes)-----------------"
        #NB_0 = open('NB5_0.txt','a')
        #NB_1 = open('NB5_1.txt','a')
        #NB_2 = open('NB5_2.txt','a')
        #NB_3 = open('NB5_3.txt','a')
        #NB_4 = open('NB5_4.txt','a')        

        ti = [0,0,0,0,0]
        n_cat = [0,0,0,0,0]
        j = 0
        for x in predicted:
            if x == 0:
                n_cat[0]+=1
                ti[0]+=1
                #if ti[0]<=100:
                #    NB_0.write(data[j].encode('utf8')+"\n")
                #print "index:",j
            elif x == 1:
                n_cat[1]+=1
                ti[1]+=1
                #if ti[1]<=100:
                #    NB_1.write(data[j].encode('utf8')+"\n")
            elif x == 2:
                n_cat[2]+=1
                ti[2]+=1
                #if ti[2]<=100:
                #    NB_2.write(data[j].encode('utf8')+"\n")
            elif x == 3:
                n_cat[3]+=1
                ti[3]+=1
                #if ti[3]<=100:
                #    NB_3.write(data[j].encode('utf8')+"\n")
            elif x == 4:
                n_cat[4]+=1
                ti[4]+=1
                #if ti[4]<=100:
                #    NB_4.write(data[j].encode('utf8')+"\n")            
            j+=1
            
        print n_cat
    
    elif n_class == 5 and alg == "svm":
        print "\n\n----------Testing: SVM (5 classes)-----------------"
        #SVM_0 = open('SVM5_0.txt','a')
        #SVM_1 = open('SVM5_1.txt','a')
        #SVM_2 = open('SVM5_2.txt','a')
        #SVM_3 = open('SVM5_3.txt','a')
        #SVM_4 = open('SVM5_4.txt','a')        

        ti = [0,0,0,0,0]
        n_cat = [0,0,0,0,0]
        j = 0
        for x in predicted:
            if x == 0:
                n_cat[0]+=1
                ti[0]+=1
                #if ti[0]<=100:
                #    SVM_0.write(data[j].encode('utf8')+"\n")
            elif x == 1:
                n_cat[1]+=1
                ti[1]+=1
                #if ti[1]<=100:
                #    SVM_1.write(data[j].encode('utf8')+"\n")
            elif x == 2:
                n_cat[2]+=1
                ti[2]+=1
                #if ti[2]<=100:
                #    SVM_2.write(data[j].encode('utf8')+"\n")
            elif x == 3:
                n_cat[3]+=1
                ti[3]+=1
                #if ti[3]<=100:
                #    SVM_3.write(data[j].encode('utf8')+"\n")
            elif x == 4:
                n_cat[4]+=1
                ti[4]+=1
                #if ti[4]<=100:
                #    SVM_4.write(data[j].encode('utf8')+"\n")
            j+=1
            
        print n_cat

def setNewClass():
    idNewThank = []
    #with open("files/id_new_thank.txt") as f:
    #    for line in f:            
    #        line = int(line.rstrip('\n'))
    #        idNewThank.append(line)
    #print idNewThank
    with open("files/id_thank.txt") as f:
        for line in f:            
            line = int(line.rstrip('\n'))
            idNewThank.append(line)
    print idNewThank

    idNewGreeting = []
    with open("files/id_greeting.txt") as f:
        for line in f:            
            line = int(line.rstrip('\n'))
            idNewGreeting.append(line)
    print idNewGreeting
    
    #filename = "../files/list_comment_category_keywordbased.txt"
    filename = "../files/list_comment_category_nbsvm.txt"
    list_comment = getListFromFile(filename)
    write_new = open('thank_new.txt','a')
    i=0
    j=0
    idC = []
    for post in list_comment["post"]:
        for c in post["comments"]:            
            text = c["text"]
            name = c["category"]
            if name == "hashtag" or name =="other":                
                if i in idNewThank:
                    write_new.write(text.encode('utf8')+"\n")
                    c["category"] = "thank"
                    idC.append(j)
                elif i in idNewGreeting:
                    write_new.write(text.encode('utf8')+"\n")
                    c["category"] = "greeting"
                    idC.append(j)
                i+=1

            j+=1
    print len(idC)
    jj=0
    for post in list_comment["post"]:
        for c in post["comments"]:
            if jj in idC:
                print "cat:",c["category"]
            jj+=1

    with open('../files/list_comment_category_nbsvm_1.txt', 'w') as outfile:
        json.dump(list_comment, outfile)

def getNClassDetail():
    c_name = ["thank", "congratulation", "agreement", "positive", "invitation", "food", "greeting", "question","hashtag","other"]
    n_cat = [0,0,0,0,0,0,0,0,0,0]
    #filename = "../files/list_comment_category_new.txt"
    filename = "../files/list_comment_category_nbsvm_1.txt"
    list_comment = getListFromFile(filename)
    for post in list_comment["post"]:
        for c in post["comments"]:
            for i in range(0,10):
                if c["category"] == c_name[i]:
                    n_cat[i]+=1
    print n_cat

if __name__ == '__main__':
    #getNClassDetail()
    #n_class = 8
    #X,y = getTrainingData(n_class)
    #print "len X: %d, len y: %d " % (len(X), len(y))

    #-------Training Data (xt & yt)
    #xt,yt,xs,ys = getTrainingAndTest(X,y,n_class)

    #print "len xt: %d, len yt: %d " % (len(xt), len(yt))
    #print "len xs: %d, len ys: %d " % (len(xs), len(ys))

    #modelNB = classificationModel(xt,yt,xs,ys,n_class,"nb")
    #modelSVM = classificationModel(xt,yt,xs,ys,n_class,"svm")

    #new_data = getNewTestData()

    #print "\n\n----------Testing: Naive Bayes-----------------"
    #classificationTesting(n_class,"nb",modelNB,new_data)
    #----------Testing: Naive Bayes (8 classes)-----------------
    #[431, 0, 0, 21611, 11, 3756, 11, 25]
    #[217, 0, 3, 16824, 7, 2558, 9, 11]
    #[522, 0, 0, 19100, 6, 4778, 31, 2]
    #----------Testing: Naive Bayes (5 classes)-----------------
    #[272, 21959, 7, 3583, 24]
    #[102, 18846, 2, 673, 6]
    #[170, 20069, 2, 4197, 1]

    #print "\n\n---------------Testing: SVM-------------------"
    #classificationTesting(n_class,"svm",modelSVM,new_data)
    #----------Testing: SVM (8 classes)-----------------
    #[16, 0, 18, 24364, 10, 1403, 32, 2]
    #[1, 0, 0, 19091, 2, 535, 0, 0]
    #[7, 0, 0, 21693, 28, 2639, 37, 35]
    #----------Testing: SVM (5 classes)-----------------
    #[4, 25821, 0, 20, 0, 0, 0, 0]
    #[1, 19628, 0, 0, 0, 0, 0, 0]
    #[0, 24063, 1, 375, 0, 0, 0, 0]

    #Final -1
    #[11237, 461, 807, 28673, 2311, 19148, 7390, 4222, 9336, 14581]
    setNewClass()
    getNClassDetail()
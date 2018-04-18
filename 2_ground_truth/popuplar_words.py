from pre_processing import *

def addWordToList(listWord, word):
	id = -1
	i = 0
	for li in listWord["words"]:
		if li["word"] == word:
			id = i
		i+=1
	if id > -1:
		listWord["words"][id]["count"]+=1
	else:
		listWord["words"].append({
			"word":word,
			"count":1
			})
	return listWord;

def setListWords():
    filename = "../files/all_comment_objects.txt"
    list_comment = getListFromFile(filename)

    list_words = {}
    list_words["words"] = []

    i = 0
    for post in list_comment["post"]:
        i += 1
        print "----------------------------------------------------iteration", i
        for c in post["comments"]:
            text = c["text"]
            isValid = isValidText(text)
            if isValid:
                lang = getLanguage(text)
            else:
                lang = "italian"

            words = getWordsStemmed(text, lang)
            for w in words:
                list_words = addWordToList(list_words, w)

    with open('files/list_words.txt', 'w') as outfile:
        json.dump(list_words, outfile)

    print "n unique words:", len(list_words["words"])


def getPopularWords(max):
    filename = "files/list_words.txt"
    list_words_obj = getListFromFile(filename)

    list_w = []
    list_c = []
    sum = 0
    for word in list_words_obj["words"]:
        list_w.append(word["word"])
        list_c.append(word["count"])
        sum = sum + word["count"]

    print len(list_w)
    print sum

    sorted_w = [x for _,x in sorted(zip(list_c,list_w), reverse=True)]
    sorted_c = sorted(list_c, reverse=True)
    
    output = {}
    output["words"] = []
    
    i = 0
    for w in sorted_w:
        if i<=max:      
            output["words"].append({
                "word":w,
                "count": sorted_c[i]
                })
        i = i + 1

    with open('words_freq.txt', 'w') as outfile:  
        json.dump(output, outfile)
    
if __name__ == '__main__':
    getPopularWords(2000)
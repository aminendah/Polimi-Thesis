import json
from remove_emoji import *
from langdetect import detect
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer


def textRemoveEmoji(text):
	text = text.encode("ascii", "ignore")
	text = remove_emoji(text)
	return text;

def textPretty(text):
	patt = re.compile("(\s*)"+"'"+"(\s*)")
	text = patt.sub('', text)
	text = text.replace("aaaaa", "aa")
	text = text.replace("iiiii", "ii")
	text = text.replace("uuuuu", "uu")
	text = text.replace("ooooo", "oo")
	text = text.replace("eeeee", "ee")
	text = text.replace("aaaa","aa")
	text = text.replace("iiii","ii")
	text = text.replace("uuuu","uu")
	text = text.replace("oooo","oo")
	text = text.replace("eeee","ee")
	text = text.replace("aaa", "aa")
	text = text.replace("iii", "ii")
	text = text.replace("uuu", "uu")
	text = text.replace("ooo", "oo")
	text = text.replace("eee", "ee")
	text = text.replace("aa", "a")
	text = text.replace("ii", "i")
	text = text.replace("uu", "u")

	text = text.lower()

	return text;

def removeUser(text):
	text2 = text
	if "@" in text:
		id = text.index("@")
		if id !=0 and text[id-1] != " ":			
			text2 = text2.replace("@", " @")			
	text = text2
	userM = getUserMentioned(text)
	if len(userM)>0:
		for u in userM:
			patt = re.compile("(\s*)"+"@"+u+"(\s*)")
			text = patt.sub('', text)

	return text;
	
def textClean(text):
	text = textPretty(text)

	text = textRemoveEmoji(text)
	text = text.replace(")","")
	text = text.replace("/","")
	text = text.replace("|","")	
	text = text.replace(",","")
	text = text.replace(";","")
	text = text.replace(":","")
	text = text.replace('"',"")
	text = text.replace("-","")
	text = text.replace("*","")
	text = text.replace("!","")
	text = text.replace("`","")
	text = text.replace("-","")
	text = text.replace("=","")
	text = text.replace("$","")
	text = text.replace("%","")
	text = text.replace("^","")
	text = text.replace("&","")
	text = text.replace("{","")
	text = text.replace("}","")
	text = text.replace("[","")
	text = text.replace("]","")	
	text = filter(None, text)
	text = removeUser(text)
	text = " ".join(text.split())
	return text;

def isValidText(text):
	isValid = False
	
	text = textClean(text)
	
	if text.isspace():
		isValid = False
	elif len(text)<=1:
		isValid = False
	else:
		isValid = True
	if "http" in text and " " not in text:
		isValid = False
	if "#expo" in text and " " not in text:
		isValid = False	
	if "socialmedia@expo2015org" in text:
		isValid = False
	if re.match("^[0-9 !@#%&*<>(^_=-?~]+$", text):
		isValid = False

	#if isValid:
		#print text, len(text)
	return isValid;

def getUserMentioned(text):
	userMentioned = [i[1:] for i in text.split() if i[0]=='@']
	return userMentioned;

def getLanguage(text):
	lang = "it"
	try:
		text = textClean(text)
		lang = detect(text)
		
		l_en = ["beautiful", "morning", "your", "igers", "food", "nice", "yumm", "good",
				"super", "anytime", "happy", "amazing", "thank", "love", "like", "keep",
				"look", "sweet", "sport", "awesome", "cool", "where", "habitat", "tree",
				"welcome", "furniture", "chair", "excellent", "hello", "how", "home",
				"travel", "art", "back", "mood", "jealous", "great"]
		
		l_it = ["ciao", "buon", "issima", "bella", "grazie", "tornata", "auguri", "mia",
				"si", "cucina", "amica", "che", "brava", "cena", "uno", "dolce", "dispiace",
				"nome", "lunga", "caramelle", "curiosa", "cosa", "studiare", "ancora", "voi"]
		for l in l_en:
			if l in text:
				lang = "en"
		for l in l_it:
			if l in text:
				lang = "it"
		if lang != "en" and lang != "it":
			lang = "it"
	except:
		print 'Could not detect language'
	
	if lang == "en":
		lang_l = "english"
	else:
		lang_l = "italian"

	return lang_l;


def getStopWords(lang): 
	stopWords = set(stopwords.words(lang))
	return stopWords;

def getWordsStemmed(text, lang):
	stopWords = getStopWords(lang)

	wordsFiltered = []
	wordsStemmed = []

	isValid = isValidText(text)
	if isValid:
		words = word_tokenize(text)

		for w in words:
			if w not in stopWords:
				wordsFiltered.append(w)

		for w in wordsFiltered:
			stemmer = SnowballStemmer(lang)
			try:
				ws = stemmer.stem(w)
			except:
				ws = w
			wordsStemmed.append(ws)
	else:
		wordsStemmed.append(text)
	return wordsStemmed;

#----------Read Json File
def getListFromFile(filename):
	with open(filename) as data_file:
		listData = json.load(data_file)
	return listData;

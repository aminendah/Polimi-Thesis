from pre_processing import *

category_name = ["thank", "congratulation", "agreement", "positive", "invitation", "food", "greeting","hashtag", "other"]

#----------Category of comments
def getCommentCategory(text):
    category_text = "cat"
    #0
    category_thank = ["grac", "graz", "ringraz", "grrrazzz",
                    "thank", "thnks", "thak", "thanks", "much","tnx",
                    "merci" ]
    #category_thank = ["grac", "graz","thank"]
    #1
    category_congratulation = ["augur", "complean", " felic", " tanti",
                            "congrat"]
    #category_congratulation = ["augur", "complean"," felic", " tanti ","congrat"]
    #2
    category_agreement = ["cert", "concordi", "convenir", "accord", " si ", "esattamente", " vero", 
                        "conferm", "anch'io", "sii", "anche io", "d'accordissimo"
                        "agree", "certain", " ok ", " right", " sure", " yes", "of course", "true",
                        "me too", "yeah"]
    #category_agreement = ["cert", "concordi", "convenir", "accord", " si ", "esattamente", "conferm",
                          #"agree", "certain", " ok ", " right", " sure", " yes", "of course", "true"]
    #3
    category_positive = ["amar", "amor", "bac", "bacion", "bei", "bel", "ben", "bont", "bravissim", 
                        "buon", "carin", "carissm", "compl", "cuor", "dolc", "fantas", "favol", "felic", 
                        "gentil", "grand", "happi", "meravigl", "merce", "miglior", "molt", "onor", "ottim", 
                        "perfett", "piac", "riusc grand", "spettacol", "splendid", "stup", "tesor", "ador",
                        "gioia", "preferit", "geni", "unic", "simpatic", "gosto", "bom dia", "buen",
                        "bom", "forte", "soddisfaz", "prego", "paradis", "megli", "oddio", "divin", "rider",
                        "magia", "bona", "amo", "arte", "valeva", "sognante", "onirica", "boni", "dio",
                        "vorrei", "fata", "unic", "notevole", "sogno", "eccellent", "cara", "meritat",
                        "magna", "buoono", "whoop", "romantic", "viva", "forza", "mamma mia", "capolavor",
                        "perfect", "braavaa","interessant","wee","caro","apprezzi","hope","abaw",
                        "luminos","bone","important","perfeit","maravi","precios","lind","eleganz",
                        "cuti","fatt","fiori","eco","belle","touchant","magnifique","tesoro", "adoro",                        
                        "amaz", "awesom", "beaut", "brav", "cool", "cute", "darling", "dear", "enjoy", 
                        "excellent", "fabulous", "good", "gorgeous", "great", "kind", "like", "lov", 
                        "magnif", "nice", "prett", "spectacul", "super", "sweet", "well", "wonder", "wow", 
                        "interest","favorite", "special", "unique", "brilliant", "best", "big", "satisfa",
                        "better", "welcome", "anytime", "fav", "heaven", "wish", "god", "artist",
                        "laugh", "aha", "hehe", "you too", "magic", "win", "a l o h a", "happy", "worth",
                        "dream", "fan", "merry","christmas", "xmas", "yee", "top", "wow", "woow", "yup",
                        "mmm", "care", "fairy", "remark", "strong", "excellent", "deserve", "masterpiece",
                        "clean", "flawless","lob", "miss", "need", "niccee","jaja","aww","f4f","muah","thumb",
                        "cheer","sexy", "ohh", "ohmamma","coool","yee","tempt","stunn","ahh","heart","mm",
                        "any time","whao","lol","lool","hum","woah","wau","beaitiful","uau","yeeh","ahmaz",
                        "ehe","euu","aww","ooh","epic","bono",
                        "<3", "keren", "kereen", ";)", ":)", ":-)", ":d","(:", ":p",":-d", ":*", ";-)","-)",
                        "xd","xx"]
    #category_positive = ["amar", "amor", "bac", "bacion", "bei", "bel", "ben", "bont", "bravissim",
                         #"buon", "carin", "carissm", "compl", "cuor", "dolc", "fantas", "favol", "felic", 
                         #"gentil", "grand", "happi", "meravigl", "merce", "miglior", "molt", "onor", "ottim", 
                         #"perfett", "piac", "riusc grand", "spettacol", "splendid", "stup", "tesor", "ador",
                         #"gioia", "preferit", "geni", "unic", "simpatic", "gosto", "bom dia", "buen",
                         #"bom", "forte", "soddisfaz", "prego", "paradis", "megli", "oddio", "divin", "rider",
                         #"magia", "bona", "amo", "arte", "valeva", "sognante", "onirica", "boni", "dio",
                         #"vorrei", "fata", "unic", "notevole", "sogno", "eccellent", "cara", "meritat",
                         #"magna", "buoono", "whoop", "romantic", "viva",
                         #"amaz", "awesom", "beaut", "brav", "cool", "cute", "darling", "dear", "enjoy", 
                         #"excellent", "fabulous", "good", "gorgeous", "great", "kind", "like", "lov", 
                         #"magnif", "nice", "prett", "spectacul", "super", "sweet", "well", "wonder", "wow", 
                         #"interest","favorite", "special", "unique",]
    #4
    category_invitation = ["canali", "invit", "pagin", "segui", "sito", "venir",
                            " blog", "check", "clic", "follow", "http", "invite", "link", "mail", "page", 
                            "http",".com ", "likes4likes", "like4like", "likeforfollow", "likeforlike"
                            "likesforlikes", "love4love",
                            " site", "visit", "web", "direct", "bussiness card", "look at", "my bio"]
    #category_invitation = ["canali", "invit", "pagin", "segui", "sito", "venir",
                            #" blog", "check", "clic", "follow", "http", "invite", "link", "mail", "page",
                            #" site", "visit", "web"]
    #5
    category_food = ["acqua", "acquolin", "aperitiv", "appet", "aranc", "assagg", "bevand", "birr", "biscott", 
                    "braciol", "broccol", "bruschett", "caff", "calzon", "cannell", "cappuccin", "capres", "beve",
                    "carne", "carot", "cavol", "cena", "cibo", "ciocco", "colazion", "cottur", "crem", "croccant", 
                    "cucchi", " cucin", "cuoc", "delica", "deliz", "diet", "dolc", "dolci", "espresso", "fagiol", 
                    "fame", "farin", "formagg", "fragol", "fresc", "frig", "fritt", "froll", "frutt", "gluten", 
                    "gnam", "gnocc", "gourmet", "grano", "gust", "hungri", "impast", "lasagn", "latt", "lievit", 
                    "limon", "mangi", "marmell", "mascarpon", "melanz", "mele", "mensa", "merenda", "noc", "nutell", 
                    "nutrit", "olio", "oliv", "pane", "panna", "parmigian", "pasticcer", "peper", "pesc","ghiacci",
                    "pizz", "polpett", "pomodor", "pranz", "pranz", "prosciut", "raviol", "ricett", "ricott", "risott", 
                    "ristor", "salam", "salat", "salato", "salsa", "saltimbocc", "sapor", "spaghet", "spuntin", "squis", 
                    "tiramis", "tonn", "uov", "vanigl", "vegan", "verdur", " vino", "vitamin", "yogurt", "zaffer", 
                    "zuccher", "zupp", "carbonara", "carbo", "perra", "cott", "sfam", "mozzarel", "orto", "panci",
                    "merend", " gelat", "sfoglia", "menta", "piatt", "affamata", "mozarel","composto","sfornat",
                    " bake", "banan", " basil", "beer", "bread", "breakfast", "cake", "calorie", "caramel", "carrot", 
                    "chees", "chef", "chocol", "cinamon", "coffe", "cook", "crisp", "crunch", "cuisin", "dairy", "delici", 
                    "delish", "dessert", "diet", "dinner", "dish", "drink", " eat ", "egg", "feed", "fish", "food", 
                    "fresh", "fried", "fruit", "fry", "fung", "homemade", "ingredient", "jam", "kitchen", "lunch", "meal", 
                    "meat", "muffin", " nom", "nourish", "omellet", "orange", "pancake", "pastr", "pepper", "pudding", 
                    "recip", "restaur", "salad", "salmon", "salt ", "seafood", "snack", "squid", "strawberr", "sugar", 
                    " sweet", "tart", " tast", "tea", "tomato", "tuna", " vanill", "veg", "wine", "yast", "yum", "pastry",
                    "stomach", "pear ", "pears ", "apple", "orange", "avocado", "mint", "yamm", "dish", "cherr", "hungry", "donuts",
                    "tort", "magar","lecker","miam","health"]
    #category_food = ["acqua", "acquolin", "aperitiv", "appet", "aranc", "assagg", "bevand", "birr", "biscott", 
                    #"braciol", "broccol", "bruschett", "caff", "calzon", "cannell", "cappuccin", "capres", "beve",
                    #"carne", "carot", "cavol", "cena", "cibo", "ciocco", "colazion", "cottur", "crem", "croccant", 
                    #"cucchi", " cucin", "cuoc", "delica", "deliz", "diet", "dolc", "dolci", "espresso", "fagiol", 
                    #"fame", "farin", "formagg", "fragol", "fresc", "frig", "fritt", "froll", "frutt", "gluten", 
                    #"gnam", "gnocc", "gourmet", "grano", "gust", "hungri", "impast", "lasagn", "latt", "lievit", 
                    #"limon", "mangi", "marmell", "mascarpon", "melanz", "mele", "mensa", "merenda", "noc", "nutell", 
                    #"nutrit", "olio", "oliv", "pane", "panna", "parmigian", "pasticcer", "peper", "pesc","ghiacci",
                    #"pizz", "polpett", "pomodor", "pranz", "pranz", "prosciut", "raviol", "ricett", "ricott", "risott", 
                    #"ristor", "salam", "salat", "salato", "salsa", "saltimbocc", "sapor", "spaghet", "spuntin", "squis", 
                    #"tiramis", "tonn", "uov", "vanigl", "vegan", "verdur", " vino", "vitamin", "yogurt", "zaffer", 
                    #"zuccher", "zupp",
                    #" bake", "banan", " basil", "beer", "bread", "breakfast", "cake", "calorie", "caramel", "carrot", 
                    #"chees", "chef", "chocol", "cinamon", "coffe", "cook", "crisp", "crunch", "cuisin", "dairy", "delici", 
                    #"delish", "dessert", "diet", "dinner", "dish", "drink", " eat ", "egg", "feed", "fish", "food", 
                    #"fresh", "fried", "fruit", "fry", "fung", "homemade", "ingredient", "jam", "kitchen", "lunch", "meal", 
                    #"meat", "muffin", " nom", "nourish", "omellet", "orange", "pancake", "pastr", "pepper", "pudding", 
                    #"recip", "restaur", "salad", "salmon", "salt ", "seafood", "snack", "squid", "strawberr", "sugar", 
                    #" sweet", "tart", " tast", "tea", "tomato", "tuna", " vanill", "veg", "wine"]
    #6
    category_greeting = ["arriv", "buon", "sera", "buongiorn", "ciao", "giorn", "mattin", "nott", 
                        "salv","buonjiorn","ciaio", "moin", 
                        "hey", "morning", "night", "morning", "afternoon", "hello", "good",
                        "bonjour", "hola", "coucou", "bonne", "bounjour","ohayo", "bonsoir"]
    #category_greeting = ["arriv", "buon", "sera", "buongiorn", "ciao", "giorn", "mattin", "nott",
                        #"salv",
                        #"hey", "morning", "night", "morning", "afternoon", "hello", "good"]


    category = []
    category.append({"name": "thank", "keywords": category_thank, "count":[]})
    category.append({"name": "congratulation", "keywords": category_congratulation, "count":[]})
    category.append({"name": "agreement", "keywords": category_agreement, "count":[]})
    category.append({"name": "positive", "keywords": category_positive, "count":[]})
    category.append({"name": "invitation", "keywords": category_invitation, "count":[]})
    category.append({"name": "food", "keywords": category_food, "count":[]})
    category.append({"name": "greeting", "keywords": category_greeting, "count":[]})

    
    
    i = 0
    score_category = []
    for cat in category:
        for word in cat["keywords"]:
            count = text.count(word)            
            cat["count"].append(count)
        score_category.append(sum(cat["count"]))
    score_category[3]=0.5*score_category[3]
    
    score_category.append(0)
    score_category.append(0.0001)
    word_token = word_tokenize(text)
    for w in word_token:
        if len(w)>0 and w[0] == "#":
            score_category[7] += 0.001
    #print score_category
    
    rank = [x for _,x in sorted(zip(score_category,category_name), reverse=True)]
    
    category_text = rank[0]
    
    return category_text;

def setCommentCategory():
    filename = "../files/list_comment.txt"
    list_comment = getListFromFile(filename)
    
    len_n = 0
    for post in list_comment["post"]:
        for c in post["comments"]:
            len_n+=1
    
    len_n = int(round(len_n/2)) #n = 50%


    i=0
    for post in list_comment["post"]:
        for c in post["comments"]:
            if i<len_n:
                #print "-----",i
                text = c["text"]
                text = textPretty(text)
                category_name = getCommentCategory(text)
                c["category"] = category_name
            i+=1

    with open('../files/list_comment_kb_2.txt', 'w') as outfile:
        json.dump(list_comment, outfile)

def saveCommentCategory():
	thank_txt = open('files/category_set/thank.txt','a')
	congratulation_txt = open('files/category_set/congratulation.txt','a')
	agreement_txt = open('files/category_set/agreement.txt','a')
	positive_txt = open('files/category_set/positive.txt','a')
	invitation_txt = open('files/category_set/invitation.txt','a')
	food_txt = open('files/category_set/food.txt','a')
	greeting_txt = open('files/category_set/greeting.txt','a')
	question_txt = open('files/category_set/question.txt','a')
	hashtag_txt = open('files/category_set/hashtag.txt','a')
	other_txt = open('files/category_set/other.txt','a')

	filename = "../files/list_comment_category_keywordbased.txt"
	list_comment = getListFromFile(filename)
	
	count_category = []
	for i in range(1,11):		
		count_category.append(0)
	
	i=0
	for post in list_comment["post"]:
		i+=1
		for c in post["comments"]:
			cat_name = c["category"]
			text = c["text"]

			if cat_name == "thank":
				thank_txt.write(text.encode('utf8')+"\n")
			elif cat_name == "congratulation":
				congratulation_txt.write(text.encode('utf8')+"\n")
			elif cat_name == "agreement":
				agreement_txt.write(text.encode('utf8')+"\n")
			elif cat_name == "positive":
				positive_txt.write(text.encode('utf8')+"\n")
			elif cat_name == "invitation":
				invitation_txt.write(text.encode('utf8')+"\n")
			elif cat_name == "food":
				food_txt.write(text.encode('utf8')+"\n")
			elif cat_name == "greeting":
				greeting_txt.write(text.encode('utf8')+"\n")
			elif cat_name == "question":
				question_txt.write(text.encode('utf8')+"\n")
			elif cat_name == "hashtag":
				hashtag_txt.write(text.encode('utf8')+"\n")
			elif cat_name == "other":
				other_txt.write(text.encode('utf8')+"\n")

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
    setCommentCategory()
    filename = "../files/list_comment_kb_2.txt"
    countCategory(filename)
	#filename = "../files/list_comment_category_keywordbased.txt"
	#list_comment = getListFromFile(filename)
#	
	#count_category = []
	#for i in range(1,11):		
		#count_category.append(0)
#	
	#i=0
	#for post in list_comment["post"]:
		#i+=1		
		#for c in post["comments"]:
			#cat_name = c["category"]
			#for name in category_name:
				#if cat_name == name:
					#count_category[(category_name.index(name))]+=1
#
	#print count_category
    
    #removing user in comment
	#result 0:[10817, 389, 1296, 27279, 2963, 15120, 4869, 4221, 10452, 20760]
	#result 1:[10679, 374, 1629, 28729, 3512, 14608, 6055, 4221, 9258, 19101]
	#result 2:[10679, 372, 1628, 28763, 3510, 14603, 6053, 4221, 9255, 19082]
	#result 3:[10260, 343, 1441, 32893, 3109, 13884, 5562, 4221, 8933, 17520]
	#result 4:[10073, 321, 1400, 33744, 3066, 14035, 5340, 4221, 8699, 17267]
	#result 5:[10068, 321, 1471, 33933, 3058, 13980, 5327, 4221, 8680, 17107]
	#result 6:[10084, 323, 1480, 33910, 3044, 13938, 5321, 4221, 8680, 17165]
    #including user in comment + human-in-loop from NB and SVM
    #result 7:[9247, 285, 5421, 33817, 3352, 15547, 5536, 4222, 7323, 13416]
    #result 8:[8838, 270, 5077, 37362, 3100, 14489, 5179, 4222, 7090, 12539]
    #final:
    #result 9:[8940, 270, 5077, 37362, 3100, 14489, 5179, 4222, 7089, 12438]

    #result 10:[10426, 431, 2163, 25769, 5386, 20766, 6746, 4222, 8685, 13572]
    #result 11:[10463, 432, 1462, 26061, 5420, 20826, 6759, 4222, 8698, 13823]
    #result 12:[10602, 449, 1069, 27698, 3774, 19611, 7246, 4222, 8867, 14628]
    #result 13:[10603, 449, 996, 27708, 3774, 19612, 7247, 4222, 8870, 14685]
    #[10603, 449, 953, 27714, 3774, 19612, 7247, 4222, 8894, 14698]
    #[10603, 449, 902, 27716, 3774, 19612, 7247, 4222, 8941, 14700]
    #[10714, 461, 807, 28647, 2366, 19129, 7389, 4222, 9351, 15080]
    #[10715, 461, 807, 28673, 2311, 19148, 7390, 4222, 9351, 15088]


    #initial:
    #[10958, 519, 734, 22172, 2439, 18982, 8217, 4222, 10439, 19484]
    #[11029, 421, 721, 22593, 2445, 18452, 8236, 4222, 10478, 19569] -- use this
    #[10692, 400, 760, 29120, 2326, 18692, 7354, 4222, 9427, 15173] -- final keyword based
    #[11337, 400, 760, 29120, 2326, 18692, 7404, 4222, 9391, 14514] -- final SVM 
    #[11409, 400, 760, 29120, 2326, 18692, 7410, 4222, 9387, 14440] -- final SVM 1
	
	#saveCommentCategory()
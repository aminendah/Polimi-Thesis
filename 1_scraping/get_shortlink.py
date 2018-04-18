from functions import *

list_shortlink = {}
list_shortlink['post']=[]

#to connect mongoDB
db = connectDB()
posts = db.newPhotos

cursor = posts.find(no_cursor_timeout=True)
i = 0
for data in cursor:
	i+=1
	print i
	object_id = str(data['_id'])
	url = data['raw']['link']
	shortlink = data['shortLink']
	list_shortlink['post'].append({
		'id' : object_id,
		'url' : url,
		'shortlink' : shortlink
		})
with open('files/list_shortlink.txt', 'w') as outfile:
    json.dump(list_shortlink, outfile)
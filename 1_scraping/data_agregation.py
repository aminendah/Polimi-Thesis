from functions import *

#----------read files
file_1 = "files/post_comment_part_1.txt"
file_2 = "files/post_comment_part_2.txt"
file_3 = "files/post_comment_part_3.txt"

list_1 = getListFromFile(file_1)
list_2 = getListFromFile(file_2)
list_3 = getListFromFile(file_3)

#----------to keep list objet_id only
list_object_id = []
#----------save into list object
list_scraping = []
for l in list_1:
	object_id = l["object_id"]
	list_object_id.append(object_id)
	list_scraping.append(l)

for l in list_2:
	object_id = l["object_id"]
	list_object_id.append(object_id)
	list_scraping.append(l)

for l in list_3:
	object_id = l["object_id"]
	list_object_id.append(object_id)
	list_scraping.append(l)

list_allcomment = {}
list_allcomment["post"] = []


list_only_comment = {}
list_only_comment["comment"] = []

list_newphoto = []

#to connect mongoDB
db = connectDB()
posts = db.newPhotos

cursor = posts.find(no_cursor_timeout=True)
#----------comment id
id_c = 0
i = 0
n = 0
for data in cursor:
	i+=1
	object_id = str(data['_id'])
	if object_id in list_object_id:
		index = list_object_id.index(object_id)
		print i, object_id, "is in", index
		raw_comment = list_scraping[index]
		comments = []
		for data in raw_comment["comments"]:
			id_c += 1
			com = {
				"id": id_c,
				"from":{
						"full_name": None,
						"id": data["node"]["owner"]["id"],
						"profile_picture": data["node"]["owner"]["profile_pic_url"],
						"username": data["node"]["owner"]["username"],
					},
				"text": data["node"]["text"],
				"created_time": data["node"]["created_at"]
				}

			comments.append(com)
			list_only_comment["comment"].append(com)
		list_allcomment["post"].append({
			"object_id": object_id,
			"comments": comments,
			"count": len(comments)
			})
	else:
		comments = []
		for com in data["raw"]["comments"]["data"]:
			id_c += 1
			com["id"] = id_c
			comments.append(com)
			list_only_comment["comment"].append(com)

		list_allcomment["post"].append({
			"object_id": object_id,
			"comments": comments,
			"count": len(comments)
			})
		print i, object_id, "is not found"


with open('all_comment_objects.txt', 'w') as outfile:
    json.dump(list_allcomment, outfile)
with open('all_comments.txt', 'w') as outfile:
    json.dump(list_only_comment, outfile)
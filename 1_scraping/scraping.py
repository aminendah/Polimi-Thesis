#!/usr/bin/python

from functions import *
import pickle


filename = "files/list_shortlink.txt"
list_shortlink = getListFromFile(filename)

#to take variabel index for starting iteration
fp = open("files/shared.pkl")
shared = pickle.load(fp)
ind = shared["index"]

maxcomment = 500
i = ind
n = 0

#open 3 file each consists 5000 data
tmp1 = open('post_comment_part_1.txt','a')
tmp2 = open('post_comment_part_2.txt','a')
tmp3 = open('post_comment_part_3.txt','a')

#looping from index to ind
for l in list_shortlink['post'][ind:]:
	i += 1
	object_id = l['id']
	url = l['url']
	shortlink = l['shortlink']
	url_status = checkUrl(url)

	if url_status:
		comments = getPostAllComment(str(maxcomment),shortlink)
		#print result to file
		if i/5000 == 0:
			tmp1.write(',{"object_id":"'+object_id+'","comments":'+json.dumps(comments)+'}')
		elif i/5000 == 1:
			tmp2.write(',{"object_id":"'+object_id+'","comments":'+json.dumps(comments)+'}')
		else:
			tmp3.write(',{"object_id":"'+object_id+'","comments":'+json.dumps(comments)+'}')
		n += 1

	print '[from ',ind,'][',i,']', object_id, url_status, n
	#to write variabel index each successful requested data
	shared1 = {"index":i}
	fp1 = open("shared.pkl","w")
	pickle.dump(shared1, fp1)

tmp1.close()
tmp2.close()
tmp3.close()
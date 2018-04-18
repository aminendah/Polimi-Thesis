import geocoder
import json
import snap
import time
import sys
from pymongo import MongoClient
from bson.objectid import ObjectId

default = None

#----------Read Json File
def getListFromFile(filename):
	with open(filename) as data_file:
		listData = json.load(data_file)

	return listData;

#----------MongoDB Connection--------------------------------------
def connectDB():
   client = MongoClient('localhost', 27017)
   db = client.YourExpo2015
   print "MongoDB is connected"
   return db;

#----------User Domain---------------------------------------------	
def addUserList(userList, id, username, fullname=default, profilePicture=default):
	userList['user'].append({  
			'id': id,
			'username': username,
			'fullname': fullname,
			'profilePicture': profilePicture
		})
	return userList;
	
def isUniqueUser(userList, username):
	unique = True
	for data in userList['user']:
		u = data['username']
		if u == username:
			unique = False
			break;
	return unique;

def getUserId(userList, username):
	id = 0
	#username = username.encode('unicode_escape')
	for data in userList['user']:
		if data['username'] == username:
			id = data['id']
			break;
	return id;

#----------Challenge Domain----------------------------------------
def isUniqueChallenge(challengeList, name):
	unique = True
	for data in challengeList['challenge']:
		if data['name'] == name:
			unique = False
			break;
	return unique

def getChallengeId(challengeList, name):
	id = 0
	for data in challengeList['challenge']:
		if data['name'] == name:
			id = data['id']
			break;
	return id;
	
def addChallengeList(challengeList, id, name):
	challengeList['challenge'].append({
		'id': id,
		'name': name
	})
	return challengeList;

#----------Comment Domain------------------------------------------
def addTempCommentList(tempCommentList, id, text, creationTime, fromUser):
	tempCommentList['comment'].append({
		'id': id,
		'text': text,
		'creationTime': creationTime,
		'fromUser': fromUser
	})
	return tempCommentList;

def getCommentIdFromSender(tempCommentList, fromUser):
	id = 0
	for data in tempCommentList['comment']:
		if data['fromUser'] == fromUser:
			id = data['id']
	return id;

def getHashtagAndUser(text):
	text = text.encode('utf-8')

	hashtags = [i[1:] for i in text.split() if i[0]=='#']
	userMentioned = [i[1:] for i in text.split() if i[0]=='@']

	for h in hashtags:
		bh = h.split('@')
		if len(bh)>1:			
			userMentioned.append(bh[1])
			hashtags.remove(h)
			h = bh[0]

		ah = h.split('#')
		
		if len(ah)>1:
			for i in ah:
				hashtags.append(i)
			if h in hashtags:
				hashtags.remove(h)

	return hashtags, userMentioned;

#----------Hashtag Domain---------------------------------------------
def isUniqueHashtag(hashtagList, hashtag):
	unique = True
	for data in hashtagList['hashtag']:
		if data['value'] == hashtag:
			unique = False
			break;
	return unique;

def getHashtagId(hashtagList, hashtag):
	id = 0
	for data in hashtagList['hashtag']:
		if data['value'] == hashtag:
			id = data['id']
			break;
	return id;
	
def addHashtag(hashtagList, id, hashtag):
	hashtagList['hashtag'].append({
					'id': id,
					'value': hashtag
				})
	return hashtagList;

#----------Location Domain------------------------------------------
def isUniqueLocation(locationList, city):
	unique = True
	for data in locationList['location']:
		if data['city'] == city:
			unique = False
			break;
	return unique;

def getLocationId(locationList, city):
	id = 0
	for data in locationList['location']:
		if data['city'] == city:
			id = data['id']
			break;
	return id;
	
def addLocation(locationList, id, city, country):
	locationList['location'].append({
		'id': id,
		'city': city,
		'country': country
	})	
	return locationList;
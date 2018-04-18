import urllib2
import json
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from requests.exceptions import HTTPError


# ----------MongoDB Connection--------------------------------------
def connectDB():
    client = MongoClient('localhost', 27017)
    db = client.YourExpo2015
    print "MongoDB is connected"
    return db;

def checkUrl(url):
    status = True
    try:
        r = requests.get(url)
        r.raise_for_status()
    except HTTPError:
        print 'Could not download page'
        status = False
    return status;

def getPostAllComment(numcomments, shortcode):
    url = 'https://www.instagram.com/graphql/query/?query_id=17852405266163336&variables={"shortcode":"' + shortcode + '","first":' + str(
        numcomments) + '}'

    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    data = json.loads(str(soup))

    comments = data["data"]['shortcode_media']['edge_media_to_comment']['edges']
    return comments;

# ----------Read Json File
def getListFromFile(filename):
    with open(filename) as data_file:
        listData = json.load(data_file)

    return listData;
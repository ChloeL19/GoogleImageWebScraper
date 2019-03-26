#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 17:59:07 2019

@author: chloeloughridge
"""

import requests
import argparse
import os
from bs4 import BeautifulSoup
import requests
import re
import urllib.request as urllib2
import http.cookiejar as cookielib
import json

def get_soup(url,header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'html.parser')

ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=True,
	help="path to output directory of images")
args = vars(ap.parse_args())

query = "hemlock" # you can change the query for the image  here
image_type="jpg"
query= query.split()
query='+'.join(query)
url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
print (url)
#add the directory for your image here
DIR="Pictures"
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
}
soup = get_soup(url,header)


ActualImages=[]# contains the link for Large original images, type of  image
for a in soup.find_all("div",{"class":"rg_meta"}):
    link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
    ActualImages.append((link,Type))

print  ("there are total" , len(ActualImages),"images")

if not os.path.exists(DIR):
            os.mkdir(DIR)
DIR = os.path.join(DIR, query.split()[0])

if not os.path.exists(DIR):
            os.mkdir(DIR)
            
###print images
count = 0
for i , (img , Type) in enumerate( ActualImages):
# grab the list of URLs from the input file, then initialize the
# total number of images downloaded thus far
    url = img
    #rows = open(args["urls"]).read().strip().split("\n")
    #total = 0

    #url = "https://giant.dexecure.net/assets/easyimage/1/11c1c6becdeadb232f8615e4b76746e7.jpg"
    response = requests.get(url)
    if response.status_code == 200:
        with open(query + str(count) + ".jpg", 'wb') as f:
            f.write(response.content)
    count += 1
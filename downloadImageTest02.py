#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 17:59:07 2019

@author: chloeloughridge
"""

import requests
import argparse
import os


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-u", "--urls", required=True,
	help="path to file containing image URLs")
ap.add_argument("-o", "--output", required=True,
	help="path to output directory of images")
args = vars(ap.parse_args())
 
# grab the list of URLs from the input file, then initialize the
# total number of images downloaded thus far
rows = open(args["urls"]).read().strip().split("\n")
total = 0

# loop the URLs
count = 0
for url in rows:

    #url = "https://giant.dexecure.net/assets/easyimage/1/11c1c6becdeadb232f8615e4b76746e7.jpg"
    response = requests.get(url)
    if response.status_code == 200:
        with open(str(count) + ".jpg", 'wb') as f:
            f.write(response.content)
    count += 1
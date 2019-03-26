#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 17:59:07 2019

@author: chloeloughridge
"""

import requests

url = "https://giant.dexecure.net/assets/easyimage/1/11c1c6becdeadb232f8615e4b76746e7.jpg"
response = requests.get(url)
if response.status_code == 200:
    with open("./sample.jpg", 'wb') as f:
        f.write(response.content)
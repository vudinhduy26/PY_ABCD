# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 22:14:33 2021

@author: duy
"""

import nltk
#nltk.dowload('popular')
from urllib import request
#url = 'http://www.gutenberg.org/files/2554/2554-0.txt'
#response = request.urlopen(url)
#raw = response.read().decode('utf8')
from bs4 import BeautifulSoup
url = 'http://news.bbc.co.uk/2/hi/health/2284781.stm'
html = request.urlopen(url).read().decode('utf8')
raw = BeautifulSoup(html,'html.parser').get_text()
tokens = nltk.word_tokenize(raw)
words = tokens[:12]
count = {}
for i in words :
    if i in count:
        count[i] +=1
    else:
        count[i]=1
for j in sorted(count, key=count.get,reverse=False): #ham sap xep trong tu dien
    print(j,":",count[j])


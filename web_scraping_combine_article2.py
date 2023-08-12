# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 09:48:31 2023

@author: ATISHKUMAR
"""

import pandas as pd
import numpy as np
import os
import bs4 as bs
import urllib.request #to read all urls
import re
import spacy
import re,string,unicodedata
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
lem=WordNetLemmatizer()

os.chdir(r'D:\Naresh_it_praksah_senapathi\august\web_scrapping\xml_many articles')

from glob import glob
path=r'D:\Naresh_it_praksah_senapathi\august\web_scrapping\xml_many articles'
all_files=glob(os.path.join(path, "*.xml"))


import xml.etree.ElementTree as ET#it will show xml file as tree format

dfs=[]
for filename in all_files:
    tree=ET.parse(filename)
    root=tree.getroot()
    root=ET.tostring(root,encoding='utf8').decode('utf8')
    dfs.append(root)
    
dfs[0]

#######

import bs4 as bs
import urllib.request
import re

parsed_article=bs.BeautifulSoup(dfs[0],'xml')

paragraphs=parsed_article.find_all('p')


article_text_full=""

for p in paragraphs:
    article_text_full+=p.text
    print(p.text)
    
def data_preprocessing(each_file):
    parsed_article=bs.BeautifulSoup(each_file,"xml")
    
    paragraphs=parsed_article.find_all('para')
    
    article_text_full=""
    for p in paragraphs:
        article_text_full+=p.text
        print(p.text)
    return article_text_full

data=[data_preprocessing(each_file)for each_file in dfs]
    
#######################this here combined all article ################################

#after we gonna see how to cleaned each article
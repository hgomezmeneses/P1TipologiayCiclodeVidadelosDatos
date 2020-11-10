#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import os
from bs4 import BeautifulSoup
import re
import pandas as pd
import urllib.request

os.mkdir('Album_Pictures')
j=0
for i in range(51):
    page = requests.get("https://www.besteveralbums.com/overall.php?o=&f=&fv=&orderby=-InfoRankScore&sortdir=asc&page=" + str(1))
    soup = BeautifulSoup(page.content, 'html.parser')
    pictures = soup.find_all('picture')
    for picture in pictures:
        url = 'https://www.besteveralbums.com/' + picture.source.get('data-srcset')
        path = 'Album_Pictures/album' + str(j) +'.jpg' 
        urllib.request.urlretrieve(url, path)
        j = j+1


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import os
from bs4 import BeautifulSoup
import re
import pandas as pd
import urllib.request
#Creamos el directorio
os.mkdir('Album_Pictures')
j=0
#Para cada página web, cada cual contiene diez álbumes
for i in range(51):
    # Cargamos el contenido
    page = requests.get("https://www.besteveralbums.com/overall.php?o=&f=&fv=&orderby=-InfoRankScore&sortdir=asc&page=" + str(1))
    soup = BeautifulSoup(page.content, 'html.parser')
    # Filtramos todas las imágenes
    pictures = soup.find_all('picture')
    # Descargamos las imágenes y las guardamos en el directorio creado
    for picture in pictures:
        url = 'https://www.besteveralbums.com/' + picture.source.get('data-srcset')
        path = 'Album_Pictures/album' + str(j) +'.jpg' 
        urllib.request.urlretrieve(url, path)
        j = j+1


# In[ ]:





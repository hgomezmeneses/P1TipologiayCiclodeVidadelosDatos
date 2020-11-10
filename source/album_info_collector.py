#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

#Creamos las listas donde almacenaremos toda nuestra información:
ranking_list = []
albums_list = []
bands_list = []
release_list = []
album_score = []

for i in range(51):
    #Cargamos las diversas paginas web, una a una
    page = requests.get("https://www.besteveralbums.com/overall.php?o=&f=&fv=&orderby=-InfoRankScore&sortdir=asc&page=" + str(i))
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # Guardamos la clasificacion de los albumes en el ranking
    albums_ranking = soup.find_all('span',class_= 'bigger')
    for album in albums_ranking:
        ranking_list.append(album.b.text)
        
    # Guardamos el nombre de los albumes  
    albums_name = soup.find_all('div',class_='chartstring chart-title-col')
    for album in albums_name:
        albums_list.append(album.a.text)
        
    # Guardamos los nombres de las bandas   
    bands_name = soup.find_all('div',class_='chart-title-col chartstring')
    for band in bands_name:
        bands_list.append(band.a.text)
        
    # Guardamos los años en que salieron los albumes
    metrics = soup.find_all('div',class_='chart-stats-metric')
    j = 0;
    for i in range(int(len(metrics)/8)):
        release_list.append(metrics[j].text)
        j = j + 8
        
    # Guardamos la puntuación del álbum
    metrics = soup.find_all('div',class_='chart-stats-metric')
    j = 6;
    for i in range(int(len(metrics)/8)):
        album_score.append(metrics[j].a.text)
        j = j + 8
    
    
#Limpiamos, lo poco que se puede, los datos obtenidos y los pasamos a un dataframe:

ranking_list = [re.sub(r'\.','', x) for x in ranking_list]
album_score = [x[0:2] for x in album_score]
albumsdf = pd.DataFrame({'Position': ranking_list,
                         'Score': album_score,
                        'Album': albums_list,
                        'Band': bands_list,
                        'Release Year': release_list,})
albumsdf.to_csv('albums_info.csv')
albumsdf


# In[ ]:





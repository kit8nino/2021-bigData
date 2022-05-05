import json
from bs4 import BeautifulSoup
import requests
import pandas as pd

"""
data = pd.read_csv('../_lab-4/movies_metadata.csv', header=0)

data['link'] = 'https://www.imdb.com/title/' + data['imdb_id'] + '/'

print(data.head())
data.to_csv('imdb_movies.csv')
"""
path = './movies_posters/'
data = pd.read_csv('../_lab-4/imdb_movies.csv', header=0, 
        usecols=['id', 'genres', 'title', 'popularity', 'release_date', 'vote_average', 'vote_count', 'link'],
        dtype=object, parse_dates=True)

for links, ids in zip(data['link'].tolist(), data['id'].tolist()):
    r = requests.get(links)
    #print('Connected!' if r.status_code==200 else 'Fail.')
    soup = BeautifulSoup(r.text, 'html.parser')
    im = requests.get(soup.find(class_='ipc-image').get('src'))
    with open(path+ids+'.jpg', 'wb') as w:
        w.write(im.content)
        w.close()

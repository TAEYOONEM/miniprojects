import requests
from bs4 import BeautifulSoup
import os

path = './'
os.mkdir(path)

url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='

keyword = '제네시스 g70'
res = requests.get(url + keyword)

soup = BeautifulSoup(res.content, 'html.parser')
imgs = soup.find_all(class_ = '_img')

n = 1
for i in imgs :
    
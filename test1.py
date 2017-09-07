#code=utf8#
from bs4 import BeautifulSoup
import requests


url='http://www.woshipm.com/'
page=requests.get(url)
soup=BeautifulSoup(page.text,'lxml')
soup.select()
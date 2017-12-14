import requests
from bs4 import BeautifulSoup
import time
import urllib.request

next_urls=['http://www.inu.ac.kr/mbshome/mbs/inu/index.do']

while True:
    next_url = next_urls.pop()
#for next_url in next_urls:
    print('visit on '+next_url)
    doc=requests.get(next_url)
    #print(doc.text)
    soup=BeautifulSoup(doc.text, 'lxml')
    block=soup.select('a')
    #print(block)
    for a in block:
        if a.get('href') and a.get('href')[0:7]=='http://':
            print('append on list - '+a.get('href'))
            next_urls.insert(0,a.get('href'))
            #break

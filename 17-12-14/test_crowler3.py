import requests
from bs4 import BeautifulSoup
import time
import urllib.request

next_urls=['http://www.inu.ac.kr/mbshome/mbs/inu/index.do']
visited_urls=[] #방문할 url 만듦

while True:
    next_url = next_urls.pop()
    if next_url in visited_urls:
        continue
    print('visit on '+next_url)
    doc=requests.get(next_url)
    #print(doc.text)
    soup=BeautifulSoup(doc.text, 'lxml')
    block=soup.select('a')
    #print(block)
    for a in block:
        if a.get('href') and a.get('href')[0:7]=='http://':#http로 시작하는 절대 url 뽑아냄
            print('append on list - '+a.get('href'))
            if next_url not in visited_urls:#웹페이지를 방문할때마다 안 갔던 곳이면 저장
                visited_urls.append(a.get('href')[7:].split('/')[0])
            print('현재 방문 했던 url들', visited_urls)
            #if a.get('href')[7:].split('/')[0] not in visited_urls:
            next_urls.insert(0,a.get('href'))

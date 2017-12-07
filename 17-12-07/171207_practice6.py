#첨부파일 크롤링

import requests
from bs4 import BeautifulSoup
import time
import urllib.request #스스로 url 다운받는 모듈

num = 0
for i in range(48510,48610):

    print("2초간 쉬기") #페이지가 있든 없든 쉼. 공격이 아니라는 걸 의미함
    time.sleep(2)
    
    print(str(i)+ "번째 게시물 방문")
    url = 'https://abeek.inu.ac.kr/Html/Sub0501.html'
    doc = requests.get(url)

    soup = BeautifulSoup(doc.text, 'lxml')

    a_list = soup.select('a')

    if (len(a_list)<1): #내용이 없으면 넘어감 (없는 페이지이면)
        continue

    for a in a_list:
        print('https://abeek.inu.ac.kr/Html/Sub0501.html'+a.get('href'))
        urllib.request.urlretrieve('https://abeek.inu.ac.kr/Html/Sub0501.html'+a.get('href'),str(num)+'.pdf')
        num=num+1


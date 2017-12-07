#첨부파일 크롤링

import requests
from bs4 import BeautifulSoup
import time
import urllib.request #스스로 url 다운받는 모듈
'''
#f = open('myfile.txt', 'w', encoding='utf8')

url='http://abeek.inu.ac.kr'
doc = requests.get(url)
#print(doc.text)
soup = BeautifulSoup(doc.text, 'lxml')
img_list = soup.select('img')

#print(img_list)

num = 0
for img in img_list:
    #print(img)
    print('http://abeek.inu.ac.kr'+img.get('src'))
    urllib.request.urlretrieve('http://abeek.inu.ac.kr'+img.get('src'),str(num)+'.jpg')
    num=num+1
    
'''
num = 0
for i in range(48510,48610):

    print("2초간 쉬기") #페이지가 있든 없든 쉼. 공격이 아니라는 걸 의미함
    time.sleep(2)
    
    print(str(i)+ "번째 게시물 방문")
    url = 'http://www.inu.ac.kr/user/boardList.do?command=view&page=1&boardId='+str(i)+'&boardSeq=460537&id=inu_070201000000&categoryDepth='
    doc = requests.get(url)

    soup = BeautifulSoup(doc.text, 'lxml')

    a_list = soup.select('a')

    if (len(a_list)<1): #내용이 없으면 넘어감 (없는 페이지이면)
        continue

    for a in a_list:
        print('http://abeek.inu.ac.kr'+a.get('href'))
        urllib.request.urlretrieve('http://abeek.inu.ac.kr'+a.get('href'),str(num)+'.hwp')
        num=num+1


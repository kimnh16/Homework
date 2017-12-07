#크롤링

import requests
from bs4 import BeautifulSoup
import time

f = open('myfile.txt', 'w', encoding='utf8')

for i in range(48510,48610):

    print("2초간 쉬기") #페이지가 있든 없든 쉼. 공격이 아니라는 걸 의미함
    time.sleep(2)
    
    print(str(i)+ "번째 게시물 방문")
    url = 'http://www.inu.ac.kr/user/boardList.do?command=view&page=1&boardId='+str(i)+'&boardSeq=460537&id=inu_070201000000&categoryDepth='
    doc = requests.get(url)

    soup = BeautifulSoup(doc.text, 'lxml')

    body = soup.select('tr > td')

    if (len(body)<1): #내용이 없으면 넘어감 (없는 페이지이면)
        continue
    
    print(body[1].text.strip()) #두번째 tr>td라서 body[1]이라 함
    f.write(body[1].text.strip()+"\n")
    f.flush()
    


f.close()

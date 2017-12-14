import requests
from bs4 import BeautifulSoup

f=open('my_titles.txt', 'w',encoding='utf8')

for i in range(1, 50):
    doc=requests.get('http://inu-xcorps.ideaboom.net/page/notice_view.php?id='+str(i)+'&page=1')
    #print(doc.text)
    soup=BeautifulSoup(doc.text, 'lxml')
    tds=soup.select('table tr td')[1] #두번째 td? tr? 필요
    #print(tds.text) #text만 가지고오라
    f.write(tds.text)
    f.write('\n') #띄어쓰기 적용
    
f.close()

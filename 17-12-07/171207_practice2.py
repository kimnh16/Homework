import requests
from bs4 import BeautifulSoup

url = 'http://abeek.inu.ac.kr/'
doc = requests.get(url)

#print(doc.text)

soup = BeautifulSoup(doc.text. 'lxml')

body = soup.select('tr > td')

print(body[0].content)

print(body[0].text.strip()) #띄어쓴 간격 없애는 함수

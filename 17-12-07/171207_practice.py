import requests
from bs4 import BeautifulSoup

url='http://english.visitkorea.or.kr/enu/AKR/FU_EN_15.jsp?cid=2517064'
doc=requests.get(url)

print(doc.text)

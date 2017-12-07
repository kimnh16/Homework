'''

f = open('myfile.txt', 'w', encoding='utf8') #myfile.txt라는 파일에 쓴다(w). 한글 안깨지게 utf8
f.write('인천대학교 산업경영공학과\n') # 씀. 작성.
f.write('3학년 전공수업\n') #\n은 줄바꿈
f.write('메리크리스마스 종강이 얼마 안남았다!!')
f.close() # 다 썼으면 닫아야함.

# 내용을 덮어쓰지 않고 추가해서 쓰려면 w대신 a쓰기. 내용 삭제 안되고 추가됨

'''

f = open('myfile.txt', 'r', encoding='utf8')

s = f.read()
print(s)

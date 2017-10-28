import turtle as t # turtle 모듈을 불러옴
import random # random 모듈을 불러옴


def wall(): # 벽 그리는 함수 정의
    t.speed(0) # 속도를 최고 속도로 설정
    t.up() # 펜을 올림
    t.goto(-250,-250) # 거북이 위치를 (-250, 250)으로 이동
    t.down() # 펜을 내림
    for x in range(4): # 아래 과정을 4번 반복 (정사각형 그리기)
        t.forward(500) # 앞으로 500만큼 감
        t.left(90) # 왼쪽으로 90도 회전
        

def obstacle(): # 장애물 그리는 함수 정의
    t.speed(0) # 속도를 최고 속도로 설정
    t.up() # 펜을 올림
    t.goto(-150,0) # 거북이 위치를 (-150, 0)으로 이동
    t.down() # 펜을 내림
    t.color("blue") # 펜 색을 파랑으로 설정
    for x in range(4): # 아래 과정을 4번 반복 (정사각형 그리기)
        t.forward(100) # 앞으로 100만큼 감
        t.left(90) # 왼쪽으로 90도 회전
    t.color("black") # 펜 색을 검정으로 설정
    
def start(): # 랜덤의 각도로 출발하는 함수 정의
    s = 20 # 변수 s는 속도를 결정함(1)
    angle = random.randint(0, 360) # 변수 angle에 임의의 각도를 정하여 대입
    t.left(angle) # 왼쪽으로 angle만큼 회전
    t.speed(0) # 속도를 최고 속도로 설정
    while -230 < t.xcor() < 230 and -230 < t.ycor() < 230: # -230 < x < 230, -230 < y < 230 동안 아래 과정을 반복
        t.forward(s) # 앞으로 s만큼 감
    while -250 < t.xcor() < 250 and -250 < t.ycor() < 250: # -250 < x < 250, -250 < y < 250 동안 아래 과정을 반복
        t.forward(1) # 앞으로 1만큼 감
       
            

def reflect(): # 벽에 반사하는 함수 정의
    ang = t.heading() # 변수 ang에 현재 바라보는 각도를 대입
    t.color("black") # 펜 색을 검정으로 설정
    t.speed(0) # 속도를 최고 속도로 설정
    if -251 < t.ycor() <= -250 or 250 <= t.ycor() < 251: # 거북이가 벽의 위, 아래에 있다면
        t.setheading(360 - ang) # 각도를 360 - ang로 설정
    elif 0 <= ang < 180: # 거북이의 각도가 0보다 크거나 같고 180보다 작다면
        t.setheading(180 - ang) # 각도를 180 - ang로 설정
    else:  # 거북이의 각도가 180보다 크거나 같고 360보다 작다면
        t.setheading(540 - ang) # 각도를 540 - ang로 설정
        
    

def reflect2(): # 장애물에 반사하는 함수 정의
    s = 20 # 변수 s는 속도를 결정함(2)
    t.speed(0) # 속도를 최고 속도로 설정
    while -150 - s <= t.xcor() <= -150 + 100 + s and 0 - s <= t.ycor() <= 0 + 100 + s: # 거북이가 장애물 (여유가 s인) 둘레에 있다면
           if -150 <= t.xcor() <= -150 + 100 and 0 <= t.ycor() <= 0 + 100: # 거북이가 장애물 안에 있다면
               ang2 = t.heading() # 변수 ang2에 현재 바라보는 각도를 대입
               t.color("blue") # 펜 색을 파랑으로 설정
               if 0 <= t.ycor() <= 0 + 1 or 0 + 100 - 1 <= t.ycor() <= 0 + 100: # 거북이가 장애물 벽의 위, 아래에 있다면
                    t.setheading(360 - ang2) # 각도를 360 - ang2로 설정
               elif 0 <= ang2 < 180: # 거북이의 각도가 0보다 크거나 같고 180보다 작다면
                    t.setheading(180 - ang2) # 각도를 180 - ang2로 설정
               else: # 거북이의 각도가 180보다 크거나 같고 360보다 작다면
                    t.setheading(540 - ang2) # 각도를 540 - ang2로 설정
               t.forward(1) # 앞으로 1만큼 감
               break # while문에서 빠져나옴
           else: # 거북이가 장애물 밖에 있다면
                t.forward(1) # 앞으로 1만큼 감
                
        

def speedIs(n): # 장애물이 있을 때 반사하며 n의 속도로 가는 함수 정의
    t.speed(0) # 속도를 최고 속도로 설정
    t.forward(1) # 앞으로 1만큼 감
    while -250 < t.xcor() < 250 and -250 < t.ycor() < 250: # -250 < x < 250, -250 < y < 250 동안 아래 과정을 반복
        while -230 < t.xcor() < 230 and -230 < t.ycor() < 230: # -230 < x < 230, -230 < y < 230 동안 아래 과정을 반복
            reflect2() # 장애물에 반사하는 함수 호출
            t.forward(n) # 앞으로 n만큼 감
        t.forward(1) # 앞으로 1만큼 감


       
wall() # 벽 그리는 함수 호출
obstacle() # 장애물 그리는 함수 호출

t.up() # 펜을 올림
t.home() # 거북이 위치를 원점으로 이동
t.down() # 펜을 내림
t.shape("turtle") # 거북이 모양을 거북이로 설정

s = 20 # 변수 s는 속도를 결정함 (3)

start() # 랜덤의 각도로 출발하는 함수 호출
reflect() # 벽에 반사하는 함수 호출

for x in range(s): # 아래 과정을 s번 반복함
    N = s - x # 변수 N에 s - x를 대입. 프로그램이 진행되며 속도를 결정할 변수임
    t.speed(0) # 속도를 최고 속도로 설정
    speedIs(N) # 장애물이 있을 때 반사하며 n의 속도로 가는 함수 호출
    reflect() # 벽에 반사하는 함수 호출

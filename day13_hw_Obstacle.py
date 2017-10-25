import turtle as t
import random

# 벽 그리는 함수
def wall():
    t.speed(0)
    t.up()
    t.goto(-250,-250)
    t.down()
    for x in range(4):
        t.forward(500)
        t.left(90)
        
# 장애물 그리는 함수(추가함)
def obstacle():
    t.speed(0)
    t.up()
    t.goto(-150,0)
    t.down()
    for x in range(4):
        t.forward(100)
        t.left(90)
    
# 랜덤의 각도로 출발하는 함수
def start():
    s = 20 # 변수 s는 속도를 결정함(1)
    angle = random.randint(0, 360)
    t.left(angle)
    t.speed(0)
    while -230 < t.xcor() < 230 and -230 < t.ycor() < 230:
        t.forward(s)
    while -250 < t.xcor() < 250 and -250 < t.ycor() < 250:
        t.forward(1)
       
            
# 벽에 반사하는 함수
def reflect():
    ang = t.heading()
    t.speed(0)
    if -251 < t.ycor() <= -250 or 250 <= t.ycor() < 251:
        t.setheading(360 - ang)
    elif 0 <= ang < 180:
        t.setheading(180 - ang)
    else:
        t.setheading(540 - ang)
        
    
# 장애물에 반사하는 함수 (추가함)
def reflect2():
    s = 20 # 변수 s는 속도를 결정함(2)
    t.speed(0)
    while -150 - s <= t.xcor() <= -150 + 100 + s and 0 - s <= t.ycor() <= 0 + 100 + s:
        while t.xcor() <= -150 or t.xcor() >= -150 + 100 or t.ycor() <= 0 or t.ycor() >= 0 + 100:
            if -150 <= t.xcor() <= -150 + 100 and 0 <= t.ycor() <= 0 + 100:
                ang2 = t.heading()
                if 0 - 1 < t.ycor() <= 0 or 0 + 100 <= t.ycor() < 0 + 100 + 1:
                    t.setheading(360 - ang2)
                elif 0 <= ang2 < 180:
                    t.setheading(180 - ang2)
                else:
                    t.setheading(540 - ang2)
            t.forward(1)
     
        
# n의 속도로 가는 함수
def speedIs(n):
    t.speed(0)
    t.forward(1)
    while -250 < t.xcor() < 250 and -250 < t.ycor() < 250:
        while -230 < t.xcor() < 230 and -230 < t.ycor() < 230:
            reflect2()
            #while 0 - 1 < t.ycor() <= 0 and -150 -1 < t.xcor() < 0 + 100 + 1:
            #    if -150 <= t.xcor() <= -150 + 100 and 0 <= t.ycor() <= 0 + 100:
            #        reflect2()
            #    else:
            #        t.forward(1)
            t.forward(n)
        t.forward(1)


       
wall()
obstacle()

t.up()
t.home()
t.down()
t.shape("turtle")

s = 20 # 변수 s는 속도를 결정함 (3)

start()
reflect()

for x in range(s):
    N = s - x
    t.speed(0)
    speedIs(N)
    reflect()

    

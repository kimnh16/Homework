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
<<<<<<< HEAD
=======
        
# 장애물 그리는 함수(추가함)
def obstacle():
    t.speed(0)
    t.up()
    t.goto(-150,0)
    t.down()
    for x in range(4):
        t.forward(100)
        t.left(90)
>>>>>>> 12fc99e2b2dbfae74d6b8686590d6ad961a2c21c
    
# 랜덤의 각도로 출발하는 함수
def start():
    angle = random.randint(0, 360)
    t.left(angle)
    t.speed(0)
    while -230 < t.xcor() < 230 and -230 < t.ycor() < 230:
        t.forward(20)
    while -250 < t.xcor() < 250 and -250 < t.ycor() < 250:
        t.forward(1)
<<<<<<< HEAD
        
# 벽에 반사하는 함수
def reflect():
    ang = t.heading()
    t.speed(0)
    if 250 <= t.ycor() < 251 or -251 < t.ycor() <= -250:
=======

# 벽에 반사하는 함수(수정해야함)
def reflect1():
    ang = t.heading()
    t.speed(0)
    if 0 <= ang < 90:
        if t.xcor() == 250:
            t.left(2 * (ang - 270))
        else:
            t.right(2 * ang)
    elif 90 <= ang < 180:
        if t.ycor() == 250:
            t.left(2 * ang)
        else:
            t.right(2 * (ang - 90))
    elif 180 <= ang < 270:
        if t.xcor() == -250:
            t.left(2 * (ang - 90))
        else:
            t.right(2 * (ang - 180))
    elif 270 <= ang <= 360:
        if t.ycor() == -250:
            t.left(2 * (ang - 180))
        else:
            t.right(2 * (ang - 270))
            
       
            
# 벽에 반사하는 함수 (추가함)
def reflect():
    ang = t.heading()
    t.speed(0)
    if t.ycor() == 250 or t.ycor == -250:
>>>>>>> 12fc99e2b2dbfae74d6b8686590d6ad961a2c21c
        t.setheading(360 - ang)
    elif 0 <= ang < 180:
        t.setheading(180 - ang)
    else:
        t.setheading(540 - ang)
    
<<<<<<< HEAD
# n의 속도로 가는 함수
def speedIs(n):
    t.speed(0)
    t.forward(1)
    while -250 < t.xcor() < 250 and -250 < t.ycor() < 250:
        while -230 < t.xcor() < 230 and -230 < t.ycor() < 230:
            t.forward(n)
=======
# 장애물에 반사하는 함수 (추가함)
def reflect2():
    ang2 = t.heading()
    t.speed(0)
    if t.ycor() == 0 or t.ycor() == 100:
        t.setheading(360 - ang2)
    elif 0 <= ang2 < 180:
        t.setheading(180 - ang2)
    else:
        t.setheading(540 - ang2)
        
     
        
# 최고속도로 가는 함수
def best():
    while -250 <= t.xcor() <= 250 and -250 <= t.ycor() <= 250:
        t.speed(0)
>>>>>>> 12fc99e2b2dbfae74d6b8686590d6ad961a2c21c
        t.forward(1)


<<<<<<< HEAD
=======
# 가장 느리게 가는 함수
def slow():
    while -250 <= t.xcor() <= 250 and -250 <= t.ycor() <= 250:
        t.speed(1)
        t.forward(1)
>>>>>>> 12fc99e2b2dbfae74d6b8686590d6ad961a2c21c
       
wall()

t.up()
t.home()
t.down()
t.shape("turtle")

start()
reflect()

<<<<<<< HEAD
for x in range(20):
    N = 20 - x
    t.speed(0)
    speedIs(N)
    reflect()

    
=======
# 만약 거북이가 향하는 방향이 장애물을 지난다면 reflect2()를 실행(코딩짜기)

for i in range(10):
    while -250 <= t.xcor() <= 250 and -250 <= t.ycor() <= 250:
        if t.xcor() == -150 or t.xcor() == -50 or t.ycor() == 0 or t.ycor() == 100:
            reflect2()
            best()        
        else:
            t.speed(10 - i) #10번 반복할때만 오류 안남
            t.forward(1)
    reflect()
>>>>>>> 12fc99e2b2dbfae74d6b8686590d6ad961a2c21c

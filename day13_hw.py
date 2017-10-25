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

  
# 랜덤의 각도로 출발하는 함수
def start():
    angle = random.randint(0, 360)
    t.left(angle)
    t.speed(0)
    while -230 < t.xcor() < 230 and -230 < t.ycor() < 230:
        t.forward(20)
    while -250 < t.xcor() < 250 and -250 < t.ycor() < 250:
        t.forward(1)
       
            
# 벽에 반사하는 함수
def reflect():
    ang = t.heading()
    t.speed(0)
    if 250 <= t.ycor() < 251 or -251 < t.ycor() <= -250:
        t.setheading(360 - ang)
    elif 0 <= ang < 180:
        t.setheading(180 - ang)
    else:
        t.setheading(540 - ang)

                
# n의 속도로 가는 함수
def speedIs(n):
    t.speed(0)
    t.forward(1)
    while -250 < t.xcor() < 250 and -250 < t.ycor() < 250:
        while -230 < t.xcor() < 230 and -230 < t.ycor() < 230:
            t.forward(n)
        t.forward(1)


       
wall()

t.up()
t.home()
t.down()
t.shape("turtle")

start()
reflect()

for x in range(20):
    N = 20 - x
    t.speed(0)
    speedIs(N)
    reflect()

    

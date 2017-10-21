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
    t.forward(250)
    while -250 <= t.xcor() <= 250 and -250 <= t.ycor() <= 250:
        t.speed(0)
        t.forward(1)

# 벽에 반사하는 함수(수정해야함)
def reflect():
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

# 최고속도로 가는 함수
def best():
    while -250 <= t.xcor() <= 250 and -250 <= t.ycor() <= 250:
        t.speed(0)
        t.forward(1)

# 빠르게 가는 함수
def fast():
    while -250 <= t.xcor() <= 250 and -250 <= t.ycor() <= 250:
        t.speed(10)
        t.forward(1)

# 가장 느리게 가는 함수
def slow():
    while -250 <= t.xcor() <= 250 and -250 <= t.ycor() <= 250:
        t.speed(1)
        t.forward(1)
        
wall()

t.up()
t.home()
t.down()
t.shape("turtle")

start()
reflect()
print(ang)

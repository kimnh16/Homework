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

def start():
    angle = random.randint(0, 360)
    t.left(angle)
    while -250 <= t.xcor() <= 250 and -250 <= t.ycor() <= 250:
        t.forward(1)
        t.speed(0)
    
wall()

t.up()
t.home()
t.down()
t.shape("turtle")

start()
ang = t.heading()
print(ang)

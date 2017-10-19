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

wall()
t.up()
t.home()
t.down()
t.shape("turtle")

print(t.pos())

import turtle as t
import random

def wall():
    t.speed(0)
    t.up()
    t.goto(-250, -250)
    t.down()
    for i in range(4):
        t.forward(500)
        t.left(90)

wall()
t.up()
t.home()
t.down()
t.shape("turtle")

#원 만들기

import turtle as t
t.shape("turtle")

n=100
t.color("purple")
t.begin_fill()
for x in range(n):
    t.forward(5)
    t.left(360/n)
t.end_fill()

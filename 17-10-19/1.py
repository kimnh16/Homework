import turtle as t
import random

t.up()
t.goto(-300, 0)
t.down()
t.forward(600)

target = random.randint(0, 250)
#print(target)
t.up()
t.goto(target, 2)
t.down()
t.pensize(4)
t.color("green")
t.forward(60)

t.pensize(1)
t.color("black")
t.up()
#t.shape("turtle")
t.goto(-200, 10)
t.down()

def up():
    t.left(5)

def down():
    t.right(5)

def circle():
    while t.ycor() >= 0:
        t.forward(10)
        t.right(360/100)
        
t.onkeypress(up,"Up")
t.onkeypress(down, "Down")
t.onkeypress(circle, "space")
b = t.xcor()
t.listen()

if b <= target and b >= target+2:
    print("success")
else:
    print("fail")

import turtle as t
import random

def right():
    t.setheading(0)

def up():
    t.setheading(90)

def left():
    t.setheading(180)

def down():
    t.setheading(270)

def play():
    t.forward(3) # 나(흰 거북이)의 속도 결정
    ang = te.towards(t.pos())
    te.setheading(ang)
    te.forward(3) # 악당 속도(빨간 거북이) 결정

t.bgcolor("orange")
t.speed(0)
t.up()
t.goto(-230,-230)
t.down()
for x in range(4):
    t.forward(460)
    t.left(90)

te = t.Turtle()
te.up()
te.goto(0,200)
te.shape("turtle")
te.color("red")

ts = t.Turtle()
ts.up()
ts.goto(0,-200)
ts.shape("circle")
ts.color("green")

t.up()
t.goto(0,0)
t.shape("turtle")
t.color("white")

t.onkeypress(right,"Right")
t.onkeypress(up,"Up")
t.onkeypress(left,"Left")
t.onkeypress(down,"Down")
t.listen()

x = True
score = 0
while x: # x는 스위치 역할
    play()
    if t.distance(te) <= 10:
        #print("나와 악당의 거리는? ", t.distance(te))
        t.color("red")
        t.write("GAME OVER", False, "center", ("", 100))
        t.color("blue")
        t.write(score, False, "center", ("", 50))
        x = False # 게임을 멈춤
    if t.distance(ts) <= 10:
        #print("먹었다")
        score += 1
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        ts.goto(x,y)

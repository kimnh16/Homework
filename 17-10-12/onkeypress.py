import turtle as t

def turn_right():
    t.color("red")
    t.setheading(0)
    t.forward(30)

def turn_up():
    t.color("orange")
    t.setheading(90)
    t.forward(30)

def turn_left():
    t.color("yellow")
    t.setheading(180)
    t.forward(30)
    
def turn_down():
    t.color("green")
    t.setheading(270)
    t.forward(30)

def blank():
    t.clear()

def ff():
    t.speed(0)

def ss():
    t.speed(1)

t.shape("turtle")
#t.speed(0)
t.onkeypress(turn_right,"Right")
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_left,"Left")
t.onkeypress(turn_down,"Down")
t.onkeypress(blank,"Escape")
t.onkeypress(ff, "f")
t.onkeypress(ss, "s")
t.listen()

import turtle as t
import time
import random

x = input("성함을 입력해주세요:")

if x == "김관호":
    print("김관호 교수님, 안녕하세요? 김나형입니다. 제가 만든 패턴을 보여드리겠습니다.")

    start = time.time()
    
    t.bgcolor("black")
    t.speed(0)
    
    for x in range(30):
        angle = random.randint(1, 360)
        
        if angle < 90:
            t.color("red")
            t.pensize(3)
            for i in range(3):
                t.forward(50)
                t.left(120)
            t.pensize(1)
            
        if 90 <= angle < 180:
            t.color("green")
            t.begin_fill()
            for j in range(5):
                t.forward(50)
                t.left(75)
            t.end_fill()
            
        if 180 <= angle < 270:
            t.color("blue")
            for k in range(60):
                t.circle(25)
                t.left(6)
                
        else:
            t.color("white")
            for l in range(10,100,5):
                t.forward(l)
                t.left(90)
        t.left(angle)
    
    end = time.time()
    et = end - start

    print(et, "초 동안 제 패턴을 기다려주셔서 감사합니다.")
    
else:
    print("죄송합니다! 제 과제는 김관호 교수님만 보실 수 있습니다.")

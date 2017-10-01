import turtle as t
t.shape("turtle")

# 삼각형 그리기
t.color("red")          # 펜 색상을 빨간색으로 바꿈
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)

# 사각형 그리기
t.color("green")        # 펜 색상을 녹색으로 바꿈
t.pensize(3)            # 펜 굵기를 3으로 바꿈
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

# 원 그리기
t.color("blue")         # 펜 색상을 파란색으로 바꿈
t.pensize(5)            # 펜 굵기를 5로 바꿈
t.circle(50)

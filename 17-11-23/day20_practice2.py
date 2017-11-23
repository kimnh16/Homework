import math
import turtle as t

x_min = -5
x_max = +5

y_min = -5
y_max = +5

space = 0.1

t.setworldcoordinates(x_min, y_min, x_max, y_max)
t.speed(0)
t.pensize(2)

#x축 그리기
t.up()
t.goto(x_min,0)
t.down()
t.goto(x_max,0)

#y축 그리기
t.up()
t.goto(0,y_min)
t.down()
t.goto(0,y_max)

function1 = input("첫번째로 그릴 함수 : ")
function2 = input("두번째로 그릴 함수 : ")

#그래프 그리기
t.color("red")
x = x_min
exec(function1)
t.up()
t.goto(x,y)
t.down()
func0_list = [ t.xcor() ]
func1_list = [ t.ycor() ]
while x <= x_max:
    x = x + space
    exec(function1)
    t.goto(x,y)
    func0_list.append(t.xcor())
    func1_list.append(t.ycor())
t.color("yellow")
x = x_min
exec(function2)
t.up()
t.goto(x,y)
t.down()
func2_list = [ t.ycor() ]
while x <= x_max:
    x = x + space
    exec(function2)
    t.goto(x,y)
    func2_list.append(t.ycor())
print(func1_list)
print(func2_list)

#func3_list = []
#for i in range(len(func0_list)):
#    A = abs(func1_list[i] - func2_list[i])
#    func3_list.append(A)

#for x in range(len(func0_list)):
#    if func3_list[i] < 1:
#        a.append(i)

for i in range(len(func0_list)):
    if abs(func1_list[i] - func2_list[i]) < 1:
        print("교점 : x=", func0_list[i], ", y=", func1_list[i])

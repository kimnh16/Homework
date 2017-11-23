import math

print("ax^2 + bx + c = 0")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a == 0:
    print("다시 입력하세요")
else:
    print("이차방정식이 맞습니다^^")
    d = b**2 - 4*a*c
    print("판별식: D = ", d)
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print("2개의 해 :", x1, x2)
    if d == 0:
        x = -b/(2*a)
        print("1개의 해 :", x)
    if d < 0:
        print("해가 없다")

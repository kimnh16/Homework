import random

num_q = 5
num_c = 0

for i in range(5):

    a1 = random.randint(1, 100)
    op = random.randint(0, 2)
    a2 = random.randint(1, 100)

    opp=""
    if op == 0:
        opp = "*"
    if op == 1:
        opp = "-"
    if op == 2:
        opp = "+"
        
    q = str(a1) + opp + str(a2)

    print("problem: ",q)
    u_ans = input()

    c_ans = eval(q)

    print("u_ans: ", u_ans, "c_ans: ", c_ans)

    if int(u_ans) == c_ans:
        print("yes!")
        num_c = num_c + 1
    else:
        print("no")

print(num_c,"/", num_q)
print(num_c / num_q * 100)

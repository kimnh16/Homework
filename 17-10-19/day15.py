import random
import time

w = ["cat", "dog", "fox", "monkey", "mouse"]

start = time.time()

for i in range(5):

    q = random.choice(w)
    print((i+1), "the question -> ", q)
    a = input()

    while a != q:
        print("wrong!! agin")
        a = input()

    print("success")

end = time.time()

et = end - start
print("elapsed time: ", et)

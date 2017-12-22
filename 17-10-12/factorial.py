def factorial(n):
    fact = 1
    for x in range(1, n+1):
        fact = fact * x
    return fact

for x in range(1,21):
    print(x, "! = ", factorial(x))

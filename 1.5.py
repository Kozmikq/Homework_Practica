def fuctorial(x):
    s = 1
    for i in range(2, x + 1):
        s *= i
    return s

def zeros(x): #В каждом 5-ом факториале +1 ноль в конце
    return x // 5
x = int(input())
print(fuctorial(x), zeros(x))
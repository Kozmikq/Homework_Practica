def primediv(x):
    a = [i for i in range(2, x + 2)]        # массив чисел от 2 до x+1(на всякий случай)
    mx = -99999999999
    t = 0
    for i in range(2,x+2):
        for j in range(len(a)):
            if (a[j] % i == 0) and (a[j] != i) and (a[j] in a):
                a[j] = 0                                       #заменяем эл-ты которые деляться на что то на 0
    for i in range(a.count(0)):
        a.remove(0)
    for i in a:
        if x % i ==0:
            if i > mx:                          #проход по массиву и нахождение наиб прстого делителя
                mx = i
    if x in a:
        return "Простое число"
    else:
        return mx
x = int(input())
print(primediv(x))


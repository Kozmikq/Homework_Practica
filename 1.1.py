def polynom():
    print('Введите степень многочлена n и х0')
    n=int(input())
    x0=int(input())
    a = [0]*(n+1)           #массив с коэффициентами а
    print('введите значения коэффициентов ')
    for i in range (n + 1):
        a[i] = int(input())

    Polynom = a[0]
    for i in range(n):
        Polynom *= x0
        Polynom += a[i + 1]
    print('Значение многочлена: ', Polynom)

    Polynom1 = a[0]*n
    for i in range(1, n):
        Polynom1 *= x0
        Polynom1 += a[i] * (n-i)
    print("Значение производной: ", Polynom1)
polynom()
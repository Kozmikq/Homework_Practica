def Polynomus():
    print('Введите степень многочлена n, значение х0 ')
    n = int(input())
    x0 = int(input())
    a = [0]*(n+1) #создаем массив с коэффициентами а, +1 тк существует а0 коэффициент
    print('введите значения коэффициентов ')
    for i in range (n + 1):
        a[i] = int(input())

    Polynom = a[0]
    for i in range (n):
        Polynom *= x0
        Polynom += a[i + 1]
    print('Значение многочлена: ', Polynom)

    Polynom1 = a[0]*n
    for i in range(1, n): #цикл с 1 так как степень уменьшается на 1
        Polynom1 *= x0
        Polynom1 += a[i] * (n-i)
    print("Значение производной: ", Polynom1)
Polynomus()
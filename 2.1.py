def maxk(a, k):
    n = len(a)
    s = 0
    mxsum = sum(a[:k])
    for i in range(k, n + 1):                # перебор от к тк мы делаем срез снизу основываясь на этом
        s = sum(a[i - k: i])                 # срез от 0 до i не включительно эл-та (при i =  k)
        if s > mxsum:
            mxsum = s
    return mxsum

n = int(input("Введите размер массива: "))
k = int(input("Введите число k: "))
a = []
if k > n:                      # последовательность к болше чем количество эл-тов в массиве
    print("так нельзя")
else:
    for i in range(n):
        a.append(int(input("Введите число из массива: ")))
    print(maxk(a, k))
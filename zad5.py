def FibonacciNumbers(x):
    FibonacciList = []
    a, b = 1, 1

    for i in range(x - 1):       # положительные числа
        FibonacciList.append(a)
        a, b = b, a + b
    a, b = 0, 1

    for i in range(x):           # отрицательные числа
        FibonacciList.insert(0, a)
        a, b = b, a - b

    return FibonacciList

n = int(input('Введите число: ')) + 1
FibonacciList = FibonacciNumbers(n)
print(FibonacciList)
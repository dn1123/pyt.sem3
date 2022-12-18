from random import randrange
quantity = int(input('Задайте количество элементов списка: '))
list1 = [randrange(50) for i in range(quantity)]
print(f'Список случайных чисел: {list1}')

# или list1 = input('Введите элементы через пробел').split() и тогда print(int(list1))

# нечет. quantity - // + 1, четн. quantity - // + 0
i = 0
for i in range(quantity // 2 + len(list1) % 2):
     print(list1[i] * list1[quantity - i - 1], end = ' ')
     i += 1
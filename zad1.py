print('Программа найдет сумму элементов списка на нечётных позициях')

from random import randrange
quantity = 1500
list1 = [randrange(50) for i in range(quantity)]
print(f'Список из случайных чисел: {list1}')

summa1 = 0
for i in range(0, quantity, 2):
    summa1 += list1[i]

summa2 = 0
for i in range(1, quantity, 2):
    summa2 += list1[i]

print(f'Сумма элементов на нечётных (для человека) позициях {summa1}')
print(f'Сумма элементов на нечётных (для компьютера) позициях {summa2}')
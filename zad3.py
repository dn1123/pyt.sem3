import random
quantity = int(input('Задайте количество элементов списка: '))
list1 = [round(random.uniform(1, 30), 2) for i in range(quantity)]
print(f'Список случайных вещественных чисел: {list1}')

min = 1
max = 0
for i in list1:                      # поиск минимума и максимума
    if (i - int(i)) <= min:          # от числа отнимем целую часть, чтобы получить дробную
        min = i - int(i)
    if (i - int(i)) >= max:          # int() возвращает целочисленный объект
        max = (i - int(i))

print(round(max - min, 2))
print('Программа переведёт десятичное число в двоичное')
DecNumber = int(input('Введите число: '))

DoubNumb = ''                                    # двоичное число в строковом виде
while DecNumber != 0:
    DoubNumb = str(DecNumber % 2) + DoubNumb     # остаток от деления допишем впереди
    DecNumber = DecNumber // 2                   # целочисленное деление

print(f'{DecNumber} в двоичной системе - это {DoubNumb}')
"""Заполните массив элементами арифметической прогрессии. Её первый элемент, 
разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки."""

def arith_prog(number, difference, length_):
    list1 = []
    for i in range(length_):
            list1.append(number)
            number = number + difference
    return list1


first_num = int(input('Введите первое число арифметической прогрессии: '))
diff = int(input('Введите разность арифметической прогрессии: '))
length_arith = int(input('Введите количество элементов списка: '))
#first_num, diff, length_arith = map(int,input('Введите первое число, разность, длину прогрессии: ').split())
print(arith_prog(first_num,diff,length_arith))


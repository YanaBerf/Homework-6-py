"""Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного
максимума)
Ввод: [-5, 9, 0, 3, -1, -2, 1,
4, -2, 10, 2, 0, -9, 8, 10, -9,
0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]"""

def create_list(min_value,max_value):
    list2 = []
    for i in range(min_value, max_value + 1, 1):
        list2.append(i)
    return list2


def search_index(list1,list2):
    index_list = [i for i in range(len(list1)) if list1[i] in list2]
    return index_list


list1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_num, max_num = map(int,input('enter number: ').split())
#max_num = int(input('enter number: '))
list2 = create_list(min_num, max_num)             
print(search_index(list1,list2))

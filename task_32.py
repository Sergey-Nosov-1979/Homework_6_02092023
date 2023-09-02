'''Задача 32: Определить индексы элементов массива (списка), значения которых 
принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше 
заданного максимума)'''


arr = [1, 6, 5, 3, 8, 12]
min_value = 4
max_value = 8

def find_index(arr, min_value, max_value):
    index = []
    for i in range(len(arr)):
        if min_value <= arr[i] <= max_value:
            index.append(i)
    return index

result = find_index(arr, min_value, max_value)
print(result)
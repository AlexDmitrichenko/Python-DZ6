# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность 
# и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: 
# an = a1+(n-1)*d. Каждое число вводится с новой строки. Пример Ввод: 7 2 5  Вывод: 7 9 11 13 15

# a = int(input("Pls enter a first element of the array: "))
# d = int(input("Pls enter a difference of the element: "))
# n = int(input("Pls enter the length of the list: "))
# newArray = []
# sum = 0

# for i in range(n):
#     if sum < a:
#         newArray.append(a)
#         sum = a
#     else:
#         newArray.append(sum+d)
#         sum = sum + d

# print(newArray)

#**************************************************************************************
# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
# Пример Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

# from random import randint

# array = [randint(-10,10) for i in range(int(input("Pls enter the length of the array: ")))]

# print(array)

# minRange = int(input("Pls enter the minimum of the range: "))
# maxRange = int(input("Pls enter the maximum of the range: "))

# print([i for i in range(len(array)) if array[i]>=minRange and array[i]<=maxRange])
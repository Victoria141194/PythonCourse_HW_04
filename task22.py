#Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
#m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.


import random

n = int(input("Введите число n - кол-во элементов первого множества: "))
x = int(input("Начало первого списка: "))
y = int(input("Конец первого списка: "))
set_first = ([random.randint(x, y) for i in range(n)])
my_list_first = sorted(list(set(set_first)))

m = int(input("Введите число m - кол-во элементов второго множества: "))
a = int(input("Начало первого списка: "))
b = int(input("Конец первого списка: "))
set_second = ([random.randint(a, b) for j in range(m)])
my_list_second = sorted(list(set(set_second)))

print(f'Первое множество: {set_first} \nУпорядоченное первое множество без повторений {my_list_first}')

print(f'Второе множество:{set_second} \nУпорядоченное второе множество без повторений{my_list_second}')
#1. Для целочисленной квадратной матрицы найти число элементов, кратных k, и наибольший из этих элементов.

import random as rd

n=int(input("Введите значение квадратной матрицы: "))
mas=[] #создание массива
for i in range(n):
    mas.append([0]*n) 

for i in range(len(mas)): #заполняем массив случайными значениями
    for j in range(len(mas[i])):
        mas[i][j]=rd.randint(1,50)

max=mas[0][0] #нахождение максимального элемента массива
for i in range(len(mas)): 
    for j in range(len(mas[i])):
       if max<mas[i][j]:
        max=mas[i][j]
print("Максимальное значение в матрице: %s"  %max)

k=int(input('Введите кратное число "k": '))
l=0
for i in range(len(mas)): #нахождение чисел кратных k
    for j in range(len(mas[i])):
            if mas[i][j]%k==0:
                l+=1
print("Кол-во чисел кратных k: %s" %l)

print("Массив: ")
for i in range(n): #Вывод массива
    for j in range(n):
        print(mas[i][j], end = ' ')
    print()
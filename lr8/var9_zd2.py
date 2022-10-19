#2. В данной действительной квадратной матрице порядка n найти наибольший по модулю элемент. Получить квадратную матрицу порядка 
#n — 1 путем отбрасывания из исходной матрицы строки и столбца, на пересечении которых расположен элемент с найденным значением.

import random as rd
import math

n=int(input("Введите значение квадратной матрицы: "))
mas=[] #создание массива
for i in range(n):
    mas.append([0]*n) 

for i in range(len(mas)): #заполняем массив случайными значениями
    for j in range(len(mas[i])):
        mas[i][j]=rd.randint(-50,50)

print("Массив: ")
for i in range(n): #Вывод массива
    for j in range(n):
        print(mas[i][j], end = ' ')
    print()

max=math.fabs(mas[0][0]) #нахождение максимального элемента массива по модулю
for i in range(len(mas)): 
    for j in range(len(mas[i])):
       if math.fabs(max)<math.fabs(mas[i][j]):
        max=(mas[i][j])
        stroka=i
        stolbec=j
print("Номер строки: %s " %stroka, end='\n')
print("Номер столбца: %s " %stolbec, end='\n')
print("Максимальное значение в матрице по модулю: %s"  %max)

mas1=[[0 for x in range(n-1)] for y in range(n-1)]


del mas[stroka] #удаление строки и столбца на пересечении
for i in range(len(mas)):
    del mas[i][stolbec]


print("Массив: ")
for i in range(n-1): #Вывод массива
    for j in range(n-1):
        print(mas[i][j], end = ' ')
    print()
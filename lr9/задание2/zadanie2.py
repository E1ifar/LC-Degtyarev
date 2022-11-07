import math

n=int(input("Введите значение квадратной матрицы: ")) 
with open('lr9\задание2\Degtyarev_vvod2.txt', 'r') as file: #получение данных из файла
    mas1 = []
    for mas1_line in file.readlines():
        line = mas1_line.split()
        mas1 += line
    mas1 = list(map(int, mas1))

mas = []
for l in range(n):
    line = [mas1.pop(0) for l in range(n)]
    mas.append(line) # преобразование данных полученных выше в массив

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

file2 = open('lr9\задание2\Degtyarev_vivod2.txt', 'w') #запись массива в файл
for i in range(n-1):
    for j in range(n-1):
        a = str(mas[i][j])
        file2.write(a)
        file2.write(' ')
file2.close()    
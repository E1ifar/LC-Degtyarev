#Ввод и вывод данных матриц из практической номер 8

n=int(input("Введите значение квадратной матрицы: "))
 #создание массива
 

#with open('lr9\задание1\Degtyarev_vvod1.txt','r') as file:
    #for i in range(len(mas)):
     #   for j in range (len(mas[i])):
      #      for line in file:
       #         mas.append([int(x) for x in line.split()]) 

with open('lr9\задание1\Degtyarev_vvod1.txt', 'r') as file:
    mass = [line.split() for line in file]
print(mass)


mas=[]    
print("Массив: ")
for i in range(n): #Вывод массива
    for j in range(n):
        print(mas[i][j], end = ' ')
    print()

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
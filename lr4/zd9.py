n=int(input("Введите количество чисел n: "));
i=1;
a1=0;
a2=1;
sum=1;
while i<=n-2:
    i=i+1;
    a3=a1+a2;
    sum=sum+a3;
    s=a2;
    a2=a3;
    a1=s;
print("Сумма ряда из " + str(n) + " чисел Фибоначи: " + str(sum));
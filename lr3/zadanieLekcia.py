a=int(input("Введите число А: "));
b=int(input("Введите число В: "));
if a<b and b>4:
    x=a+b;
elif a>b:
    x=a-b;
else:
    x=a**2;
print(x);
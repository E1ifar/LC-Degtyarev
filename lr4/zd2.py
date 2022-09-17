a=int(input("Введите число А: "));
b=int(input("Введите число В: "));
if a<b:
    for i in range(a,b+1):
        print(i, end="; ");
else:
    for y in reversed(range(b, a+1)):
        print(y, end="; ");
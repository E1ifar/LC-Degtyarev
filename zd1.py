a=int(input("Введите число А: "));
b=int(input("Введите число В, которое больше, чем число А: ")); #a<=b
if a<=b:
    for i in range(a, b+1):
        print(i, end="; ");
else:
    print("Введите А<=B !");
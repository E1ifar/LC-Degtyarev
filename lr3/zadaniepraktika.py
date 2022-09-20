a=int(input("Введите целое число 'a': "));
b=int(input("Введите целое число 'b': "));
c=int(input("Введите целое число 'c': "));
if a>=1 and a<=3:
    if b>=1 and b<=3:
        if c>=1 and c<=3:
            print("Вывод: %s" %a, b, c);
        else:
            print("Вывод: %s" %a, b);
    else:
        if c>=1 and c<=3:
            print("Вывод: %s" %a, c);
        else:
            print("Вывод: %s" %a);
else:
    if b>=1 and b<=3:
        if c>=1 and c<=3:
            print("Вывод: %s" %b, c);
        else:
            print("Вывод: %s" %b);
    else:
        if c>=1 and c<=3:
            print("Вывод: %s" %c);
        else:
            print("Нету чисел из промежутка[1;3]");
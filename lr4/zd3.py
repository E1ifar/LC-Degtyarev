# Даны два целых числа A и В, A>B. Выведите все нечётные числа от A до B
#включительно, в порядке убывания.
b=int(input("Введите число В: "));
a=int(input("Введите число А>B: "));
if (b % 2) == 0:
    for i in reversed((range(b+1, a+1, 2))):
     print (i, end="; ");
else:
    for i in reversed(range(b, a+1, 2)):
        print (i, end="; ");
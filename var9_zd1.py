n=[];
def cifr(a):
    while a>1:
        n.append(a%10);
        a=a//10;
    return n;
a=int(input("Введите число: "));
i=0;
d=a;
while d>0:
    print(cifr(d));
    s=sum(n);
    i=i+1;
    d=d-s;
    n.clear();
    print(d);
print(i);
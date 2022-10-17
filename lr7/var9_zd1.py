n=[]
def cifr(a):
    while a>0:
        n.append(a%10)
        a=a//10
    return n
def su(g):
    su=0
    for i in g:
        su=su+i
    return su
a=int(input("Введите число: "))
i=0
d=a
while d>0:
    cifr(d)
    s=su(n)
    i=i+1
    d=d-s
    n.clear()
    print(d)
print(i)
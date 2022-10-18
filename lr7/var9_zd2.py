import random as rd

m1=[rd.randint(1, 100) for i in range(rd.randint(1,10))] 
m2=[rd.randint(1, 100) for i in range(rd.randint(1,10))]
m3=[rd.randint(1, 100) for i in range(rd.randint(1,10))]
def pr(x):
    res=1
    for i in x:
        res=res*i
    return res
def su(g):
    su=0
    for i in g:
        su=su+i
    return su
print(m1, m2, m3, end='\n')
print(pr(m1), su(m1), end='\n')
print(pr(m2), su(m2), end='\n')
print(pr(m3), su(m3), end='\n')


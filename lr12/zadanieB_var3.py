def funs():
    a = []
    i = 1
    while i > 0:
        l = int(input())
        if l != 0:
            a.append(l)
        else:
            break
    i=0
    for i in list(a):
        if i % 2 != 0 or i == 0:
            print(a[i-1])
    funs()
    
if __name__ == "__main__":
    funs()
a=str(input("Введите текст: "));
count=0;
for b in a.split(" "):
    if b.strip()[0] == 'е':
        count = count + 1;
print(count);
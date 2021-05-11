n = int(input())
cont = 0
while cont < 6:
    if n % 2 == 1:
        print(n)
        n += 1
        cont += 1
    else:
        n += 1

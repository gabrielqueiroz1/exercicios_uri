x = 1
while x != 0:
    x = int(input())
    s = 0
    cont = 5
    aux = x
    if x == 0:
        break
    while cont != 0:
        if aux % 2 == 0:
            s += aux
            cont -= 1
        aux += 1
    print(s)

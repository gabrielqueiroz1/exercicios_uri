n = int(input())
for i in range(n):
    s = 0
    cont = 0
    x, y = [int(i) for i in input().split()]
    aux = x
    while y != 0:
        if aux % 2 == 1:
            s += aux
            y -= 1
        aux += 1
    print(s)

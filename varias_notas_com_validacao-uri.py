c = soma = 0
x = 1
while c < 2 and x == 1:
    n = float(input())
    if n < 0 or n > 10:
        print("nota invalida")
    if 0 <= n <= 10:
        soma += n
        c += 1
    if c == 2:
        print("media = {:.2f}".format(soma/2))
        x = -1
    while x < 1 or x > 2:
        print("novo calculo (1-sim 2-nao)")
        x = int(input())
        if x == 1:
            c = soma = 0
        if x == 2:
            break

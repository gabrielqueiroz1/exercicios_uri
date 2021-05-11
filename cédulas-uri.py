n = int(input())
c = 100
contC = 0
print(n)
while True:
    if n >= c:
        n -= c
        contC += 1
    elif contC > 0 or contC < c:
        print(f'{contC} nota(s) de R$ {c},00')
        if c == 100:
            c = 50
        elif c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 5
        elif c == 5:
            c = 2
        elif c == 2:
            c = 1
            if n == 0:
                contC = 0
                print(f'{contC} nota(s) de R$ {c},00')
                break
        contC = 0
        if n == 0:
            break

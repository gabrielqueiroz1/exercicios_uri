'''n = int(input())
for i in range(1, 11):
    print(f"{i} x {n} = {i * n}")
'''

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    try:
        return n * (fatorial(n - 1))
    except RecursionError:
        return n * (fatorial(n - 1))

while True:
    try:
        m, n = [int(i) for i in input().split()]
        soma = fatorial(m) + fatorial(n)
        print(soma)
    except EOFError:
        break

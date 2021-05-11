def fatorial(n):
    if n == 0 or n == 1:
        return 1
    try:
        return n * (fatorial(n - 1))
    except RecursionError:
        return n * (fatorial(n - 1))

n = int(input())

print(fatorial(n))

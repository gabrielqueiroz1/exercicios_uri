m = n = 1
ordem = []
while True:
    m, n = map(int, input().split())
    if m <= 0 or n <= 0:
        break
    else:
        if m > n:
            for i in range(n, m+1):
                ordem.append(i)
            soma = sum(ordem)
            for i in sorted(ordem):
                print(f"{i}", end=' ')
            print(f"Sum={soma}")
            ordem = []
        if n > m:
            for i in range(m, n+1):
                ordem.append(i)
            soma = sum(ordem)
            for i in sorted(ordem):
                print(f"{i}", end=' ')
            print(f"Sum={soma}")
            ordem = []

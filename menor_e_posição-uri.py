n = int(input())
x = [len(range(n))]
for i in x:
    x = [int(i) for i in input().split()]
print(f"Menor valor: {min(x)}")
print(f"Posicao: {x.index(min(x))}")

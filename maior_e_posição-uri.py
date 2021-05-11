lista = []
for i in range(0, 100):
    n = int(input())
    lista.append(n)
print(max(lista))
print(lista.index(max(lista)) + 1)

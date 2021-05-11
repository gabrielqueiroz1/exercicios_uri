pos = soma = 0
for i in range(0, 6):
    n = float(input())
    if n > 0:
        pos += 1
        soma += n
media = soma/pos
print(f"{pos} valores positivos")
print(f"{media:.1f}")

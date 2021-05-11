contP = 0
numeros = []
for i in range(0, 6):
    num = float(input())
    numeros.append(num)
    if numeros[i] > 0:
     contP += 1
print(f"{contP} valores positivos")
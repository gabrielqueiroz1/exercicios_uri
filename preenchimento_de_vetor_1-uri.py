n = int(input())
vet = []
aux = cont = 0
while True:
    if cont == 0:
        vet.append(n)
        print(f"N[{cont}] = {vet[cont]}")

    else:
        aux = vet[-1] * 2
        vet.append(aux)
        print(f"N[{cont}] = {aux}")

    cont += 1
    if cont == 10:
        break

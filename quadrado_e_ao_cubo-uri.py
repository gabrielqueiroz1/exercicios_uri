n = int(input())
cont = 0
for i in range(1, n+1):
    for j in range(1, 4):
        cont += 1
        if cont < 3:
            print(str(i**j), end=" ")
        if cont == 3:
            print(str(i**j).strip())
            cont = 0

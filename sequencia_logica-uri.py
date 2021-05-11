n = int(input())
cont = 0
for i in range(1, n+1):
    for j in range(1, 4):
        for g in range(1, 3):
            cont += 1
            if cont == 1:
                print(str(i), end=" ")
            if cont == 2:
                if j > 2:
                    print(str(i*i+1), end=" ")
                else:
                    print(str(i*i), end=" ")
            if cont == 3:
                if j == 3:
                    print(str(i**j+1).strip())
                else:
                    print(str(i**j*i).strip())
                cont = 0

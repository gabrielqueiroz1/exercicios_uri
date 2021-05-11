n = int(input())
for i in range(n):
    x = int(input())
    primo = True
    for j in range(2, x):
        if x % j == 0:
            primo = False
            break
    if primo:
        print(f"{x} eh primo")
    else:
        print(f"{x} nao eh primo")

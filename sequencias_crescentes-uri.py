x = 1
while x != 0:
    x = int(input())
    for i in range(1, x+1):
        if i < x:
            print(str(i), end=" ")
        if i == x:
            print(str(i).strip())

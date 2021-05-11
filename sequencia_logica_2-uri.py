x, y = [int(i) for i in input().split()]
n = 0
for i in range(1, y + 1):
    n += 1
    if n < x:
        print(i, end=" ")
    if n == x:
        print(str(i).strip())
        n = 0

#ou

x, y = [int(i) for i in input().split()]
n = 0
for i in range(1, y + 1):
    n += 1
    if n < x:
        print("".join(str(i)), end=" ")
    if n == x:
        print("".join(str(i)).strip())
        n = 0

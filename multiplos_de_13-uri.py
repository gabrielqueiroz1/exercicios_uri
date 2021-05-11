x = int(input())
y = int(input())
contN = 0
if x < y:
    for i in range(x, y + 1):
        if i % 13 != 0:
            contN += i
    print(contN)
else:
    for i in range(y, x + 1):
        if i % 13 != 0:
            contN += i
    print(contN)

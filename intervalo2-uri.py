n = int(input())
entreN = 0
entreNot = 0
for i in range(0, n):
    x = int(input())
    if 10 <= x <= 20 and x > 0:
        entreN += 1
    elif 10 != x != 20 and x > 0:
        entreNot += 1

print(f"{entreN} in")
print(f"{entreNot} out")

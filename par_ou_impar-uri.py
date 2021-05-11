n = int(input())
for i in range(0, n):
    num = int(input())
    if num % 2 == 0 and num > 0:
        print("EVEN POSITIVE")
    elif num % 2 == 0 and num < 0:
        print("EVEN NEGATIVE")
    if num % 2 == 1 and num > 0:
        print("ODD POSITIVE")
    elif num % 2 == 1 and num < 0:
        print("ODD NEGATIVE")
    if num == 0:
        print("NULL")

n = int(input())
s = 0
while n > 0:
    X, Y = map(int, input().split())
    if X < Y:
        for i in range(X+1, Y):
            if i % 2 == 1:
                s += i
        print(s)
        s = 0
    if Y < X:
        for i in range(Y+1, X):
            if i % 2 == 1:
                s += i
        print(s)
        s = 0
    if X == Y:
        print("0")
        s = 0
    n -= 1

quant = int(input())
for i in range(0, quant):
    x, y = map(int, input().split())
    try:
        if y == 0:
            print("divisao impossivel")
        else:
            print(x/y)
    except ZeroDivisionError:
        print("0.0")

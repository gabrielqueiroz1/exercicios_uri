g = []
n = 0
while True:
    try:
        n = int(input())
        g.append(n)
        if len(g) == 10:
            break
    except EOFError:
        break
for i, x in enumerate(g):
    if x <= 0:
        x = 1
    print(f"X[{i}] = {x}")

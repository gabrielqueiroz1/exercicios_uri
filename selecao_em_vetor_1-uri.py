g = []
n = 0
while True:
    try:
        n = float(input())
        g.append(n)
        if len(g) == 100:
            break
    except EOFError:
        break
for i, x in enumerate(g):
    if x <= 10:
        print(f"A[{i}] = {x}")

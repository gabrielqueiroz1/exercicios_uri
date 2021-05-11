n = int(input())
c = 1
v = 0
for i in range(0, n):
    print(f"{c} {c+1} {c+2} PUM")
    v += 3
    if v == 3:
        v = 0
        c += 4

x = int(input())
y = int(input())
resto_div = []
if y > x:
    for j in range(x+1, y):
        if j % 5 == 2 or j % 5 == 3:
            resto_div.append(j)
else:
    if x > y:
        for i in range(y+1, x):
            if i % 5 == 2 or i % 5 == 3:
                resto_div.append(i)

for g in sorted(resto_div):
    print(g)

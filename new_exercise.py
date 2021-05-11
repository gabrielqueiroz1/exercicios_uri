n = int(input())
parts_n = str(n)
s = 0
qbr = []
for i in parts_n:
    i = int(i)
    if i % 3 == 0:
        s += i
        qbr.append(i)
qbr = ''.join(map(lambda x: str(x), qbr))
qbr = int(qbr)
s1 = qbr + s

print(s1)

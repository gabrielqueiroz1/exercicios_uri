k = 0
j = 7
c = 0
trava = 0
while c < 3 and trava < 15:
    print(f"I={k+1} J={j}")
    j -= 1
    c += 1
    trava += 1
    if c == 3:
        c = 0
        k += 2
        j += 5

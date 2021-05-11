k = 0
j = 1
c = 0
trava = 0
while c < 3 and trava < 33:
    print(f"I={k:g} J={j:g}") #:g é como se fosse um float "resumido"
    j += 1
    c += 1
    trava += 1
    if c == 3:
        j -= 3
        c = 0
        k += 0.2
        j += 0.2

alc = gas = die = 0
while True:
    c = int(input())
    if 1 <= c <= 4:
        if c == 1:
            alc += 1
        if c == 2:
            gas += 1
        if c == 3:
            die += 1
        if c == 4:
            break
print("MUITO OBRIGADO")
print(f"Alcool: {alc}\n"
      f"Gasolina: {gas}\n"
      f"Diesel: {die}")

n = float(input(""))
aum = 0
reaj = 0
porc = 0
if n <= 400:
    aum = n * 1.15
    reaj = aum - n
    porc = 15

elif 400.01 <= n <= 800:
    aum = n * 1.12
    reaj = aum - n
    porc = 12

elif 800.01 <= n <= 1200:
    aum = n * 1.10
    reaj = aum - n
    porc = 10

elif 1200.01 <= n <= 2000:
    aum = n * 1.07
    reaj = aum - n
    porc = 7

elif n > 2000:
    aum = n * 1.04
    reaj = aum - n
    porc = 4

print("Novo salario: {:.2f}".format(aum))
print("Reajuste ganho: {:.2f}".format(reaj))
print("Em percentual: {} %".format(porc))

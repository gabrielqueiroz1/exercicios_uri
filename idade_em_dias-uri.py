idade = int(input())
ano = mes = dia = 0
while idade > 0:
    if idade >= 365:
        ano += 1
        idade -= 365
    if idade >= 30:
        mes += 1
        idade -= 30
    if idade > 0:
        dia += 1
        idade -= 1
print(f"{ano} ano(s)")
print(f"{mes} mes(es)")
print(f"{dia} dia(s)")

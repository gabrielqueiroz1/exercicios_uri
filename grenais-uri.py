inter_win = gremio_win = emp = maior_vencedor = contG = 0
esc = 1
while esc != 2:
    if esc == 1:
        x, y = [int(i) for i in input().split()]
        if x > y:
            inter_win += 1
            contG += 1
        elif y > x:
            gremio_win += 1
            contG += 1
        else:
            emp += 1
            contG += 1
    esc = int(input("Novo grenal (1-sim 2-nao)\n"))
print(f"{contG} grenais")
print(f"Inter:{inter_win}")
print(f"Gremio:{gremio_win}")
print(f"Empates:{emp}")
if inter_win > gremio_win:
    print("Inter venceu mais")
elif gremio_win > inter_win:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")

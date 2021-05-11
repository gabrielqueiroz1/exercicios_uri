hora_inicial, hora_final = map(int, input().split())

if hora_inicial > hora_final:
    nova_hora = (24 - hora_inicial) + hora_final
    print(f"O JOGO DUROU {nova_hora} HORA(S)")
elif hora_inicial < hora_final:
    nova_hora = hora_final - hora_inicial
    print(f"O JOGO DUROU {nova_hora} HORA(S)")
else:
    nova_hora = 24
    print(f"O JOGO DUROU {nova_hora} HORA(S)")

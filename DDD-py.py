dic_ddd = {61: "Brasilia", 71: "Salvador", 11: "Sao Paulo", 21: "Rio de Janeiro", 32: "Juiz de Fora", 19: "Campinas",
           27: "Vitoria", 31: "Belo Horizonte"}

sel_ddd = int(input())

if sel_ddd in dic_ddd:
    print(dic_ddd[sel_ddd])
else:
    print("DDD nao cadastrado")

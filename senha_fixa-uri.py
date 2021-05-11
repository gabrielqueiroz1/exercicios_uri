senha_fixa = 2002
correto = 0
while correto != 1:
    tentativa_senha = int(input())
    if tentativa_senha == senha_fixa:
        print("Acesso Permitido")
        break
    else:
        print("Senha Invalida")

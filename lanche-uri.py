cod_prod = int(input("Digite o código do alimento: "))
quant_prod = int(input("Qual será a quantidade? "))

if cod_prod == 1:
    cod_prod = 4
    total = cod_prod * quant_prod
    print("Total: R$ {:.2f}".format(float(total)))

elif cod_prod == 2:
    cod_prod = 4.5
    total = cod_prod * quant_prod
    print("Total: R$ {:.2f}".format(float(total)))

elif cod_prod == 3:
    cod_prod = 5
    total = cod_prod * quant_prod
    print("Total: R$ {:.2f}".format(float(total)))

elif cod_prod == 4:
    cod_prod = 2
    total = cod_prod * quant_prod
    print("Total: R$ {:.2f}".format(float(total)))

elif cod_prod == 5:
    cod_prod = 1.5
    total = cod_prod * quant_prod
    print("Total: R$ {:.2f}".format(float(total)))

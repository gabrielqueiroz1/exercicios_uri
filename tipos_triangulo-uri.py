a, b, c = [float(i) for i in input().split()]
if a + b > c and a + c > b and c + b > a:
    if a == b and a == c and b == c: #poderíamos escrever assim: r1 == r2 == r3:
        print("TRIANGULO EQUILATERO"
              "TRIANGULO ACUTANGULO")

    elif a == b != c or a == c != b or b == c != a:
        print("Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES")

    elif a != b and a != c and b != c: #poderíamos escrever assim: r1 != r2 != r3 != r1:
        print("Os segmentos acima PODEM FORMAR um triângulo ESCALENO")

else:
    print("NAO FORMA TRIANGULO")

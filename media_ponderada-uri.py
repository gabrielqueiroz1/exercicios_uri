quant_nota = int(input())
for i in range(0, quant_nota):
    n1, n2, n3 = map(float, input().split())
    media = (n1*0.2)+(n2*0.3)+(n3*0.5)
    print("{:.1f}".format(media))

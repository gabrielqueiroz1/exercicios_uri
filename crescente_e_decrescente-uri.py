def crescenteDecrescente():
    x = 0
    y = 1
    while x != y:
        x, y = map(int, input().split())

        if x > y:
            print("Decrescente")

        elif y > x:
            print("Crescente")
crescenteDecrescente()
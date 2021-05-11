A, B, C = map(float, input().split())

if A + B > C and A + C > B and B + C > A:
    peri = A + B + C
    print(f"Perimetro = {peri:.1f}")
else:
    area = ((A + B) / 2) * C
    print(f"Area = {area:.1f}")

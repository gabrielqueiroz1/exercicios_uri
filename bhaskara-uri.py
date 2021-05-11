from math import sqrt
A, B, C = [int(i) for i in input().split()]
r1 = r2 = 0
try:
    form = (B ** 2) - (4 * A * C)
    r1 = (- B + (sqrt(form))) / (2 * A)
    r2 = (- B - (sqrt(form))) / (2 * A)

    if r1 != 0 and r2 != 0 or r1 < 0 and r2 < 0:
        print("R1 = {:.5f}".format(r1))
        print("R2 = {:.5f}".format(r2))
except ZeroDivisionError:
    if r1 <= 0 or r2 <= 0 or A <= 0 or B <= 0 or C <= 0:
        print("Impossivel calcular")
except ValueError:
    print("Impossivel calcular")

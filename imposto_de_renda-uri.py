renda = float(input())

if renda <= 2000:
    print("Isento")

elif 2000.01 <= renda <= 3000:
    nova_renda = 0.08 * (renda - 2000)
    print(f"R$ {nova_renda:.2f}")
elif 3000.01 <= renda <= 4500:
    nova_renda = (0.08 * 1000) + (0.18 * (renda - 3000))
    print(f"R$ {nova_renda:.2f}")
else:
    nova_renda = (0.08 * 1000) + (0.18 * 1500) + (0.28 * (renda - 4500))
    print(f"R$ {nova_renda:.2f}")

c = r = s = tot_cob = 0

def percentual(x):
    perc = (x * 100) / tot_cob
    return perc

n = int(input())

for i in range(0, n):
    q, esc = map(str, input().split())
    q = int(q)
    esc = esc.upper()
    if esc == 'C':
        c += q
        tot_cob += q
    if esc == 'R':
        r += q
        tot_cob += q
    if esc == 'S':
        s += q
        tot_cob += q
print(f"Total: {tot_cob} cobaias")
print(f"Total de coelhos: {c}")
print(f"Total de ratos: {r}")
print(f"Total de sapos: {s}")
print(f"Percentual de coelhos: {percentual(c):.2f} %")
print(f"Percentual de ratos: {percentual(r):.2f} %")
print(f"Percentual de sapos: {percentual(s):.2f} %")

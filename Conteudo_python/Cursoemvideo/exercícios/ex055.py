v = []

for c in range(1, 6):
    n = int(input(("Digite seu peso: ")))
    v.append(n)
    maior = v[0]
    menor = v[0]
if v[1] > maior:
    maior = v[1]
if v[2] > maior:
    maior = v[2]
if v[3] > maior:
    maior = v[3]
if v[4] > maior:
    maior = v[4]
if v[1] < menor:
    menor = v[1]
if v[2] < menor:
    menor = v[2]
if v[3] < menor:
    menor = v[3]
if v[4] < menor:
    menor = v[4]
print("Maior: ", maior)
print("Menor: ", menor)

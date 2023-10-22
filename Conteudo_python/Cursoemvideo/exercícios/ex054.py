from datetime import date
v = []
z = 0
count = 0
b = 0

for c in range(1, 8):
    n = int(input(("Qual é seu ano de nascimento: ")))
    v.append(n)
for var in range(z, 7, 1):
    a = date.today().year - v[z]
    z += 1
    if a >= 21:
        count += 1
    else:
        b += 1
print(count, "pessoas já são maiores de idade\n",
            b,"pessoas ainda não são maiores de idade")

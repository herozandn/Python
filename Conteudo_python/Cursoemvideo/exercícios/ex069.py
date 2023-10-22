c = 0
h = 0
m = 0

while True:
    print("-" * 30)
    print("CADASTRE UMA PESSOA")
    print("-" * 30)
    i = int(input("Idade: "))
    if i > 18:
        c += 1
    s = str(input("Sexo: [M/F] ")).upper()
    while s not in "MF":
        s = str(input("Sexo: [M/F] ")).upper()
    if s == "M":
        h += 1
    if s == "F" and i < 20:
        m += 1
    e = str(input("Quer continuar? [S/N] ")).upper()
    while e not in "SN":
        e = str(input("Quer continuar? [S/N] ")).upper()
    if e == "N":
        break

print("="*5, end=" ")
print("FIM DO PROGRAMA", end=" ")
print("="*5)

print(f"Total de pessoas com mais de 18 anos: {c}")
print(f"Ao todo temos {h} homens cadastrados")
print(f'E temos {m} mulheres com menos de 20 anos')
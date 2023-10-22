si = 0
mi = 0
mih = 0
nv = " "
m = 0
for c in range(0, 4):
    n = str(input("Digite seu nome: ")).strip()
    i = int(input("Digite sua idade: "))
    s = str(input("[M] para \033[34mhomens\033[m \n[F] para \033[36mmulheres\033[m\n")).strip()
    si += i
    if c == 1 and s in "Mm":
        mih = i
        nv = n
    if s in "Mm" and i > mih:
        mih = i
        nv = n
    if s in "Ff" and i > 20:
        m += 1
mi = si / 4
print("A média de idade do grupo é de", mi, "anos")
print("O homem mais velho tem", mih, "anos e se chama", nv)
print("São", m, "mulheres com mais de 20 anos")
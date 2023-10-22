t, m, c, menor = 0
barato = " "

print("-" * 30)
print("LEITOR DE PREÇOS")
print("-" * 30)

while True:
    n = str(input("Nome do produto: "))
    p = float(input("Preço: "))
    t += p
    if p > 1000:
        m += 1
    c += 1
    if c == 1 or p < menor:
        menor = p
        barato = n
    e = str(input("Quer continuar? [S/N] ")).upper()
    if e == "N":
        break

print("-"*5, end=" ")
print("FIM DO PROGRAMA", end=" ")
print("-"*5)
print(f"O total da compra foi R${t:.2f}")
print(f"Temos {m} produtos custando mais de R$1000.00")
print(f'O produto mais barato foi {barato} que custa R${p:.2f}')

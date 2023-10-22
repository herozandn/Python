d = float(input("Qual foi a distância da viagem em km: "))
if d <= 200:
    t = d * 0.5
    print("O preço da viagem é R${:.2f}" .format(t))
if d > 200:
    t = d * 0.45
    print("O preço da viagem é RS{:.2f}" .format(t))

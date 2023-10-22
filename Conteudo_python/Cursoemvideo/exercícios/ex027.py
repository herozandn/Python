n = str(input("Digite seu nome: ")).strip()
n = n.split()
print("Seu primeiro nome é: {}". format(n[0].capitalize()))
print("Seu último nome é: {}". format(n[len(n)-1]).capitalize())

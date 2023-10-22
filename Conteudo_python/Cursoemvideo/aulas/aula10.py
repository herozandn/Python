nome = str(input("Qual é o seu nome: ")).capitalize()
if nome == "Henrique":
    print("Que nome lindo você tem")
else:
    print("Que nome comum")
print("Bom dia, {}".format(nome))

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1+n2)/2
print("A sua média é {:.1f}".format(m))
if m >= 6.0:
    print("Sua média foi boa!!")
else:
    print("Sua média foi ruim")
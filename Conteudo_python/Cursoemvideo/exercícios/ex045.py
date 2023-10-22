import random
from time import sleep
print("-*"*12)
print("PEDRA, PAPEL, TESOURA")
print("-*"*12)

a = 1
u = str(input("Escolha entre 'pedra', 'papel' e 'tesoura': "))
sleep(a)
print("PEDRA")
sleep(a)
print("PAPEL")
sleep(a)
print("TESOURA")
l = ["pedra", "papel", "tesoura"]
e = random.choice(l)
if u == "pedra" and e == "papel" or u == "papel" and "tesoura" or u == "tesoura" and e == "pedra":
    print("{} \033[31mPERDE\033[m para {}\nEu ganhei".format(u, e))
elif u == "pedra" and e == "tesoura" or u == "papel" and e == "pedra" or u == "tesoura" and e == "papel":
    print("{} \033[33mGANHA\033[m de {}\nVocê ganhou".format(u, e))
else:
    print("{} com {} é empate".format(u, e))

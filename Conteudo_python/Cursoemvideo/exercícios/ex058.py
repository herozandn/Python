import random
from time import sleep

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
atraso = 1
escolha = random.choice(numeros)
usuario = ""
c = 0

print("TENTE ACERTAR O NÚMERO ESCOLHIDO PELO COMPUTADOR")
sleep(atraso)

while usuario != escolha:
    usuario = int(input("Escolha um número entre 0 e 10: "))
    c += 1
    if usuario > escolha:
        print("Menos... O número é menor")
    elif usuario < escolha:
        print("Mais... O número é maior")
print("O número escolhido foi\033[32m", escolha, "\033[m\nVocê precisou de\033[36m", c, "\033[mchances para acertar")

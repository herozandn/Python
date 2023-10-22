import random
from time import sleep
numeros = [0,5]
atraso = 1
escolha = random.choice(numeros)
print("TENTE ACERTAR O NÚMERO ESCOLHIDO PELO COMPUTADOR")
sleep(atraso)
usuario = int(input("Escolha um número entre 0 e 5: "))
if escolha == usuario:
    print("Você venceu!!\nPARABÉNS")
else:
    print("Você perdeu\nMais sorte da próxima vez!!")

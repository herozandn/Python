import random
from time import sleep
sorteio = []

num = int(input('Insira o número de sorteios: '))
for i in range(num):
    linha = []
    for j in range(6):
        a = random.randint(1, 60)
        if a not in linha:
            linha.append(a)
            linha.sort()
    sorteio.append(linha)

print('-='*5, end=' ')
print(f'SORTEANDO {num} JOGOS', end=' ')
print('-='*5)

for c, val in enumerate(sorteio, start=1):
    print(f'Jogo {c}: {val}')
    sleep(1)
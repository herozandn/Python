from time import sleep
from random import randint

dic = {}

print('Valores sorteados')

for i, c in enumerate(range(0, 4), start=1):
    r = randint(1, 6)
    dic[f'Jogador {i}'] = r

for k, v in dic.items():
    print(f'{k} tirou \033[35m{v}\033[m')
    sleep(1)

print('Ranking dos Jogadores: ')
for v, i in enumerate(sorted(dic, key = dic.get, reverse = True), start=1):
    print(f'{v}° lugar: {i} com \033[35m{dic[i]}\033[m')
    sleep(1)
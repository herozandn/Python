dic = {}
lista = []

dic['nome'] = str(input('Nome do jogador: ')).capitalize()
partidas = int(input('Quantas partidas ele jogou? '))

for gol in range(partidas):
    gols = int(input(f'Quantos gols na partida {gol+1}? '))
    lista.append(gols)

dic['gols'] = lista
dic['total'] = sum(lista)
print('-='*30)
print(dic)
print('-='*30)

for c, v in dic.items():
    print(f'O campo {c} tem o valor de {v}.')
print('-='*30)

print(f'O jogador {dic["nome"]} jogou {partidas} partidas')

for a, b in enumerate(lista, start=1):
    print(f'   => Na partida {a}, fez {b} ', end='')
    print('gols') if b > 1 or b == 0 else print('gol')
print(f'Foi um total de {dic["total"]} gols')
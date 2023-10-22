dic = {}
lista = []
geral = []

while True:
    dic['nome'] = str(input('Nome do jogador: ')).capitalize()
    partidas = int(input(f'Quantas partidas {dic["nome"]} jogou? '))
    lista.clear()
    for gol in range(partidas):
        lista.append(int(input(f'Quantos gols na partida {gol+1}? ')))
    dic['gols'] = lista[:]
    dic['total'] = sum(lista)
    geral.append(dic.copy())

    res = str(input('Quer continuar? [S/N] ')).capitalize()
    while res not in "SN":
        res = str(input('Quer continuar? [S/N] ')).capitalize()
    if res == "N":
        break

print('-='*30)
print(f'{"cod":<4}{"nome":<8}{"gols":<12}{"total":<16}')
print('-'*55)

for k, v in enumerate(geral):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*30)

while True:
    print('-'*35)
    jogador = int(input('Mostrar notas de qual jogador? (999 interrompe): '))
    if jogador == 999:
        print('FINALIZANDO...')
        break
    elif jogador <= len(geral) - 1:
        print(f'-- LEVANTAMENTO DO JOGADOR {geral[jogador]["nome"]}')
        for a, b in enumerate(lista, start=1):
            print(f'   => Na partida {a}, fez {b} ', end='')
            print('gols') if b > 1 or b == 0 else print('gol')
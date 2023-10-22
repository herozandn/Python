def ficha(nome='<desconhecido>', gol=0):
    print(f'O jogador {nome} marcou {gol} gols')



nome = input('Nome do jogador: ').capitalize()
gol = str(input('Gols marcados: '))

if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    ficha(gol=gol)
else:
    ficha(nome, gol)



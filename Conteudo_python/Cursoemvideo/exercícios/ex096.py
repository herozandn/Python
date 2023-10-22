print('Controle de terrenos')
print('-' * 30)

def area(lar, com):
    tot = lar * com
    print(f'A área de um terreno de {lar} x {com} é de {tot}m².')


area(lar = float(input('Largura (m): ')), com = float(input('Comprimento (m): ')))

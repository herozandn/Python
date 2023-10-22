matriz = []

#programa matriz
for i in range(3):
    linha = []
    for j in range(3):
        val = int(input(f'Digite um valor para as coordenadas [{i+1, j+1}]: '))
        linha.append(val)
    matriz.append(linha)
print('-='*50)

#vizualização
for p in matriz:
    i = 0
    while i < 3:
        print(f'[{p[i]:^5}]', end='')
        i += 1
    if i == 3:
        print('')

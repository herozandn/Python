matriz = []
soma = coluna = mai = 0

#programa matriz
for i in range(3):
    linha = []
    for j in range(3):
        val = int(input(f'Digite um valor para as coordenadas [{i+1, j+1}]: '))
        linha.append(val)

        #soma dos pares
        if val % 2 == 0:
            par = val
            soma += par

        #soma da terceira coluna
        if j == 2:
            ter = val
            coluna += ter

    matriz.append(linha)

#maior da segunda linha
for val in matriz[1]:
    if len(matriz[1]) == 0:
        mai = val
    else:
        if val > mai:
            mai = val

print('-='*50)

#vizualização
for p in matriz:
    i = 0
    while i < 3:
        print(f'[  {p[i]}  ]', end=' ')
        i += 1
    if i == 3:
        print('')

print('-='*50)
print(f'A soma dos números pares é {soma}')
print(f'A soma dos elementos da terceira coluna é {coluna}')
print(f'O maior valor da segunda linha é {mai}')
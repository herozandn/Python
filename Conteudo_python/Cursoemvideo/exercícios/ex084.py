pessoas = list()
dados = list()
mai = men = 0

while True:

    #entrada
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))

    #maior e menor
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        elif dados[1] < men:
            men = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    #condição de parada
    r = str(input('Continuar? [S/N]'))
    if r in 'Nn':
        break
    while r not in 'SsNn':
        r = str(input('Continuar? [S/N]'))

print('='*50)
print(len(pessoas), 'pessoas foram cadastradas')
print(f'O maior peso cadastrado foi \033[38m{mai}\033[mkg', end=' ')
for p in pessoas:
    if p[1] == mai:
        print(f'{p[0]}')
print(f'O menor peso cadastrado foi \033[39m{men}\033[mkg', end=" ")
for p in pessoas:
    if p[1] == men:
        print(f'{p[0]}')

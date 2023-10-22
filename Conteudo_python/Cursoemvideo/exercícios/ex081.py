lista = []
cont = 0

while True:
    val = int(input('Digite um valor: '))
    r = str(input("Quer continuar? [S/N] "))
    lista.append(val)
    cont += 1
    if r in 'Nn':
        break
print(f'Foram digitados {cont} números')
lista.sort(reverse=True)
print(f'A lista em ordem decrenscente {lista}')
if 5 in lista:
    print('5 está na lista')
else:
    print('5 não está na lista')

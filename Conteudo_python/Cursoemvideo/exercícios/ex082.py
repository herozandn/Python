r = ' '
lista = []
lista_par = []
lista_impar = []

while True:
    val = int(input('Digite um valor: '))
    r = str(input("Quer continuar? [S/N] ")).upper()
    lista.append(val)
    if val % 2 == 0:
        lista_par.append(val)
    else:
        lista_impar.append(val)
    if r == 'N':
        break

print('Os valores digitados foram', end=" ")
for val in lista:
    print(f'{val}', end=" ")
print('\n')
print('Os valores pares digitados foram', end=" ")
for v in lista_par:
    print(f'{v}', end=" ")
print('\n')
print('Os valores ímpares digitados foram', end=" ")
for va in lista_impar:
    print(f'{va}', end=" ")

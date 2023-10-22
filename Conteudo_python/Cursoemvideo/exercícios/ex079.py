r = 'S'
v = list()

while True:
    v.append(int(input("Digite um valor: ")))
    r = str(input("Deseja continuar... [S/N] ")).upper()
    if r == 'N':
        break
print('=-'*50)
lista = list(set(v)) # remove valores repetidos
lista.sort() # coloca em ordem crescente a lista
print(f'Você digitou os valores {lista}')
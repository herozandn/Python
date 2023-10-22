n = [2, 5, 9, 1]
n[2] = 2
n.append(7) #adiciona valor
n.sort() #coloca em ordem cescente
len(n) #tamanho da lista
n.insert(2, 0) #insere um valor em uma posição
#n.pop() #exclui o último valor
if 5 in n:
    n.remove(5) #remove um valor
    print(n)
else:
    print("Não achei o 5")

"""v = list()
for cont in range(0, 5):
    v.append(int(input("Digite um valor: ")))

for c, val in enumerate(v):
    print(f"Na posição {c}, achei o valor {val}")"""

a = [2, 3, 5, 9]
b = a[:] #cópia de listas
b[2] = 'a'
print(f'Lista A: {a}')
print(f'Lista B: {b}')
lanches = "hambúrguer", "suco", "pizza", "pudim"
print(lanches[2])
print(lanches[1:3])
print(lanches[1:])
print(lanches[-1:])
print(len(lanches))

for c in enumerate(lanches):
    print(c, end="")
    print("," if c != "pudim" else "", end=" ")

for cont in range(0, len(lanches)):
    print(lanches[cont])

print(sorted(lanches)) #mostra a tupla em ordem alfabética

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c.count(0)) #quantas vezes aparece um determinado elemento
print(c.index(5)) #em posição está um determinado elemento
del(lanches) #comando de deleção
p = ("Leite", 6.60, "Carne", 20.65, "Ovo", 16.63, "Pão", 14.50, "Azeite", 30.65, "Açúcar", 9.63, "Arroz", 10.98, "Feijão", 9.69)

print("-"*50)
print("{:^50}".format("LISTAGEM DE COMPRAS"))
print("-"*50)

c = 0
while True:
    print(p[c], end=" ")
    c += 1
    print("R$", end="")
    print(p[c])
    c += 1
    if c == 16:
        break
print("-"*50)
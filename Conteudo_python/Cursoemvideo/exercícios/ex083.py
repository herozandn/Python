lista = list()

a = str(input("Digite uma expressão: "))
lista.append(a)
b = a.count("(")
c = a.count(")")
if b == c:
    print('Operação válida')
else:
    print('Operação inválida')
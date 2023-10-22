lista = []

for count in range(5):
    v = (int(input("Digite um valor: ")))
    if count == 0 or v > lista[-1]:
        lista.append(v)
    else:
        pos = 0
        while pos < len(lista):
            if v <= lista[pos]:
                lista.insert(pos, v)
                break
            pos += 1
print('='*50)
print(f'Os valores em ordem foram {lista}')
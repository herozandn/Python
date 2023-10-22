v = []
mai = men = 0

for c in range(0, 5):
    v.append(int(input(f"Digite um valor na posição {c}: ")))
    if c == 0:
        mai = men = v[c]
    else:
        if v[c] > mai:
            mai = v[c]
        if v[c] < men:
            men = v[c]

print("=-"*50)
print(f'Você digitou os valores {v}')
print(f'O maior valor foi {mai}, nas posições', end=" ")

for val, i in enumerate(v):
    if i == mai:
        print(f'{val}')

print(f"O menor valor foi {men}, nas posições", end=' ')

for val, i in enumerate(v):
    if i == men:
        print(f'{val}', end=' ')

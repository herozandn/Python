"""
def soma(a, b):
    print(f'A soma de {a} com {b} é igual a', end=' ')
    s = a + b
    print(s)


soma(2, -1)
soma(5, 8)
soma(2, 5)
soma(4, 0)
"""
'''
def contador(*num):
    for valor in num:
        print(f'{valor}', end=' ')
    print()
    tam = len(num)
    print(f'Os valores {num} {tam}')


contador(5, 6, 3)
contador(6, 3)
contador(2, 6, 8, 2, 41)
'''

def dobra(lis):
    pos = 0
    while pos < len(lis):
        lis[pos] *= 2
        pos += 1


val = [2, 6, 3, 5, 4, 0]
dobra(val)
print(val)


def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(s)

soma(2, 6)
soma(2, 3, 6, 4)

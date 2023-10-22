# interactive help
help(print)

print(input.__doc__)

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: vazio
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print()


contador(2, 10, 2)
help(contador)

# parametro opcional
def somar(a, b, c=0):
    s = a + b + c
    print(f'A soma vale {s}')


somar(2, 6, 3)
somar(2, 6)
print()

#escopo de variável
'''
def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


n = 2
print(f'No programa principal, n vale {n}')
teste()
print(f'No programa principal, x vale {x}')
'''

'''
def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
funcao()
print(f'N1 fora vale {n1}')
'''

def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste(a)
print(f'A fora vale {a}')


def somar2(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar2(2, 6, 3)
r2 = somar2(2, 3)
r3 = somar2(1)
print(f'Meus cálculos são {r1}, {r2}, {r3}')

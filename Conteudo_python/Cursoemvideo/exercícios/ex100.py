import random

def sorteio():
    num = random.sample(range(1, 10), 5)
    return num

def soma():
    s = 0
    for n in num:
        if n % 2 == 0:
            s += n
    return s

num = sorteio()
res = soma()
print(f'Sorteando os 5 valores da lista: {num}')
print(f'A soma dos pares de {num} é {res}')

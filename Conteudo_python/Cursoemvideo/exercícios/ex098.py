import time as tm

def contagem(i, f, p):
    print('-='*20)
    print(f'Contagem de {i} até {f} de {abs(p)} em {abs(p)}')
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            cont += p
            tm.sleep(0.5)
        print()
    elif i > f:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            cont -= abs(p)
            tm.sleep(0.5)
        print()


contagem(1, 10, 1)
contagem(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contagem(ini, fim, pas)

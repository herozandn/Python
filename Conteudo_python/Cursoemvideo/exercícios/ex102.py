def fatorial(n, show=False):
    if n == 0 or n == 1:
        return f'O fatorial de {n} é 1'
    elif n < 0:
        return 'Erro'
    else:
        f = 1
        for c in range(n, 0, -1):
            if show:
                print(c, end=' ')
                if c > 1:
                    print('x', end=' ')
                else:
                    print('=', end=' ')
            f *= c
        print(f)


fatorial(90, show=True)
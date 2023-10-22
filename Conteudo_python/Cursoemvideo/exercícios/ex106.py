def ajuda(f):
    help(f)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print('~'*tam)
    print(f'{  msg}')
    print('~'*tam)


while True:
    f = str(input('Biblioteca ou função > '))
    if f.upper() == 'FIM':
        break
    else:
        ajuda(f)


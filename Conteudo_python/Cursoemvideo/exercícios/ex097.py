def escrever(txt):
    pos = 0
    while pos < len(txt):
        print('-', end='')
        pos += 1
    print()
    print(txt)
    print('-'*pos)

escrever('Olá, mundo')
escrever('Henrique Zanchin')
escrever('                        ')
escrever('Oi')
def maior(*num):
    print('-='*20)
    print('Analisando os valores passados...')
    for b in num:
        print(b, end=' ')
    print(f'Foram digitados \033[34m{len(num)}\033[m valores ao todo.')
    if len(num) != 0:
        mai = num[0]
        for e in num:
            if e > mai:
                mai = e
        print(f'O maior valor é \033[35m{mai}\033[m')
    else:
        print(f'O maior volar é \033[35m{len(num)}\033[m')


maior(2, 6, 9, 5, 2)
maior(2, 6, 5, 4)
maior()
maior(0)
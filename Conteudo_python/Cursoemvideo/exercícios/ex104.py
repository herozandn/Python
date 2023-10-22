def leiaInt():
    print('-'*20)
    while True:
        car = input('Digite um número: ')
        x = car.isnumeric()
        if x == 0:
            print('Erro')
        else:
            print(f'Você digitou o número {car}')
            break


leiaInt()

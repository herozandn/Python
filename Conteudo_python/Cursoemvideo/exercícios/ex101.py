def voto(n):
    import datetime as dt
    tem = dt.date.today().year - n
    print(f'{tem}:', end=' ')
    if tem < 16:
        return 'VOTO NEGADO'
    elif 16 <= tem <= 18 or tem > 65:
        return 'VOTO FACULTATIVO'
    else:
        return 'VOTO OBRIGATÓRIO'


print(voto(2008))

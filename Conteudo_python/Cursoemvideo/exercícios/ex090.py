dic = {}
dic['Nome'] = str(input('Nome: '))
dic['Media'] = float(input('Média: '))
if dic['Media'] >= 7.0:
    dic['Situação'] = 'Aprovado'
else:
    dic['Situação'] = 'Reprovado'

for k, v in dic.items():
    print(f'{k} é igual a {v}')
from datetime import datetime

dic = {}

dic['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
dic['idade'] = datetime.now().year - ano
dic['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
while dic['ctps'] == 0:
    break
else:
    cont = int(input('Ano de contratação: '))
    dic['contratação'] = cont
    dic['salário'] = float(input('Salário: R$'))
    dic['aposentadoria'] = dic["idade"] + ((dic["contratação"] + 35) - datetime.now().year)

for k, v in dic.items():
    print(f' - {k} tem valor {v}')
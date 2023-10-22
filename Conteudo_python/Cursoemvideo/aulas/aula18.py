dados = list()
dados.append('Pedro')
dados.append(25)
pessoas = list()
pessoas.append(dados[:])
dados[0] = 'Maria'
dados[1] = 23
pessoas.append(dados[:])
print(pessoas)

galera = [['João', 14], ['Pedro', 12], ['Henrique', 45], ['Nicole', 52]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')

pessoal = list()
dado = list()
totmai = totmen = 0

while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    pessoal.append(dado[:])
    dado.clear()

    for p in pessoal:
        if p[1] >= 21:
            print(f'{p[0]} é maior de idade')
            totmai += 1
        else:
            print(f'{p[0]} é menor de idade')
            totmen += 1
    print(f'{totmai} maiores e {totmen} menores')
    r = str(input('Continuar? [S/N] '))
    if r in 'Nn':
        break

"""pessoas.append(dados[:])
print(pessoas)

pessoas = [['Pedro', 25], ['Maria', 19], ['Kaio', 20]]
               #0    #1      #0     #1      #0    #1
                  #0             #1            #2
print(pessoas)

print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])"""
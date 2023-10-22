filme = {'título': 'Star Wars',
        'ano': '1977',
        'diretor': 'George Lucas'
}
print(filme.values())
print(filme.keys())
print(filme.items())

for k, v in filme.items():
    print(f'O {k} é {v}')

locadora = []
locadora.append(filme)
print(locadora[0]['ano'])
print(locadora[0]['título'])
print('\n')

pessoas = {'nome': 'Gustavo', 'sexo': 'M', "idade": '23'}
pessoas['peso'] = '98.5'
for k, v in pessoas.items():
    print(f"{k} = {v}")

brasil = []
estado = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado)
brasil.append(estado2)
print(brasil[1]['sigla'])

est = {}
brasil = []
for c in range(3):
    est['uf'] = str(input('Unidade Federatriva: '))
    est['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(est.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
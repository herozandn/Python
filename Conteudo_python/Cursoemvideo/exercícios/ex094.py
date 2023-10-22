grupo = []
pessoa = {}
soma_idade = media_idade = 0

while True:
    pessoa['nome'] = str(input('Nome: ')).capitalize()
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).capitalize()
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).capitalize()

    pessoa['idade'] = int(input('Idade: '))
    grupo.append(pessoa.copy())

    soma_idade += pessoa["idade"]
    media_idade = soma_idade / len(grupo)

    res = str(input('Quer continuar? [S/N] ')).capitalize()
    while res not in "SN":
        res = str(input('Quer continuar? [S/N] ')).capitalize()
    if res == "N":
        break

mulher = [pessoa["nome"] for pessoa in grupo if pessoa["sexo"] == "F"]

print('-='*20)
print(f'- O grupo tem {len(grupo)} pessoas.')
print(f'- A média de idade é {media_idade:.2f} anos')
print('- As mulheres cadastradas foram: ', end='')
for gente in mulher:
    print(gente, end=' ')

print()
print('- Lista das pessoas que estão acima da média:')

for pessoa in grupo:
    if pessoa["idade"] > media_idade:
        for k, v in pessoa.items():
            print(f'{k} = {v};', end=' ')
        print()
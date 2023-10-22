geral = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    geral.append([nome, [nota1, nota2], media])

    r = str(input('Continuar [S/N]: '))
    while r not in 'SsNn':
        r = str(input('Continuar [S/N]: '))
    if r in 'Nn':
        break

print('-='*25)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*25)
for i, a in enumerate(geral):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-'*35)
    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if aluno == 999:
        print('FINALIZANDO...')
        break
    elif aluno <= len(geral) - 1:
        print(f'Notas de {geral[aluno][0]} são {geral[aluno][1]}')
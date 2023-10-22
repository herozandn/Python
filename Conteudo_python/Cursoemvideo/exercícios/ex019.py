import random
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
l = [a1,a2,a3,a4]
e = random.choice(l) #escolhe um elemento
print('O aluno escolhido foi {}'.format(e))

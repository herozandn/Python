'''a = 5 + 2 #adição
b = 5 - 2 #subtração
c = 5 * 2 #multiplicação
d = 5 / 2 #divisão
e = 5 ** 2 #exponenciação
f = 5 // 2 #divisão inteira
g = 5 % 2 #resto da divisão
print(a, b, c, d, e, f, g,)'''

'''
Ordem de precedência
1 - ()
2 - **
3 - * / // %
4 - + -
'''

'''n = input('Qual é o seu nome?')
print('Prazer em te conhecer {:20}!'. format(n))''' #escreveu o "n" em 20 caracteres

'''n = input('Qual é o seu nome?')
print('Prazer em te conhecer {:>20}!'. format(n))''' #alinhou à esquerda

'''n = input('Qual é o seu nome?')
print('Prazer em te conhecer {:^20}!'. format(n))''' #centralizou

'''n = input('Qual é o seu nome?')
print('Prazer em te conhecer {:=^20}!'. format(n))'''

n1 = int(input('Digite um valor '))
n2 = int(input('Digite outro valor '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {}, a divisão é {:.3} \nA divisão inteira é {} e a exponenciação é {}'.format(s, m, d, di, e))

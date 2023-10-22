"""n = int(input("Digite um número: "))
c = n
f = 1
while c > 0:
    print(f'{c}', end=" ")
    print("x" if c > 1 else " = ", end=" ")
    f *= c
    c -= 1
print(f)"""

n = int(input("Digite um número: "))
f = 1
for c in range(n, 0, -1):
    print(c, end=" ")
    print("x" if c > 1 else "=", end=" ")
    f *= c
print(f)



"""from math import factorial
a = int(input("Digite um número para calcular seu fatorial: "))
print(f'O fatorial de {a} é {factorial(a)}')"""
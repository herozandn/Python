print("="*30)
print("BANCO CEV")
print("="*30)

v = int(input("Que valor você deseja sacar? R$"))

if v // 50 >= 1:
    print(f'Total de {v // 50} cédulas de R$50')
    a = v % 50
if a // 20 >= 1:
    print(f'Total de {a // 20} cédulas de R20')
    b = a % 20
if b // 10 >= 1:
    print(f'Total de {b // 10} cédulas de R$10')
    c = b % 10
if c // 1 >= 1:
    print(f'Total de {c // 1} cédulas de R$1')

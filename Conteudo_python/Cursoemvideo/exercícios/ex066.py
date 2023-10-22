n = c = s = 0
while True:
    n = int(input("Digite um valor (999 para parar): "))
    if n == 999:
        break
    c += n
    s += 1
print(f'A soma dos {s} valores é {c}')
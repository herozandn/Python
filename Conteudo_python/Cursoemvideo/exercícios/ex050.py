s = 0
c = 0
for n in range(1, 7):
    num = int(input("Digite o {} número: ". format(n)))
    if num % 2 == 0:
        s += num
        c += 1
print("A soma de {} números pares é igual a {}".format(c, s))

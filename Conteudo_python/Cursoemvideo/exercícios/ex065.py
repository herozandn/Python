r = "S"
count = 0
a = 0

while r == "S":
    n = int(input("Digite um número: "))
    r = str(input("Quer continuar? [S/N] ")).upper()
    count += n
    a += 1
    m = count / a
    if a == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print("Foram digitados", a, "números e a soma entre eles é", count, "\nA média é", m)
print("O \033[35mmaior\033[m valor é", maior, "e o \033[36mmenor\033[m valor é", menor)
print("FIM")

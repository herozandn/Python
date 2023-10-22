t = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze",
     "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")


p = "S"
while True:
    n = int(input("Digite um número: "))
    while n < 0 or n > 20:
        n = int(input("Digite um número: "))
    print(f"Você digitou o número \033[36m{t[n]}\033[m")
    p = str(input("Deseja continuar? [S/N] ")).upper()
    if p == "N":
        break
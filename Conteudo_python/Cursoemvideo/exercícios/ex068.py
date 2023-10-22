import random

print("=-"*15)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("=-"*15)
c = 0

while True:
    v = int(input("Diga um valor: "))
    d = str(input("Par ou Ímpar? [P/I] ")).upper()
    e = random.randint(0, 10)

    print("-"*30)

    print(f"Você jogou {v} e o computador {e}.", end=" ")
    print(f"Total de {v + e}")

    if (v + e) % 2 == 0:
        print("PAR")
    else:
        print("ÍMPAR")

    print("-"*30)

    a = d == "P" and (v + e) % 2 == 0
    b = d == "I" and (v + e) % 2 != 0

    if a is True:
        print("Você VENCEU!")
        print("Vamos jogar novamente...")
        c += 1
    elif b is True:
        print("Você VENCEU!")
        print("Vamos jogar novamente...")
        c += 1
    else:
        print("Você PERDEU")
        break
print(f"GAME OVER! Você venceu {c} vezes.")

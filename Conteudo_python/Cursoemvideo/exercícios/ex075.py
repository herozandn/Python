n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))
n4 = int(input("Digite um número: "))

t = (n1, n2, n3, n4)
print(f"Você digitou os valores {t}")
print(f"O valor 9 apareceu {t.count(9)}", end="")
print(" vezes" if t.count(9) > 1 else " vez")

if 3 in t:
    print(f"O valor 3 foi digitado na posição {(t.index(3))+1}")
else:
    print("O valor 3 não foi digitado")

print("Os números pares são", end=" ")
for c in t:
    if c % 2 == 0:
        print(c, end=" ")
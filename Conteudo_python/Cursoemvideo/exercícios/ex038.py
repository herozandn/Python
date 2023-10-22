a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

if a > b:
    print("O \033[4;36mprimeiro valor\033[m é \033[35mmaior\033[m")
elif a < b:
    print("O \033[4;36msegundo valor\033[m é \033[35mmaior\033[m")
else:
    print("\033[4;36mNão existe\033[m valor maior, os dois são \033[35miguais\033[m")

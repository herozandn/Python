n = str(input("Qual é seu nome? "))
if n == "Henrique":
    print("Que nome bonito!")
elif n == "Pedro" or n == "Maria" or n == "Paulo":
    print("Seu nome é popular")
elif n in "Ana Cláudia Jéssica Juliana":
    print("Belo nome feminino")
else:
    print("Seu nome é bem normal")
print("Tenha um bom dia, {}".format(n))

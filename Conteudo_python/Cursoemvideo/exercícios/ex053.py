f = str(input("Digite uma frase: ")).split()
f = ("".join(f))
f1 = f[::-1]
if f == f1:
    print("\033[39mPALÍNDROMO\033[m")
else:
    print("Não é palíndromo")

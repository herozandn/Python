p = float(input("Informe seu peso em kg: "))
h = float(input("Informe sua altura em m: "))
imc = p / (h * h)

if imc < 18.5:
    print("{:.2f}\033[31m\nABAIXO DO PESO\033[m".format(imc))
elif 18.5 <= imc < 25:
    print("{:.2f}\033[32m\nPESO IDEAL\033[m".format(imc))
elif 25 <= imc < 30:
    print("{:.2f}\033[33m\nSOBREPESO\033[m".format(imc))
elif 30 <= imc < 40:
    print("{:.2f}\033[34m\nOBESIDADE\033[m".format(imc))
else:
    print("{:.2f}\033[35m\nOBESIDADE MÓRBIDA\033[m".format(imc))

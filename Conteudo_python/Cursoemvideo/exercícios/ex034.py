s = float(input("Informe seu salário: "))
if s > 1250:
    ns = ((1/10) * s) + s
    print("Seu novo salário com um aumento de 10% é R${:.2f}". format(ns))
if s <= 1250:
    ns = ((1.5/10) * s) + s
    print("Seu novo salário com um aumento de 15% é R${:.2f}".format(ns))

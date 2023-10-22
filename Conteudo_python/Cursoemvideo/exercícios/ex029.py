velocidade = float(input("Qual a velocidade do carro: "))
if velocidade > 80.0:
    excedente = velocidade - 80.0
    multa = excedente * 7.00
    print("Você foi multado em R$ {:.2f}".format(multa))
else:
    print("Tenha um bom dia!!")

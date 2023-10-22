p = float(input("Inofrme o valor do produto: "))
e = int(input("Digte\n[1] para \033[33mà vista\033[m \033[36mdinheiro / cheque\033[m"
              "\n[2] para \033[33mà vista\033[m \033[36mcartão\033[m"
              "\n[3] para \033[33maté duas vezes\033[m no \033[36mcartão\033[m"
              "\n[4] para \033[33mtrês vezes ou mais\033[m no \033[36mcartão\033[m"
              "\n"))

if e == 1:
    p = p - ((10/100)*p)
    print("Com \033[4m10% de desconto\033[m, o preço passa a ser \033[32mR${:.2f}\033[m".format(p))
elif e == 2:
    p = p - ((5/100)*p)
    print("Com \033[4m5% de desconto\033[m, o preço passa a ser \033[32mR${:.2f}\033[m".format(p))
elif e == 3:
    print("O preço a ser pago é \033[32mR${:.2f}\033[m".format(p))
else:
    p = p + ((20/100)*p)
    print("Com \033[4m20% de juros\033[m, o preço passa a ser \033[32mR${:.2f}\033[m".format(p))

n = int(input("Digite um número: "))
e = int(input("[1] para \033[31mbinário\033[m "
              "\n[2] para \033[32moctal\033[m "
              "\n[3] para \033[33mhexadecimal\033[m"
              "\n"))
if e == 1:
    print("{}".format(bin(n)[2:]))
if e == 2:
    print("{}".format(oct(n)[2:]))
else:
    print("{}".format(hex(n)[2:]))



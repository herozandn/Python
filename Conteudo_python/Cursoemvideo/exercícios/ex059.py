v1 = int(input("Digite o 1° valor: "))
v2 = int(input("Digite o 2° valor: "))
menu = 0
while menu != 5:
    menu = int(input("[1] \033[32msomar\033[m"
                     "\n[2] \033[31mmultiplicar\033[m"
                     "\n[3] \033[33mmaior\033[m"
                     "\n[4] \033[34mnovos números\033[m"
                     "\n[5] \033[35msair do programa\033[m"
                     "\n"))
    if menu == 1:
        soma = v1 + v2
        print("A soma de\033[95m", v1, "\033[mcom\033[95m", v2, "\033[mé igual a\033[95m", soma, "\033[m")
    elif menu == 2:
        mult = v1 * v2
        print("A multilplicação de\033[94m", v1, "\033[me\033[94m", v2, "\033[mé igual a\033[94m", mult, "\033[m")
    elif menu == 3:
        if v1 > v2:
            print("O \033[95mmaior\033[m valor é", v1)
        else:
            print("O \033[95mmaior\033[m valor é", v2)
    elif menu == 4:
        v1 = int(input("Digite um novo valor: "))
        v2 = int(input("Digite outro valor: "))

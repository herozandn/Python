n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
m = (n1+n2)/2

if m < 5.0:
    print("\033[31mREPROVADO\033[m")
elif 5.0 <= m <= 6.9:
    print("\033[32mRECUPERAÇÃO\033[m")
else:
    print("\033[36mAPROVADO!!!\033[m")

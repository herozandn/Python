vc = float(input("Informe o valor da casa: "))
s = float(input("Informe seu salário: "))
a = int(input("Informe em quantos anos você pagará: "))

vm = vc / (a*12)

if vm < s*(30/100):
    print("\033[32mEmpréstimo aceito")
else:
    print("\033[31mEmpréstimo negado")

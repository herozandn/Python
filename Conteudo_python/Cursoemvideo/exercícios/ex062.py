p = int(input("Digite o primeiro termo da progressão: "))
r = int(input("Digite a razão da progressão: "))

d = 0

while d < 10:
    d += 1
    u = p + (d - 1) * r
    print(u, end=" ")
t = int(input("\nDigite quantos termos a mais você quer ver: "))
a = 0
if t > a:
    while t > a:
        a += 1
        u = p + ((a+10) - 1) * r
        print(u, end=" ")

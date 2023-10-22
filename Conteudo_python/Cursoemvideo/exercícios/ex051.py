p = int(input("Digite o primeiro termo da progressão: "))
r = int(input("Digite a razão da progressão: "))
d = 10

u = p + (d-1)*r
u += 1
for c in range(p, u, r):
    print(c, end=" ")

p = int(input("Digite o primeiro termo da progressão: "))
r = int(input("Digite a razão da progressão: "))

d = 0

while d < 10:
    d += 1
    u = p + (d - 1) * r
    print(u, end=" ")
print("FIM")
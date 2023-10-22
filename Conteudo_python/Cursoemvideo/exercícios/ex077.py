p = ("maça", "pao", "navio", "tempo", "escritorio", "escravo", "queijo", "pano", "mao", "caixa", "lupa", "gula", "casa")

c = 0
while True:
    print("Na palavra ", end="")
    print(p[c].upper(), end=" ")
    c += 1
    print("temos")
    if c == len(p):
        break
    for l in p:
        if l.lower() in "aeiou":
            print(l, end=" ")
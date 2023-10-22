from datetime import date
a = int(input("Em que ano você nasceu? "))

if date.today().year - a == 18:
    print("\033[7mJá está na hora de você se alistar\033[m")
elif date.today().year - a > 18:
    b = (date.today().year - a) - 18
    print("\033[31mJá passaram {} anos do seu tempo de alistamento\033[m".format(b))
else:
    c = (date.today().year - a) - 18
    print("\033[33mFaltam {} anos para seu alistamento\033[m".format(abs(c)))

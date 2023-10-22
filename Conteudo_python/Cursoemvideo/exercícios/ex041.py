from datetime import date
a = int(input("Em que ano você nasceu? "))

if date.today().year - a <= 9:
    print("\033[31mMIRIM\033[m")
elif 9 < date.today().year - a <= 14:
    print("\033[32mINFANTIL\033[m")
elif 14 < date.today().year - a <= 19:
    print("\033[33mJUNIOR\033[m")
elif date.today().year - a == 20:
    print("\033[34mSÊNIOR\033[m")
else:
    print("\033[35mMASTER\033[m")

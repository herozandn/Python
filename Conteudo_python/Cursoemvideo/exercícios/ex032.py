from datetime import date
a = int(input("Em que ano estamos? "))
if a == 0:
    a = date.today().year
r = a % 4
print("{} é BISSEXTO!!!".format(a) if r == 0 and a % 100 != 0 or a % 400 == 0 else "{} não é bissexto".format(a))

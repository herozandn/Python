from time import sleep

a = 0.5
x = 0
y = 0
z = 0

r1 = int(input("RETA 1: "))
sleep(a)
r2 = int(input("RETA 2: "))
sleep(a)
r3 = int(input("RETA 3: "))
sleep(a)

if abs(r2-r3) < r1 < r2+r3:
    x = 1
if abs(r1-r3) < r2 < r1+r3:
    y = 1
if abs(r1-r2) < r3 < r1+r2:
    z = 1
if x + y + z == 3:
    print("É possível fazer um triângulo")
if x + y + z < 3:
    print("Não é possível fazer um triângulo")

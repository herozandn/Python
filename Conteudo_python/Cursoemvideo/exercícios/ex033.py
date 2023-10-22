x, y, z = input("Digite três números: ").split()
x = int(x)
y = int(y)
z = int(z)

if x > y and x > z:
    print("{} é o maior".format(x))
    if y > z:
        print("{} é o menor".format(z))
    elif z > y:
        print("{} é o menor".format(y))
elif y > x and y > z:
    print("{} é o maior".format(y))
    if x > z:
        print("{} é o menor".format(z))
    elif z > x:
        print("{} é o menor".format(x))
elif z > y and z > x:
    print("{} é o maior".format(z))
    if y > x:
        print("{} é o menor".format(x))
    elif x > y:
        print("{} é o menor".format(y))

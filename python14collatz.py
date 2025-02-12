#
print("¿Número?")
num = int(input())
while (num != 1):
    if (num % 2 == 0):
    # número PAR
        num = num / 2
    else:
        num = num * 3 + 1
    print("El número es ,", num)
print("Fin de programa")
# Pedir número y mostrar la tabla de multiplicar
print("¿Número? ")
num = int(input())
#while ( num < (num * 10)):
for i in range( 1 , 11 ):
    multi = num * i
    print(str(num) + " * " + str(i) + " = " + str(multi))
print("Fin de programa")
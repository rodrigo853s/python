
# Pedir 2 números
# Mostrar un menú con:
# Sumar
# Restar
# Multiplicar
# Tres métodos , uno por función y mostraremos el resultado de lo seleccionado

def sumar(num1, num2):
    return num1 + num2
    
def restar(num1, num2):
    return num1 - num2 

def multiplicar(num1, num2):
    return num1 * num2

def mostrarMenu():
    print("Seleccione una opción:")
    print("Opción1 --> Sumar")
    print("Opción2 --> Restar")
    print("Opción3 --> Multiplicar")

# Código principal
print("Método return")
print("Introduzca un número")
valor = int(input())
print("Introduzca otro número")
valor2 = int(input())
mostrarMenu()
opcion = int(input())
if (opcion == 1):
    resultado = sumar(valor, valor2)
    print(str(valor) + ' + ' + str(valor2) + " = " + str(resultado))
elif (opcion == 2):
    resultado = restar(valor, valor2)
    print(str(valor) + ' - ' + str(valor2) + " = " + str(resultado))
elif (opcion == 3):
    resultado = multiplicar(valor, valor2)
    print(str(valor) + ' * ' + str(valor2) + " = " + str(resultado))
else:
    print("Wrong option")


print("Fin de programa")

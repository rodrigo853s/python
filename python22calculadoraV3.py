# SI El usuario no introduce números (inicio)
# volver a pedirle números hasta que nos de dos números
# Meter una opción más para que elu suario meta dos numeros mas
# si lo desea
# DECLARACION METODOS
def sumarNumeros(num1, num2):
    return num1 + num2

def restarNumeros(num1, num2):
    return num1 - num2

def multiplicarNumeros(num1, num2):
    return num1 * num2


def mostrarMenu():
    print("0.- Salir")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("Seleccione una opción")

#--------------------------------
print("Calculadora metodos")
print("Introduzca numero 1")
# Almacenar lo que pone el usuario en una variable STRING
aux = input()
while (aux.isdigit() == False)
    print("Esto no es un número")
    print("Introduzca numero 1")
    aux = input()
numero1 = int(aux)

print("Introduzca numero 2")
# Almacenar lo que pone el usuario en una variable STRING para poder usar isdigit
aux = input()
while (aux.isdigit() == False)
    print("Esto no es un número")
    print("Introduzca numero 2")
    aux = input()
numero2 = int(aux)

    
print("Introduzca numero 2")
numero2 = int(input())
# ASIGNAMOS UN VALOR A OPCION PARA ENTRAR EN EL BUCLE
opcion = 1
# CREAMOS UN WHILE HASTA QUE EL USUARIO ESCRIBA 0
while (opcion != 0):
    mostrarMenu()
    opcion = int(input())
    operacion = 0
    if (opcion == 1):
        operacion = sumarNumeros(numero1, numero2)
    elif (opcion == 2):
        operacion = restarNumeros(numero1, numero2)
    elif (opcion == 3):
        operacion = multiplicarNumeros(numero1, numero2)
    else:
        print("No ha seleccionado una opción correcta")
    print("Operación " + str(operacion))
print("Fin de programa")

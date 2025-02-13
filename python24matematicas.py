# PRIMERO IMPORTS
import libreria24matematicas

# METODOS
#ninguno en este ejemplo

# CÓDIGO
print("Calculadora métodos")
num1 = 3
num2 = 5
libreria24matematicas.mostrarMenu()
opcion = int(input())
resultado = 0

if (opcion == 1):
    resultado = libreria24matematicas.sumarNumeros(num1, num2)
    print(str(num1) + ' + ' + str(num2) + " = " + str(resultado))
elif (opcion == 2):
    resultado = libreria24matematicas.restarNumeros(num1, num2)
    print(str(num1) + ' - ' + str(num2) + " = " + str(resultado))
elif (opcion == 3):
    resultado = libreria24matematicas.multiplicarNumeros(num1, num2)
    print(str(num1) + ' * ' + str(num2) + " = " + str(resultado))
else:
    print("Wrong option")

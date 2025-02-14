from class30coche import Coche
from class31deportivo import Deportivo

print("Conduciendo mi coche")
car = Coche()
print ("Deportivo")
depor = Deportivo()
depor.arrancar()
depor.acelerar()
depor.turbo()
velDepor = depor.getVelocidadMaxima()
print ("Velocidad deportivo ", velDepor)
car.marca = "Volkswagen"
car.arrancar()
car.acelerar()
car.modelo = "Escarabajo"

opcion = -1
while (opcion != 0):
     print("------------------")
     print("0.- Salir")
     print("1.- Arrancar")
     print("2.- Acelerar")
     print("3.- Frenar")
     print("4.- Detener coche")
     print("Seleccione una opción")
     opcion = int(input())
     if (opcion == 1):
         car.arrancar()
     elif (opcion == 2):
         car.acelerar()
     elif (opcion == 3):
         car.frenar()
     elif (opcion == 4):
         car.detener()
     elif (opcion == 0):
         print("Saliendo del programa")
     else:
         print("Opción incorrecta")
print("Fin de programa")
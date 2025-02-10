#
#Debemos pedir el día, el número de mes y el año que el usuario haya nacido.
print("¿Día de nacimiento?")
dia = int(input())
print("¿Mes de nacimiento?")
mes = int(input())
print("¿Año de nacimiento?")
year = int(input())
if (mes == 1):
    year = year - 1
    mes = 13
elif (mes == 2):
    year = year - 1
    mes = 14
from math import trunc
#print("El día de nacimiento es " + str(dia) + "/" + str(mes) + "/" str(year))
#Multiplicar el Mes más 1 por 3 y dividirlo entre 5
primero = trunc((mes + 1) * 3) / 5
segundo = trunc(year / 4)
tercero = trunc(year / 100)
cuarto = trunc(year / 400)
# Sumar el dia, el doble del mes, el año, el resultado de la operación 1, 
# el resultado de la operación 2, menos el resultado de la operación 3 más la operación 4 más 2.
quinto = trunc(dia + (2 * mes) + year + primero + segundo - tercero + cuarto + 2)  
sexto = trunc(quinto / 7)
result = trunc(quinto - (sexto * 7))
if (result == 0):
    resultado = "sabado"
elif (result == 1):
    resultado = "domingo"
elif (result == 2):
    resultado = "lunes"
elif (result == 3):
    resultado = "martes"
elif (result == 4):
    resultado = "miercoles"
elif (result == 5):
    resultado = "jueves"
elif (result == 6):
    resultado = "viernes"
print(resultado)




#DNI letra
# Se calcula el valor de la siguiente resta 
#( nº DNI - (ENTERO(nº DNI / 23) * 23
from math import trunc
print("Introduzca número DNI")
dni = int(input())
res = dni - (int(dni / 23) * 23)
print(res)
if (res == 0):
    letra = "T"
elif (res == 5):
    letra = "M"
#elif etcm, etc 
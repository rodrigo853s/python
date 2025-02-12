# Pedir texto numérico
# sumar cada número y mostrar el resulado
print("¿ISBN?")
isbn = input()
longitud = len(isbn)
if (longitud != 10 or isbn.isnumeric() is False):
    print("El número no es correcto")
else:
    suma = 0
# RECORREMOs CADA CARACTER
    for i in range(longitud):
    # ALMACENAMOS CADA CARACTER
        letra = isbn[i]
        #print(letra)
     #CONVERTIMOS CADA CARACTER A ENTERO
        numero = int(letra)
    # SUMAMOS CADA NUMERO
        multi = (i + 1) * numero
        print(multi)
        suma = sum(multi)
print("Fin de programa")

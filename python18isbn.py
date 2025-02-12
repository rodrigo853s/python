print("¿ISBN?")
isbn = input() # HA DE SER TEXTO, PARA IR LETRA A LETRA
longitud = len(isbn)
if (longitud != 10 or isbn.isnumeric() == False):
    print("El número no es correcto")
else:
    suma = 0
# RECORREMOs CADA CARACTER
    for i in range(longitud):
    # ALMACENAMOS CADA CARACTER
        letra = isbn[i] # i ES LA POSICIÓN DE CADA LETRA
        #print(letra)
     #CONVERTIMOS CADA CARACTER A ENTERO
        numero = int(letra)
    # SUMAMOS CADA NUMERO
        multi = (i + 1) * numero
        #print(multi)
        suma = suma + multi
    if ( suma % 11 == 0 ):
        print("El isbn " + isbn + " es CORRECTO")
    else:
        print("El isbn " + isbn + " NO es CORRECTO")

print("Fin de programa")

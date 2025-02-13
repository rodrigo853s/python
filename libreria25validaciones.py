# Método para validar ISBN. NOS DEVUELVE CORRECTO O NO
# Método para calcular letra DNI. NOS DEVUELVE LA LETRA
def compruebaIsbn(isbn):
    #isbn = input() # HA DE SER TEXTO, PARA IR LETRA A LETRA
    longitud = len(isbn)
    if (longitud != 10 or isbn.isnumeric() == False):
        return False
    else:
        suma = 0
    # RECORREMOs CADA CARACTER
        for i in range(longitud):
        # ALMACENAMOS CADA CARACTER
            letra = isbn[i] # i ES LA POSICIÓN DE CADA LETRA
        #CONVERTIMOS CADA CARACTER A ENTERO
            numero = int(letra)
        # SUMAMOS CADA NUMERO
            multi = (i + 1) * numero
            #print(multi)
            suma = suma + multi
        if ( suma % 11 == 0 ):
            return True
        else:
            return False
        

def calculaLetradni (dni):
    res = dni - (int(dni / 23) * 23)
    if (res == 0):
        letra = "T"
    elif (res == 5):
        letra = "M"
    print(letra)
#elif etcm, etc 
# Pedir texto numérico
# sumar cada número y mostrar el resulado
print("¿Texto numérico?")
textonum = input()
suma = 0
# RECORREMOs CADA CARACTER
longitud = len(textonum) # LA GUARDO, AUNQUE NO ES NECESARIO
for i in range(longitud):
    # ALMACENAMOS CADA CARACTER
    letra = textonum[i]
     #CONVERTIMOS CADA CARACTER A ENTERO
    numero = int(letra)
    # SUMAMOS CADA NUMERO
    suma = suma + numero
print("La suma de " + textonum + " es " + str(suma))
print("Fin de programa")

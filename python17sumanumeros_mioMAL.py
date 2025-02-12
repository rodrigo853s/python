# Pedir texto numérico
# sumar cada número y mostrar el resulado
print("¿Texto numérico?")
# VAR AUXILIAR
aux = input()
if (aux.isdigit()):
    longitud = len(aux)
    print(longitud)
    for i in range(0, longitud):
        suma = aux[i]
    print(suma)

else:
    print("No es un numero")
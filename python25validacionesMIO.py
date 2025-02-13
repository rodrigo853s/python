# Probamos si llamando al método ISBN funciona
# Llamamos al método DNI
import libreria25validaciones
print("Introduzca ISBN:")
isbn = input()
valido = libreria25validaciones.compruebaIsbn(isbn)
print("El ISBN es", valido)

print("Introduzca DNI: ")
dni = int(input())
libreria25validaciones.calculaLetradni(dni)
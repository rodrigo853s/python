print("Clase string y funciones")
texto = "primero python"
#VAMOS PROBANDO MÉTODOS
print("upper ", texto.upper())
print("replace ", texto.replace("o", "@"))
print("Letra 0 ", texto[0])
# FUNCIÓN LENGHT
print("Longitud ", len(texto))
#MAS MÉTODOS
print("find P", texto.find("p"))
print("find Z", texto.find("z"))
print("rfind R", texto.rfind("r"))
#SOBRECARGA DE FIND (contenido a buscar, índice)
print("find p sobrecarga", texto.find("p", 1))
print("startswith A ", texto.startswith("A"))
print("endswith A ", texto.endswith("n"))
print("isdigit() ", texto.isdigit())
print("isalpha() ", texto.isalpha()) # FALSE POR EL ESPACIO
print("isalnum() ", texto.isalnum()) # FALSE POR EL ESPACIO
# SLICING O SUBSTRINGS
# DESDE POSICION 2 EN ADELANTE
substring = texto[2:]
print("Posición 2 en adelante ", substring)
# DESDE POSICION 2 A POSICIÓN 5
substring = texto[2: 5]
print("Posición 2 a 5 ", substring)
# RECORRER CADA CARACTER
longitud = len(texto)
for i in range(longitud):
    letra = texto[i]
    print("Posición " + str(i) + ": " + letra)
# COMPROBAR INPUT NUMÈRICO
print("¿Número")
# VAR AUXILIAR
aux = input()
if (aux.isnumeric()):
    for i in range():
        print("Es un numero")
else:
    print("No es un numero")
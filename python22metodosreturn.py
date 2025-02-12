
def convertirMayusculas(texto):
    return texto.upper() # return finaliza el método
    
def convertirMinusculas(texto):
    return texto.lower()

def concatenar(texto1, texto2):
    resultado = texto1 + texto2
    return resultado

def mostrarMenu():
    print("Selecione una opción:")
    print("Opción1 --> Convertir a MAYÚSCULAS")
    print("Opción2 --> Convertir a minúsculas")
    print("Opción3 --> Concatenar textos")

# Código principal
print("Método return")
print("Introduzca texto")
valor = input()
mostrarMenu()
opcion = int(input())
if (opcion == 1):
    resultado = convertirMayusculas(valor)
    print(resultado)
elif (opcion == 2):
    resultado = convertirMinusculas(valor)
    print(resultado)
else:
    print("Introduzca otro texto")
    valor2 = input()
    resultado = concatenar(valor, valor2)
    print(resultado)


print("Fin de programa")

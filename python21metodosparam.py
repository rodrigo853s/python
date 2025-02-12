
def saludar(nombre):
    print("Bienvenido " + nombre)
def despedir(nombre, dia):
    print("Adios " + dia + ' ' + nombre)

# Código principal
print("Ejemplo de método con parámetros")
name = "Alumno"
dia = "miércoles"
# Podemos llamar al método
saludar(name)
despedir(dia, name)

print("Fin de programa")

from  conexionoracle47eliminarenfermos import ConexionOracleEnfermos
print("Probando clases de Oracle: ENFERMOS")
print("Introduzca un número de Inscripción")
inscripcion = int(input())
# creamos un objeto connection para ejecutar las consultas
print("Seleccione una opción")
print("1 - Eliminar")
print("2 - Modificar")
opcion = int(input())
if (opcion == 1):
    connection = ConexionOracleEnfermos()
    eliminados = connection.eliminarEnfermo(inscripcion)
    print(f"Enfermos eliminados: {eliminados}")
else:
    print("Nuevo Apellido?")
    apellido = input()
    connection = ConexionOracleEnfermos()
    modificados = connection.modificarApellido(apellido, inscripcion)
    print(f"Enfermos modificados: {modificados}")
print("Fin de programa")
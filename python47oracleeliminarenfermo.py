from  conexionoracle47eliminarenfermos import ConexionOracleEnfermos
print("Probando clases de Oracle: ENFERMOS")
print("Introduzca un número de Inscripción")
inscripcion = int(input())
# creamos un objeto connection para ejecutar las consultas

connection = ConexionOracleEnfermos()
eliminados = connection.eliminarEnfermo(inscripcion)

print(f"Enfermos eliminados: {eliminados}")
print("Fin de programa")
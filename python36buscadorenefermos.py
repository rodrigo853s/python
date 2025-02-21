# Buscar un enfermo por su INSCRIPCIÓN
# Si no existe, lo indicamos. Si existe,
# mostramos apellido y dirección

import oracledb

print("Introduzca número de inscripcion")
data = input() # Lo cogemos como texto, para pasárselo al string de la consulta sql
sql = "select * from ENFERMO where inscripcion=" + data
connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
cursor = connection.cursor()
cursor.execute(sql)

# Como estamos buscando por Primary key
# sólo nos puede devolver una fila

row = cursor.fetchone()

# Debemos comprobar si la fila tiene contenido/algo

if (not row):
    print("No existe el enfermo")
else:
    apellido = row[1]
    direccion = row[2]
    print(apellido + ", " + direccion )

# Cerrar TODO

cursor.close()
connection.close()

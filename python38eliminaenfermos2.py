# Buscar un enfermo por su INSCRIPCIÓN
# y nos lo cepillamos


import oracledb

print("Introduzca número de inscripcion")
data = input() # Lo cogemos como texto, para pasárselo al string de la consulta sql
sql = "delete from ENFERMO where inscripcion=" + data
connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
cursor = connection.cursor()
# SI EL CURSOR ES DE ACCIÓN RECUPERAMOS SU int MEDIANTE rowcount
cursor.execute(sql)

afectados = cursor.rowcount
print("Registros eliminados " + str(afectados))
# Para que realmente lo haga, hay que incluir "commit" (o rollback)
connection.commit()


# Cerrar TODO

cursor.close()

# UNA VEZ QUE HEMOS CERRADO EL CURSOR, POEDMOES HACER MÄS
# CONSULTAS SOBRE EL MISMO OBJETO, CREANDO UNO NUEVO CON LA CONEXIÓN
sqlselect = "select * from ENFERMO"
# CREAMOS UN CURSOR SOBRE LA MISMA VARIABLE

cursor = connection.cursor()
cursor.execute(sqlselect)
print("----------ENFERMOS---------")
for row in cursor:
    print("Inscripción: " + str(row[0]) + " - " + row[1])
#CERRAMOS EL CURSOR

cursor.close()
connection.close()

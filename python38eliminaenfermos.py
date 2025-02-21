# Buscar un enfermo por su INSCRIPCIÓN
# y nos lo cepillamos


import oracledb

print("Introduzca número de inscripcion")
data = input() # Lo cogemos como texto, para pasárselo al string de la consulta sql
sql = "delete from ENFERMO where inscripcion=" + data
connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
cursor = connection.cursor()
# SI EL CURSOR ES DE ACCIÓN RECUPERAMOS SU INT MEDIATE rowcount
cursor.execute(sql)

afectados = cursor.rowcount
print("Registros eliminados " + str(afectados))
# Para que realmente lo haga, hay que incluir "commit" (o rollback)
connection.commit()


# Cerrar TODO

cursor.close()
connection.close()

# Pedimos al usuario los datos del DEPARTAMENTO nuevo que queremos insertar
# 

import oracledb
print("Insertar nuevo DEPARTAMENTO:")
connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

print("Introduzca ID DEPARTAMENTO:")
iddept = input()

print("Introduzca NOMBRE DEPARTAMENTO:")
nombre = input()

print("Introduzca LOCALIDAD DEPARTAMENTO:")
localidad = input()
# insert into DEPT values (99, 'A','B') --> PARA VISUALIZAR LA CONSULTA
sqlinsert = "insert into DEPT values (" + iddept + ",'" + nombre + "','" + localidad + "')"
print (sqlinsert)
cursor = connection.cursor()
cursor.execute(sqlinsert)

print("Departamentos insertados: " + str(cursor.rowcount))

cursor.close()

cursor = connection.cursor()
sqlselect = "select * from DEPT"

cursor.execute(sqlselect)

for row in cursor:
    print(row)

cursor.close()
connection.close()

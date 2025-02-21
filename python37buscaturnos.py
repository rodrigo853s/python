# Buscar un empleados por su TURNO
# mostramos apellido y funcion del turno determinado

import oracledb

print("Introduzca Turno - M,T,N")
data = input() 
#sql = "select APELLIDO, FUNCION from PLANTILLA where TURNO =" + data
sql = "select APELLIDO, FUNCION from PLANTILLA where TURNO ='" + data + "'"
#print(sql)
connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
cursor = connection.cursor()
cursor.execute(sql)

for apellido, funcion in cursor:
    print(apellido + ": " + funcion)

cursor.close()
connection.close()





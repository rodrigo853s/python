# Pedimos al usuario los datos del HOSPITAL nuevo que queremos insertar
# 

import oracledb
print("Insertar nuevo HOSPITAL:")
connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

print("Introduzca ID CODIGO DE HOSPITAL:")
hospcod = input()

print("Introduzca NOMBRE HOSPITAL:")
nombre = input()

print("Introduzca DIRECCIÓN HOSPITAL:")
direccion = input()

print("Introduzca TELÉFONO HOSPITAL:")
telefono = input()

print("Introduzca NÚMERO DE CAMAS DEL HOSPITAL:")
camas = input()

# insert into HOSPITAL values (10,'B','C','D',20) --> PARA VISUALIZAR LA CONSULTA
#sqlinsert = "insert into HOSPITAL values (" + hospcod + ",'" + nombre + "','" + direccion + "','" + telefono + "', " + camas + ")"
sqlinsert = f"insert into HOSPITAL values ({hospcod},'{nombre}','{direccion}','{telefono}',{camas}) "

print (sqlinsert)
cursor = connection.cursor()
cursor.execute(sqlinsert)

print("Hospitales insertados: " + str(cursor.rowcount))

cursor.close()

cursor = connection.cursor()
sqlselect = "select * from HOSPITAL"

cursor.execute(sqlselect)

for row in cursor:
    print(row)

cursor.close()
connection.close()

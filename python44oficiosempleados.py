#
#
#
#
#
#
import oracledb


print("----Buscador oficios empleados---")
#Temporal
# Hacemos primero esta parte
print("Introduzca un oficio")
oficio = input()
connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
sqlempleados = "select * from EMP where OFICIO=:p1" 
cursor = connection.cursor()
cursor.execute(sqlempleados, (oficio,))
for row in cursor:    # para chequear que funciona
    print (row)
cursor.close()
connection.close()
print("Fin de programa")
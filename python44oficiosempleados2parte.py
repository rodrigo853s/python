#
#
#
#
#
#
import oracledb

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
print("----Buscador oficios empleados---")
sqloficios = "select distinct OFICIO from EMP"
cursor = connection.cursor()
cursor.execute(sqloficios)
for ofi in cursor:
    print(ofi)
cursor.close()

print("Introduzca un oficio")
oficio = input()

sqlempleados = "select * from EMP where OFICIO=:p1" 
cursor = connection.cursor()
cursor.execute(sqlempleados, (oficio,))
for row in cursor:    # para chequear que funciona
    print (row)
cursor.close()
connection.close()
print("Fin de programa")
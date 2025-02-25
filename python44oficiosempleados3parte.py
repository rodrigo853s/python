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
contador = 1
for row in cursor:
    print(f"{contador} - {row[0]}")
    contador = contador + 1
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
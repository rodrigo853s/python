# Incrementaremos el salario a los empleados de un OFICIO.
# Pediremos OFICIO e INCREMENTO
# Mostraremos  el número de empleados con incremento
# YH mostraremos el apellido, oficio y salario de esos empleados


import oracledb
print("Incremento Salario:")
connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

print("Introduzca OFICIO:")
oficio = input()
print("Introduzca INCREMENTO:")
incremento = int(input())

sql = f"update EMP set SALARIO = SALARIO + {incremento} where OFICIO='{oficio}'" 

print (sql)
cursor = connection.cursor()
cursor.execute(sql) 

incrementados = cursor.rowcount
print("Usuarios incrementados " + str(incrementados))

cursor.close()
connection.close()

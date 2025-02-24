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

#sqlupdate  = "update EMP set SALARIO = SALARIO + 1 where OFICIO=DIRECTOR" --> PARA VISUALIZAR
# Nos vamos olvidando de concatenar (f ó "+"), por seguridad
sqlupdate  = "update EMP set SALARIO = SALARIO + :p1 where OFICIO=:p2" 

cursor = connection.cursor()
cursor.execute(sqlupdate, (incremento, oficio)) 
# CONSULTA DE ACCION; DEVUELVE REGISTROS AFECTADOS
registros = cursor.rowcount
# ALMACENAMOS EN BBDD
connection.commit()
# CERRAMOS EL CURSOR
cursor.close()
print(f"Usuarios incrementados: {registros}")
# AHORA PINTAMOS LOS REGISTROS QUE QUEREMOS
# ABRIMOS OTRO CURSOR
cursor = connection.cursor()
sqlselect = "select APELLIDO, OFICIO, SALARIO from EMP where OFICIO=:p1"
cursor.execute(sqlselect,(oficio,))
for ape, ofi, sal in cursor:
    print(f"Apellido:{ape}, Oficio: {ofi}, Salario:{sal}")


cursor.close()
connection.close()

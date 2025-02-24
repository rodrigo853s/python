# Incrementaremos el salario a los empleados de la PLANTILLA de un HOSPITAL.
# Pediremos Código de Hospital e INCREMENTO
# Mostraremos  el número de empleados con incremento
# Y mostraremos el apellido, función y salario de esos empleados


import oracledb
print("Incremento Salario:")
connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

print("Introduzca CÓDIGO DE HOSPITAL:")
hospital = input()
print("Introduzca INCREMENTO:")
incremento = int(input())

#sqlupdate  = "update PLANTILLA set SALARIO = SALARIO + 1 where HOSPITAL=19" --> PARA VISUALIZAR
# Nos vamos olvidando de concatenar (f ó "+"), por seguridad
sqlupdate  = "update PLANTILLA set SALARIO = SALARIO + :p1 where HOSPITAL_COD=:p2" 

cursor = connection.cursor()
cursor.execute(sqlupdate, (incremento, hospital)) 
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
sqlselect = "select APELLIDO, FUNCION, SALARIO from PLANTILLA where HOSPITAL_COD=:p2"
cursor.execute(sqlselect,(hospital,))
for ape, fun, sal in cursor:
    print(f"Apellido:{ape}, Función: {fun}, Salario:{sal}")


cursor.close()
connection.close()

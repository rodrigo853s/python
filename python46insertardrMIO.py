# Insertar Dr en un hospital determinado
# El programa deberá indicarnos qué hospitales hay, en un menú
# Debemos pedir:
# Apellido
# Especialidad
# salario
# Insertaremos el Dr en eh hospital elegido
# El id del Dr lo debemos recuperar como el Máximo del dr (otra consulta)

import oracledb

connection = oracledb.connect (user='SYSTEM', password='oracle', dsn='localhost/xe')
print("----Insertar nuevo Doctor---")

sqlhospital = "select NOMBRE from HOSPITAL"
cursor = connection.cursor()
cursor.execute(sqlhospital)
contador = 1
listahospital = []
for row in (cursor):
    print(f"{contador} - {row[0]}")
    listahospital.append(row[0])
    contador = contador + 1
cursor.close()

print("Elija un hospital")
opcion = int(input())
hospital = listahospital[opcion - 1]
sqlselectHospCod = "select HOSPITAL_COD from HOSPITAL where NOMBRE = :parametro1" 
cursor = connection.cursor()
cursor.execute(sqlselectHospCod, (hospital,))

id_hospital = 0
for row in cursor:   
    print (row[0])
    id_hospital = row[0]

cursor.close()

sqldoctor_no = "select max(DOCTOR_NO) from DOCTOR"
cursor = connection.cursor()
cursor.execute(sqldoctor_no)

print("Apellido del Doctor?")
apellido = input()

print("Especialidad del Doctor?")
especialidad = input()

print("Salario del Doctor?")
salario = int(input())

sqlinsert = "insert into DOCTOR (HOSPITAL_COD, DOCTOR_NO, APELLIDO, ESPECIALIDAD, SALARIO) values
(id_hospital, DOCTOR_NO, 'apellido' , 'especialidad', salario)

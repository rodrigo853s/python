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
print("----Insertar nuevo Doctor----")

print("Apellido del Doctor?")
apellido = input()

print("Especialidad del Doctor?")
espe = input()

print("Salario del Doctor?")
salario = int(input())



sqlhospital = "select * from HOSPITAL"
cursor = connection.cursor()
cursor.execute(sqlhospital)
contador = 1
listahospital = []
for row in (cursor):
    listahospital.append(row[0])
    print(f"{contador} - {row[1]}")
    contador = contador + 1
cursor.close()


print("Elija un hospital")
opcion = int(input()) - 1
hospital = listahospital[opcion]

sqldoctor_no = "select max(DOCTOR_NO) +1 as MAXIMO from DOCTOR"
cursor = connection.cursor()
cursor.execute(sqldoctor_no) 
row = cursor.fetchone() # Solo devuelve una fila; no hace falta hacer un bucle
iddoctor = row[0] # Solo tiene una columna
cursor.close()


sqlinsert = "insert into DOCTOR values (:idhospital, :iddoctor, :apellido, :espe, :salario)"
cursor = connection.cursor()
cursor.execute(sqlinsert, (hospital, iddoctor, apellido, espe, salario))
registros = cursor.rowcount
print(f"Doctores Insertados: {registros}")
connection.commit() 
cursor.close()
connection.close()

print("Fin de programa")

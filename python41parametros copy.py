# Pedimos al usuario los datos del DEPARTAMENTO y mostraremos
# algun dato de los empleados de dicho DEP
# 

import oracledb
print("Ejemplo de parámetros Oracle:")
connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

print("Introduzca número de DEPARTAMENTO:")
iddept = int(input()) # LO PONEMOS COMO NUMERO O NO (Oracle se lo come igual)

# insert into HOSPITAL values (10,'B','C','D',20) --> PARA VISUALIZAR LA CONSULTA
#sqlinsert = "insert into HOSPITAL values (" + hospcod + ",'" + nombre + "','" + direccion + "','" + telefono + "', " + camas + ")"
sql = "select * from EMP where DEPT_NO=:parametro1" # Ponemos ":" y el nombre que queramos

print (sql)
cursor = connection.cursor()
cursor.execute(sql, (iddept,)) # Aquí le pasmos el valor del DEPT, finalizando en "," si sólo es 1 parametro 

for row in cursor:
    print(f"Apellido: {row[1]}, Oficio: {row[2]}, Departamento: {row[7]}")

cursor.close()
connection.close()

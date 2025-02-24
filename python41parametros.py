# Pedimos al usuario los datos del DEPARTAMENTO y mostraremos
# algun dato de los empleados de dicho DEP
# 

import oracledb
print("Ejemplo de parámetros Oracle:")
connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

print("Introduzca número de DEPARTAMENTO:")
iddept = input()

# insert into HOSPITAL values (10,'B','C','D',20) --> PARA VISUALIZAR LA CONSULTA
#sqlinsert = "insert into HOSPITAL values (" + hospcod + ",'" + nombre + "','" + direccion + "','" + telefono + "', " + camas + ")"
sql = f"select * from EMP where DEPT_NO={iddept}"

print (sql)
cursor = connection.cursor()
cursor.execute(sql)

for row in cursor:
    print(f"Apellido: {row[1]}, Oficio: {row[2]}, Departamento: {row[7]}")

cursor.close()
connection.close()


# SI respondemos "0 or 1=1", nos muestra TODOS los resultados. Es un SQL Injection

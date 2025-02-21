import oracledb

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

print("Conectados!!!")
print("Introduzca número de departamento")
data = input() # Lo cogemos como texto, para pasárselo al string de la consulta sql


cursor = connection.cursor()
sql = "select * from DEPT where DEPT_NO=" + data
cursor.execute(sql)

# Como estamos buscando por Primary key
# sólo nos puede devolver una fila

row = cursor.fetchone()

# Debemos comprobar si la fila tiene contenido/algo

if (not row):
    print("No existe el departamento")
else:

    #print(row)
    # o, para verlo mejor

    cod = row[0]
    nombre = row[1]
    localidad = row[2]
    print(str(cod) + ", " + nombre + ", " + localidad)

# Cerrar TODO

cursor.close()
connection.close()

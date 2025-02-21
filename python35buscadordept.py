import oracledb

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

print("Connectados!!!")


cursor = connection.cursor()
sql = "select * from DEPT where DEPT_NO=30"
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

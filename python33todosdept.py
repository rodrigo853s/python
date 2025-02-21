# Importamos la libreria de Python Oracle
import oracledb

#  Tenemos un objeto connection (user, passwd, server/bbdd/port (1521 default))

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

print("Connectados!!!")

# Las consultas no llevan ";"
sql = "select * from DEPT"
# Creamos un cursor para realizar la consulta

cursor = connection.cursor()

# La consulta se ejecuta y recupero los datos a la vez 
# al aplicar el método execute(sql)

cursor.execute(sql)

# Una vez que tenemos los datos, tenemos que leerlos
# Hay varias formas
# Para recorrer un cursor se usan bucles for

for row in cursor:
    print(row)

    # Si desamos extrae datos de alguna columna
    # podemos realizarlo por el índice

    print(row[2])

    # También podemos recuperar datos
    # por nombre de columna. SÓLO es compatible con algunas BBDD. AQUÍ NO FUNCIONA
    #nombre = row.DNOMBRE
    #print (nombre)

# El cursor sólo se puede leer una vez. Si queremos leer de nuevo, debemos
# ejecutar de nuevo

fila = cursor.fetchone()
print(fila)                 # "None"

# También se puede recorrer por índices 

# for row in
#    num=row[0]
#    nombre=row[1]
#    ...

# O mediante variables asignadas al índice, como
# este ejemplo

sql = "select * from DEPT"
cursor = connection.cursor()
cursor.execute(sql)


for numero, nombre, localidad in cursor:
    print(str(numero) + ": " + nombre + ", " + localidad)


# Por norma, siempre debemos liberar los recursos de BBDD
# Cerrar TODO

cursor.close()
connection.close()

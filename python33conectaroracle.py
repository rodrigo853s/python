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
# Ahora, en lugar de fila en fila, todos a la vez
# Método fetchone()devuelve una fila y cada vez que lo ejecutemos, avanza una fila

row = cursor.fetchone()
print(row)
row = cursor.fetchone()
print(row)
row = cursor.fetchone()
print(row)
row = cursor.fetchone()
print(row)

# Por norma, siempre debemos liberar los recursos de BBDD
# Cerrar TODO

cursor.close()
connection.close()

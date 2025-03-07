# Mostrar los empleados de un turno
# Debemos seleccionar un turno en un menú
# Mostraremos los datos de la planilla de ese turno
#
#
#
import oracledb

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
print("----Buscador TURNOS plantilla---")
sqlturnos = """
    select distinct TURNO, case TURNO
    when 'T' then 'TARDE'
    when 'M' then 'MAÑANA'
    else 'NOCHE'
    end as VALOR
    from PLANTILLA
"""
cursor = connection.cursor()
cursor.execute(sqlturnos)
contador = 1
# El cursor desaparece tras ser ejecutado, por lo que no puedo seleccionar algo que ya no existe
# Por eso guardo los oficios en una lista que puedo usar cuando quiera
listaturnos = []
for row in cursor:
    listaturnos.append(row[0])
    print(f"{contador} - {row[1]}")
    contador = contador + 1
cursor.close()

print("Introduzca un turno")
opcion = int(input()) - 1
turno = listaturnos[opcion]

sqlplant = "select * from PLANTILLA where TURNO=:parametro1" 
cursor = connection.cursor()
cursor.execute(sqlplant, (turno,))
for row in cursor:    # para chequear que funciona
    print (row)
cursor.close()
connection.close()

print("Fin de programa")
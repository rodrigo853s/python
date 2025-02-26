import oracledb

class ConexionOracleEnfermos:
    # En el inicio de la class debemos crear un objeto coonection
    # para usarlo en todos los métodos (__init__)
    def __init__(self):
        self.connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

    def eliminarEnfermo(self, inscripcion):
        cursor = self.connection.cursor()
        sql = "delete from ENFERMO where INSCRIPCION=:p1"
        cursor.execute(sql, (inscripcion,))
        registros = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registros
    
# Método para modificar el apellido de un enfermo por su inscripción

    def modificarApellido(self, apellido, inscripcion):
        sql = "update ENFERMO set APELLIDO = :param1 where INSCRIPCION = :param2"
        cursor = self.connection.cursor()
        cursor.execute(sql, (apellido, inscripcion))
        registros = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registros
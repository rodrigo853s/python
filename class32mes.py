# Almacenar infirmación de un mes
# nombre, Tª máxima, Tª mínima
# Calcular media del mes (que se calcule sola)
# Al escribir el objeto mes (print(mes)) se tiene que visualizar nombre, max y min directamente
# 2 clases mes.class y pyhton.class


class Mes:
    nombreMes = ""
    temperaturaMaxima = 0
    temperaturaMinima = 0
 
    def mediaMes(self): 
        return (self.temperaturaMaxima + self.temperaturaMinima) / 2
    
    def __str__(self):
        return self.nombreMes + ", Max: " + str(self.temperaturaMaxima) + ", Min: " + str(self.temperaturaMinima)
    
 
        

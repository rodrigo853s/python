class Persona:
    nombre = ""
    apellidos = ""
    enail = ""
    anyonacimiento = 0 # Sin comillas
    pais = ""

    def __init__(self):          # Constructor; por defecto cuando se cree una persona
        self.pais = "Francia"    # será de Francia. Inicializa variables

    def getNombreCompleto(self): # con self accedo a la clase de arriba
        return self.nombre + " " + self.apellidos
    
    def getEdad(self):
        return 2025 - self.anyonacimiento
        

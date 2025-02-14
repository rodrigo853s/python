from class29persona import Persona
print("Test clase Persona")
#Creamos una nueva persona
person = Persona()
print(person.pais)
person.pais = "España"
print(person.pais)
person.anyonacimiento = 2000   # Sin comillas
person.email = "pepe@gmail.com"
print(person.getNombreCompleto())
print(str(person.getEdad()))

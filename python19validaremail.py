# Validar email SIN BUCLES, sólo MÉTODOS
# HA DE CONTENER @ (UNA SOLA, NI AL PRINCIPIO NI AL FINAL)
# HA DE CONTENER UN . (NI AL PRINCIPIO NI AL FINAL)
# HA DE CONTENER 1 . DESPUÉS DE @
# DOMINIO DE 2 a 3 CARACTERES
# MENSAJE CON EL ERROR DETECTADO
print("Introduzca email...")
email = input()

if (email.find("@") == -1 ): # email.count("@") == 0
    print("El email no tiene @ ")
elif (email.startswith("@") == 1 or email.endswith("@") == 1):
    print("El email no puede empezar o terminar con @ ")
elif (email.count("@") > 1):
    print("El email tiene más de una @")

if (email.find(".") == -1 ):
    print("El email no tiene . ")
elif (email.startswith(".") == 1 or email.endswith(".") == 1):
    print("El email no puede empezar o terminar con . ")
# EXISTA PUNTO DESPUES DE ARROBA
position = email.find('@')
position2 = email.rfind('.')

if (position2 < position):
    print("No hay . después de @")
# NECESITAMOS RECUPERAR EL DOMINIO A PARTIR DEL ÚLTIMO PUNTO

ultimoPunto = (email.rfind('.'))
dominio = email[ultimoPunto + 1:]
longitudDominio = len(dominio)
if ( longitudDominio > 3 or longitudDominio < 2):
    print("Dominio mal..")
print("Fin de programa")






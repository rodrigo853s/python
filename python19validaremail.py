# Validar email SIN BUCLES, sólo MÉTODOS
# HA DE CONTENER @ (UNA SOLA, NI AL PRINCIPIO NI AL FINAL)
# HA DE CONTENER UN . (NI AL PRINCIPIO NI AL FINAL)
# HA DE CONTENER 1 . DESPUÉS DE @
# DOMINIO DE 2 a 3 CARACTERES
# MENSAJE CON EL ERROR DETECTADO
print("Introduzca email...")
email = input()
position = email.find('@')
print(position)
if (email.find("@") == -1 ):
    print("El email no tiene @ ")
elif (email.startswith("@") == 1 or email.endswith("@")):
    print("El email no puede empezar o terminar con @ ")
elif (email.count("@") > 1):
    print("El email tiene más de una @")

if (email.find(".") == -1 ):
    print("El email no tiene . ")
elif (email.startswith(".") == 1 or email.endswith(".")):
    print("El email no puede empezar o terminar con . ")

position2 = email.rfind('.')
print(position2)
if (position2 < position):
    print("No hay . después de @")

#if (email.rfind('.') > 3)
print(email.rfind('.'))
punto = (email.rfind('.'))





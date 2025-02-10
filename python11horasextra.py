#Pediremos a un usuario las horas trabajadas, precio hora y los kilómetros
print("Horas trabajadas")
horas = int(input())
print("Precio hora")
precio = int(input())
print("Kilometros")
km = int(input())
#El trabajador tendrá horas extra a partir de la hora 36
#Cada hora extra será 2€ más

if (horas > 36):
    extras = horas - 36
else:
    extras = 0

#Si el trabajador hace menos de 100 km las dietas son LOCALES
#Si el trabajador hace entre 101km y 500 km las dietas son PROVINCIALES
#Si hace más km, serán NACIONALES35

if (km < 100):
    dietas = "LOCALES"
elif (km >= 101 and km < 500):
    dietas = "PROVINCIALES"
else:
    dietas = "NACIONALES"
#Si el precio final es menor a 250€ SIN RETENCIONES
#Si es entre 251 y 600, 20% retención
#Si es mayor 40 % retención
preciofinal = (horas * precio) + (extras * 2)
if (preciofinal < 250):
    retencion = "SIN RETENCIONES"
elif (preciofinal >= 250 and preciofinal <= 600):
    retencion = "20% RETENCION"
else:
    retencion = "40% RETENCION"
#Salario base: 36 * 20
#Salario Extra: 4 * 22
#Salario total: Salario base + salario extra
salariob = precio * horas  # MAL, VER EL DEL PROFESOR  
salarioe = (precio + 2) * extras
salariot = salariob + salarioe
print("Horas trabajadas", horas)
print("Horas extras", extras)
print("Kilometros", km)
print("Dietas", dietas)
print("Retención", retencion)
print("Salario base", salariob)
print("Salario extra", salarioe)
print("Salario total", salariot)
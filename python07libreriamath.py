print("Ejemplo de librerias")
#Sintaxis con FROM
from math import floor, ceil, trunc
#import math  # OTRA SINTAXIS
numero1 = 20
numero2 = 3
division = numero1 / numero2
print("La division es ", division)
#Declaramos variables para almacenar los valores de las operaciones
varFloor = floor(division)
#varFloor = math.floor(division) #EN ESTE CASO HAY QUE PONER LA LIBRERIA
varCeil = ceil(division)
varTrunc = trunc(division)
print("Floor ", varFloor)
print("Ceil ", varCeil)
print("Trunc ", varTrunc)
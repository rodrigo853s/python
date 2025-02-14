from class32mes import Mes
print("Test clase Mes")

enero = Mes()
enero.nombreMes = "Enero"
enero.temperaturaMaxima = 16
enero.temperaturaMinima = 2
media = enero.mediaMes()
print("Enero ", media)
print(enero)

febrero = Mes()
febrero.nombreMes = "Febrero"
febrero.temperaturaMaxima = 13
febrero.temperaturaMinima = 1
media = febrero.mediaMes()
print("Febrero ", media)
print(febrero)






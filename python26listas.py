print("--------------LISTAS-------------")
print("CREANDO LISTAS DE ENTEROS")
# Las slitas comienzan en 0 y terminan en LEN -1
listaNumeros= [20,84,18,41,36,25]
print("Número 0:",listaNumeros[0])
print("Número 2:",listaNumeros[2])
print("CREANDO LISTAS DE CADENAS")
listaNombre= ["Benito", "Floro", "Floro", "Angulo", "Andrea", "Pascual", "Sara"]
print("Nombre 4:",listaNombre[4])
print("Nombre 2:",listaNombre[2])
print("---------------------------")
# Vamos a recorrer la lista y mostrar su posicion
for i in range(len(listaNombre)):
    print(str(i) + "=" + listaNombre[i])
print("---------------------------")
# append crea un nuevo elemento al final
listaNombre.append("Johnny")
print("Nombre 6:",listaNombre[6])
# insert() crea un nuevo elemento en una posicion
listaNombre.insert(4, "NewName")
print("Nombre 4:",listaNombre[4])
# remove() elimina un el primer elemento que encuentra de los que se le indican.
# Si no lo encuentra da error
listaNombre.remove("Floro")
# pop() elimina un elemento por su posición
listaNombre.pop(1)
# Vamos a recorrer la lista y mostrar su posicion
for i in range(len(listaNombre)):
    print(str(i) + "=" + listaNombre[i])
print("---------------------------")
# del es igual que pop, pero es una función, no un método
# Con del puedo especificar desde una posición a otra (slicing)
del listaNombre[0:2]
# Vamos a recorrer la lista y mostrar su posicion
for i in range(len(listaNombre)):
    print(str(i) + "=" + listaNombre[i])
print("---------------------------")
# Clear borra el contenido de una lista
print("---------------------------")
#In
#Podemos preguntar si un elemento existe en la lista.


print("PREGUNTAMOS")
nombre= ["Benito", "Floro", "Alex", "Andrea", "Rosa", "Sara"]
print("Andrea" in nombre) #Preguntamos si el elemento Andrea existe en la lista
print("Pepito" in nombre) #Preguntamos si el elemento Pepito existe en la lista
print("---------------------------")
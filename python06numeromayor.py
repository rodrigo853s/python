print("Dame un número...")
numero = int(input())
print("Dame otro número...")
numero2 = int(input())
if (numero > numero2):
    #print("El numero mayor es ", numero) 
    print("El numero " + str(numero) + " es mayor que el numero " + str(numero2))
elif (numero2 > numero):
    #print("El numero mayor es ", numero2) 
    print("El numero " + str(numero2) + " es mayor que el numero " + str(numero))
else:
    print("Los numeros son iguales") 

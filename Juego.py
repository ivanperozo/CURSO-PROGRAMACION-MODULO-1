# Crea un juego donde el programa genera un número aleatorio entre 1 y 100. El 
# usuario debe adivinar este número. En cada intento, el programa debe darle una pista al usuario, 
# indicando si el número que ingresó es mayor


numero = input("Ingresa el numero: ")  

import random

numero_aleatorio = random.randint(1,100)

numero_adiv = int(numero)
print(f"El numero {numero}, puede ser el {numero_aleatorio}")

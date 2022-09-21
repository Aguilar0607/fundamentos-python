# Script que juega piedra papel y tijera con el usuario 
import random 

# Leer eleccion del usuario 
user = input("Elige: piedra, papel o tijera \n")

# Generar eleccion de la maquina 
aleatorio = random.randint(1, 3)
if aleatorio == 1:
    machine = "piedra"
elif aleatorio == 2:
    machine = "papel"
else:
    machine = "tijera"

# Comparar para determinar quien gana 
print((f"El usuario eligio {user} y la maquina eligio {machine}"))

if user == "piedra" and machine == "tijera":
    print('Gana el usuario')
elif user == "papel" and machine == "tijera":
    print('Gana la maquina')
elif user == "tijera" and machine == "tijera":
    print('Es un empate')

elif user == "piedra" and machine == "piedra":
    print('Es un empate')
elif user == "papel" and machine == "piedra":
    print('Gana la maquina')
elif user == "tijera" and machine == "piedra":
    print('Gana la maquina')
    
elif user == "piedra" and machine == "papel":
    print('Gana la maquina')
elif user == "papel" and machine == "papel":
    print('Es un empate')
elif user == "tijera" and machine == "papel":
    print('Gana el usuario')
else:
    print('Escribe bien tu eleccion')
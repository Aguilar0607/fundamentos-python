# Condicionales if elif else 
# Nos permite evaluar expresiones booleanas que de cumplirse realizan 
# Una accion y en caso de que no entonces realizan otra 

# Evaluar si una persona es mayor de edad
# Nos diga es niño, joven, adulto, bebe, muy mayor 

genre = input("Ingresa tu genero (H/M): ")
age = int(input('Ingresa tu edad: '))
mujer = ""

if genre == "M":
    mujer = "a"

if age < 2:
    print(f"Eres un{mujer} bebe")
elif age < 12:
    print(f'Eres un{mujer} niño')
elif age < 18:
    print(f'Eres un{mujer} joven')
elif age < 50:
    print(f'Eres un{mujer} adulto')
else:
    print("Eres muy mayor!")
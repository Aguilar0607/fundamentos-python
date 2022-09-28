from email import message


def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divided(num1, num2):
    return num1 / num2

if __name__ == '__main__':
    message = f"Calculadora: \n Elige una opcion\n 1 - Suma\n 2 - Resta\n 3 - Multiplicacion\n 4 - Division"   
    while True:
        opcion = int(input(message))
        if opcion == 5:
            print('Bye')
            break
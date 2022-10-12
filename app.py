
lista_elements = [
{
    "id": 1,
    "name" : "Emmanuel",
    "last_name" : "Aguilar"
},
{
    "id": 2,
    "name" : "Omar",
    "last_name" : "Flores"
}
]

def add_element():
    id = int(input(f"\nIngrese el ID de la persona: "))
    name = input(f"\nIngrese el nombre de la persona: ")
    last_name = input(f"\nIngrese el apellido de la persona: ")
    person = {
        "id": id,
        "name": name,
        "last_name": last_name
    }
    lista_elements.append(person)

def remove_element():
    id = int(input('Ingresa el ID del elemento a eliminar: '))
    found = find_element(id)    
    print(f"    {found}")
    aceptar = input(f"Estas seguro? (S/N)")
    if aceptar == "S":
        lista_elements.remove(found)
        print("Elemento eliminado")
    else:
        print("No se elimino el elemento")

def show_element():
    pass

def find_element(id):
    found = {}
    for element in lista_elements:
        if element['id'] == id:
            found = element
    return found

def show_elements():
    # print(lista_element)
    for element in lista_elements:
        for key, value in element.items():
            print(f"    {key} -> {value}")

def edit_element():
    id = int(input('Ingresa el ID del elemento a editar: '))
    found = find_element(id)    
    print(f"    {found}")
    index = lista_elements.index(found)
    name = input(f"\nIngresa el nuevo nombre, deja en blanco para conservar: ")
    last_name = input(f"\nIngresa el nuevo apellido, deja en blanco para conservar: ")
    if name != '':
        lista_elements[index]['name'] = name
    if last_name != '':
        lista_elements[index]['last_name'] = last_name
    
    # name = input(f"\nIngrese el nuevo nombre de la persona: ")
    # last_name = input(f"\nIngrese el nuevo apellido de la persona: ")
    # person = {
    #     "id": id,
    #     "name": name,
    #     "last_name": last_name
    # }
    # lista_elements.remove(found)
    # lista_elements.append(person)



if __name__ == '__main__':
    menu = '''
    Implementacion de CRUD de Elementos:
    
    Elige una Opcion
    
    1 - Insertar
    2 - Mostrar todos
    3 - Buscar por ID
    4 - Editar
    5 - Eliminar
    6 - Salir
    -------------------
    '''
    while True:
        opcion = input(menu)
        if opcion == '1':
            print('    Insertar elemento')
            add_element()
        elif opcion == '2':
            print(f'\n    Mostrar todos los elementos\n')
            show_elements()
        elif opcion == '3':
            print(f"\n    Busca por ID")
            id = int(input("Ingresa el ID a buscar: "))
            found = find_element(id)
            print(found)
        elif opcion == '4':
            print('    Editar elemento')
            edit_element()
        elif opcion == '5':
            print('    Eliminar elemento')
            remove_element()
        elif opcion == '6':
            print('    Bye!')
            break
        else:
            print('Opcion incorrecta')
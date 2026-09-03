usuario_valido = "admin"
contrasenia_encriptada = "EDQFR" # Contraseña encriptada "BANCO"
opcion_usuario = -1


def login():
    usuario = input("Ingrese su usuario: ").lower()
    contrasenia = input("Ingrese su contraseña: ")
    contrasenia = encriptar_contrasenia(contrasenia)

    while usuario != usuario_valido or contrasenia != contrasenia_encriptada:

        print("Usuario o contraseña incorrectos. Intente nuevamente.")

        usuario = input("Ingrese su usuario: ").lower()

        contrasenia = input("Ingrese su contraseña: ")
        contrasenia = encriptar_contrasenia(contrasenia)

    return True
   
        

def encriptar_contrasenia(contrasenia):
    contrasenia_encriptada = ""

    for caracter in contrasenia:
        codigo_ascii = ord(caracter)
        codigo_ascii = codigo_ascii + 3
        caracter_encriptado = chr(codigo_ascii)

        contrasenia_encriptada = contrasenia_encriptada + caracter_encriptado

    return contrasenia_encriptada   


def validar_enteros(minimo,maximo,mensaje,error):
    print(mensaje)
    opcion = input()
    while not opcion.isdigit() or int(opcion) < minimo or int(opcion) > maximo:
        print(error)
        opcion = input()

    return int(opcion)


def mostrar_menu():
    print("MENU PRINCIPAL")
    print("0. Instrucciones")
    print("1. Jugar")
    print("2. Cambiar contraseña")
    print("3. Cerrar sesión")

    opcion_usuario = validar_enteros(0,3,"Ingrese una opción del menu: ","Opción inválida. Ingrese nuevamente: ")

    return opcion_usuario

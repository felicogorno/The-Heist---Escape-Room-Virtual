def encriptar_contrasena(contrasena):
    contrasena_encriptada = ""

    for caracter in contrasena:
        contrasena_encriptada += chr(ord(caracter) + 3)

    return contrasena_encriptada


def desencriptar_contrasena(contrasena):
    contrasena_desencriptada = ""

    for caracter in contrasena:
        contrasena_desencriptada += chr(ord(caracter) - 3)

    return contrasena_desencriptada


def validar_credenciales(usuario, contrasena, usuario_correcto, contrasena_correcta):
    if usuario == usuario_correcto and contrasena == contrasena_correcta:
        return True
    else:
        return False


def login(usuario_correcto, contrasena_correcta):
    autentificado = False

    while autentificado == False:
        usuario = input("Ingrese su usuario: ")
        contrasena = input("Ingrese la contrasena: ")

        contrasena_encriptada = encriptar_contrasena(contrasena)

        validacion = validar_credenciales(usuario, contrasena_encriptada, usuario_correcto, contrasena_correcta)

        if validacion == True:
            print("Inicio de sesión exitoso. ¡Bienvenido!")
            autentificado = True
        else:
            print("Usuario o contraseña incorrectos.")

    return autentificado


usuario_correcto = "juniors"
contrasena_correcta = encriptar_contrasena("Banco123")

autentificado = login(usuario_correcto, contrasena_correcta)
# Practica 1
# criptografia
# Cifrado de Vigenere
# Integrantes
# Carlos Cruz Rangel
# Jose Demian Jimenez Salgado
# Victor Hugo Gallegos Mota


# alfabeto latino con la letra Ñ
LETRAS = ("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")

# ciframos un mensaje por medio de una clave "STRING" y un mensaje que le pasara el usuario


def cifrar_mensaje(clave, men):
    return traductor_mensaje(clave, men, 'encriptar')

# Desciframos el mensaje con la clave que se uso para cifrar "STRING" y un mensaje cifrado con vigenere


def descifrar_mensaje(clave, men):
    return traductor_mensaje(clave, men, 'descifrar')

# esta funcion es la que llevara a cabo el desencriptado o el encriptado al recibir la clave de cifrado
# el mesaje con el que trabajaremos y recibira tambien la opcion elegida por el usuario
# guardaremos el mensaje que se valla traduciendo en el arreglo mensaje traducido y es el que regresaremos


def traductor_mensaje(clave, men, operacion):
    mensajetraducido = []
    indice_clave = 0
    clave = clave.upper()

    for letras in men:
        num = LETRAS.find(letras.upper())
        if num != -1:
            if operacion == 'encriptar':
                num += LETRAS.find(clave[indice_clave])
            elif operacion == 'descifrar':
                num -= LETRAS.find(clave[indice_clave])
            num %= len(LETRAS)
            if letras.isupper():
                mensajetraducido.append(LETRAS[num])
            elif letras.islower():
                mensajetraducido.append(LETRAS[num].lower())
            indice_clave += 1
            if indice_clave == len(clave):
                indice_clave = 0

        else:
            mensajetraducido.append(letras)
    return ('').join(mensajetraducido)

# Metodo main el programa preguntara al usuario que operacion desea realizar
# si encriptar o desencriptar un mensaje
# El mensaje hay que meterlo sin espacios y en mayusculas


def main():
    # menu de opciones
    print('''   Cifrado de Vigenere     ''')
    print('''   1. Encriptar mensaje    ''')
    print('''   2. Desencriptar mensaje ''')
    print('''   3. Salir                ''')
    operacion = (input('Ingrese una opcion: '))
    if operacion == '1':
        mensaje = input("Mensaje: ")
        clavecif = "COMPU"
        print("clave: ", clavecif)
        print("Mensaje encriptado: ", cifrar_mensaje(clavecif, mensaje))
    elif operacion == '2':
        mensaje = input("Mensaje: ")
        clavecif = "COMPU"
        print("clave: ", clavecif)
        print("Mensaje desencriptado: ", descifrar_mensaje(clavecif, mensaje))
    elif operacion == '3':
        print("Adios")
    else:
        print('Solo se aceptan las opciones 1, 2 y 3')
        main()


if __name__ == '__main__':
    main()

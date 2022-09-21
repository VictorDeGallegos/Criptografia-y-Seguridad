# Autores
# Victor Hugo Gallegos Mota
# José Demian Jiménez
# Carlos Cruz Rangel

import numpy as np
import random
from sympy import Matrix

diccionario_encryt = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
                      'M': 12, 'N': 13, 'Ñ': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

diccionario_decrypt = {'0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '7': 'H', '8': 'I', '9': 'J', '10': 'K', '11': 'L', '12': 'M',
                       '13': 'N', '14': 'Ñ', '15': 'O', '16': 'P', '17': 'Q', '18': 'R', '19': 'S', '20': 'T', '21': 'U', '22': 'V', '23': 'W', '24': 'X', '25': 'Y', '26': 'Z'}


def uoc_hill_genkey(size):
    """
    Generador de claves para el cifrado Hill
    :size: tamaño de matriz
    :return: size x size matriz que contiene la clave
    """

    matrix = []

    L = []

    # Relleno una lista con tantos valores aleatorios como elementos a rellenar en la matriz determinada por size (size * size)

    for x in range(size * size):
        L.append(random.randrange(26))  # Se usa el 26 porque el modulo es 27

    # Se crea la matrix clave con los valores generados, de tamaño size * size

    matrix = np.array(L).reshape(size, size)

    return matrix


def uoc_hill_cipher(message, key):
    """
    Cifrado de Hill
    :message: Mensaje para cifrado (texto plano)
    :key: clave para usar al cifrar el mensaje (como lo devuelve por
          uoc_hill_genkey ())
    :return: ciphered text
    """

    ciphertext = ''

    # Variables

    matrix_mensaje = []
    list_temp = []
    ciphertext_temp = ''

    # Convertir el mensaje a mayusculas

    message = message.upper()

    # Si el tamaño del mensaje es menor o igual al tamaño de la clave

    if len(message) <= len(key):

        # Convertir el tamaño del mensaje al tamaño de la clave, si no es igual, se añaden 'X' hasta que sean iguales los tamaños.

        while len(message) < len(key):
            message = message + 'X'

        # Crear la matriz para el mensaje

        for i in range(0, len(message)):
            matrix_mensaje.append(diccionario_encryt[message[i]])

        # Se crea la matriz

        matrix_mensaje = np.array(matrix_mensaje)

        # Se multiplica la matriz clave por la de mensaje

        cifrado = np.matmul(key, matrix_mensaje)

        # Se obtiene el modulo sobre el diccionario de cada celda

        cifrado = cifrado % 27

        # Se codifica de valores numericos a los del diccionario, añadiendo a ciphertext el valor en el diccionario pasandole como indice la i posicion de la variable cifrado

        for i in range(0, len(cifrado)):
            ciphertext += diccionario_decrypt[str(cifrado[i])]
    else:

        # Si el tamaño del mensaje es menor o igual al tamaño de la clave

        # Si al dividir en trozos del tamaño de la clave, existe algun trozo que tiene menos caracteres que la long. de la clave se añaden tantas 'X' como falten

        while len(message) % len(key) != 0:
            message = message + 'X'

        # Se troce el mensaje en subsstrings de tamaño len(key) y se alamcenan como valores de un array

        matrix_mensaje = [message[i:i + len(key)] for i in range(0,
                          len(message), len(key))]

        # Para cada valor del array (grupo de caracteres de la longitud de la clave)

        for bloque in matrix_mensaje:

            # Crear la matriz para el bloque

            for i in range(0, len(bloque)):
                list_temp.append(diccionario_encryt[bloque[i]])

            # Se crea la matriz de ese bloque

            matrix_encrypt = np.array(list_temp)

            # Se multiplica la matriz clave por la del bloque

            cifrado = np.matmul(key, matrix_encrypt)

            # Se obtiene el modulo sobre el diccionario de cada celda

            cifrado = cifrado % 27

            # Se codifica de valores numericos a los del diccionario, añadiendo a ciphertext el valor en el diccionario pasandole como indice la i posicion de la variable cifrado

            for i in range(0, len(cifrado)):
                ciphertext_temp += diccionario_decrypt[str(cifrado[i])]

            # Se inicializan las variables para el nuevo bloque

            matrix_encrypt = []
            list_temp = []

        # Se añade el mensaje encriptado a la variable que contiene el mensaje encriptado completo

        ciphertext = ciphertext_temp

    # --------------------------------

    return ciphertext


def uoc_hill_decipher(message, key):
    """
    Descifrado de Hill
    :message: Mensaje para decifrar (texto cifrado)
    :key: clave para usar al descifrar el mensaje (como lo devuelve por
          uoc_hill_genkey ())
    :return: texto plano correspondiente al texto cifrado
    """

    plaintext = ''

    matrix_mensaje = []
    plaintext_temp = ''
    list_temp = []
    matrix_inversa = []
    matrix_mensaje = [message[i:i + len(key)] for i in range(0,
                      len(message), len(key))]

    # Se calcula la matriz inversa aplicando el modulo 27

    matrix_inversa = Matrix(key).inv_mod(27)

    # Se transforma en una matriz

    matrix_inversa = np.array(matrix_inversa)

    # Se pasan los elementos a float

    matrix_inversa = matrix_inversa.astype(float)

    # Para cada bloque

    for bloque in matrix_mensaje:

        # Se encripta el mensaje encriptado

        for i in range(0, len(bloque)):
            list_temp.append(diccionario_encryt[bloque[i]])

        # Se convierte a matriz

        matrix_encrypt = np.array(list_temp)

        # Se multiplica la matriz inversa por el bloque

        cifrado = np.matmul(matrix_inversa, matrix_encrypt)

        # Se le aplica a cada elemento el modulo 27

        cifrado = np.remainder(cifrado, 27).flatten()

        # Se desencripta el mensaje

        for i in range(0, len(cifrado)):
            plaintext_temp += diccionario_decrypt[str(int(cifrado[i]))]

        matrix_encrypt = []
        list_temp = []
    plaintext = plaintext_temp

    # Se eleminan las X procedentes de su addicion en la encriptacion para tener bloques del tamaño de la clave

    while plaintext[-1] == 'X':
        plaintext = plaintext.rstrip(plaintext[-1])

    return plaintext


def run():
    """
    Main function
    """
    # Menu para preguntar si desea encriptar o desencriptar
    print("1. Encriptar")
    print("2. Desencriptar")
    opcion = input("Introduzca una opcion: ")

    if opcion == "1":
        # Mensaje a encriptar ignorando los espacios
        message = input("Introduzca el mensaje a encriptar: ").replace(
            " ", "")
        # preguntar tamaño de la clave
        tam_clave = int(input("Introduzca el tamaño de la clave: "))
        # Generar clave
        key = uoc_hill_genkey(tam_clave)
        # introducir valores a la clave
        print("Introduzca los valores de la clave: ")
        for i in range(0, tam_clave):
            for j in range(0, tam_clave):
                key[i][j] = int(input())
        print("La clave es: \n", key)
        ciphertext = uoc_hill_cipher(message, key)
        print("El mensaje encriptado es:", ciphertext)
        # convertir a mayuscula message
        print("Texto plano:", message.upper())

    elif opcion == "2":
        # Desencriptar
        message = input("Introduzca el mensaje a desencriptar: ").replace(
            " ", "")
        # preguntar tamaño de la clave
        tam_clave = int(input("Introduzca el tamaño de la clave: "))
        # Generar clave
        key = uoc_hill_genkey(tam_clave)
        # introducir valores a la clave
        print("Introduzca los valores de la clave: ")
        for i in range(0, tam_clave):
            for j in range(0, tam_clave):
                key[i][j] = int(input())
        print("La clave es: \n", key)
        plaintext = uoc_hill_decipher(message, key)
        print("El mensaje desencriptado es: ", plaintext)

    else:
        print("OPCION INCORRECTA SOLO PUEDE INTRODUCIR 1 O 2")
        run()  # Se llama a si misma para hacer persistente el programa


if __name__ == '__main__':
    run()

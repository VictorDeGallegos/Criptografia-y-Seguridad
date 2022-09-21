# Programa de cifrado de Hill con una matriz de 2x2 en español con alfabeto sin librerías
# ----------------------------------
# Integrantes de Equipo:
# Jose Demian Jimenez Salgado
# Carlos Cruz Rangel
# Victor Hugo Gallegos Mota
# ----------------------------------


# convertir matrix string key

def convertKey(key):
    alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    # key a mayúscula
    key = key.upper()
    # key a lista
    key = list(key)
    # key a  números
    key = [alphabet.index(letter) for letter in key]
    # key a Matrix
    key = [key[i:i+2] for i in range(0, len(key), 2)]
    # return
    return key


# función para cifrar con la matriz de la clave y el mensaje dado
def encrypt(matrix, message, alphabet):
    # Mensaje a mayúscula
    message = message.upper()
    # Mensaje a  lista
    message = list(message)
    # Mensaje a  números
    message = [alphabet.index(letter) for letter in message]
    # Mensaje a Matrix
    message = [message[i:i+2] for i in range(0, len(message), 2)]
    # Encriptar
    encrypted = ""
    for i in range(len(message)):
        encrypted += alphabet[(matrix[0][0] * message[i]
                               [0] + matrix[0][1] * message[i][1]) % len(alphabet)]
        encrypted += alphabet[(matrix[1][0] * message[i]
                               [0] + matrix[1][1] * message[i][1]) % len(alphabet)]
    # Return
    return encrypted


# Funcion para encriptar con key tipo string y el mensaje dado
def encrypt_with_key(key, message, alphabet):
    # Mensaje a mayúscula
    message = message.upper()
    # Mensaje a  lista
    message = list(message)
    # Mensaje a  números
    message = [alphabet.index(letter) for letter in message]
    # Mensaje a Matrix
    message = [message[i:i+2] for i in range(0, len(message), 2)]
    # Encriptar
    encrypted = ""
    for i in range(len(message)):
        encrypted += alphabet[(key[0][0] * message[i]
                               [0] + key[0][1] * message[i][1]) % len(alphabet)]
        encrypted += alphabet[(key[1][0] * message[i]
                               [0] + key[1][1] * message[i][1]) % len(alphabet)]
    # Return
    return encrypted


# funcion para desencriptar con key tipo string y el mensaje dado
def decrypt_with_key(key, message, alphabet):
    # Mensaje a mayúscula
    message = message.upper()
    # mensaje a  lista
    message = list(message)
    # mensaje a  números
    message = [alphabet.index(letter) for letter in message]
    # mensaje a Matrix
    message = [message[i:i+2] for i in range(0, len(message), 2)]

    # matriz inversa para descifrar
    inverse_matrix = [[key[1][1], -key[0][1]],
                      [-key[1][0], key[0][0]]]
    # determinante de la matriz
    determinant = key[0][0] * key[1][1] - key[0][1] * key[1][0]
    # Determinante Mod 27
    determinant = determinant % len(alphabet)
    # inverso multiplicativo determinante
    for i in range(len(alphabet)):
        x = determinant * i
        if x % len(alphabet) == 1:
            determinant = i
            break
    # matriz inversa
    for i in range(2):
        for j in range(2):
            inverse_matrix[i][j] = inverse_matrix[i][j] * determinant

    # descifrar
    decrypted = ""
    for i in range(len(message)):
        decrypted += alphabet[(inverse_matrix[0][0] * message[i]
                               [0] + inverse_matrix[0][1] * message[i][1]) % len(alphabet)]
        decrypted += alphabet[(inverse_matrix[1][0] * message[i]
                               [0] + inverse_matrix[1][1] * message[i][1]) % len(alphabet)]
    # return
    return decrypted


# función para descifrar con la matriz de la clave y el mensaje dado
def decrypt(matrix, message, alphabet):
    # Mensaje a mayúscula
    message = message.upper()
    # mensaje a  lista
    message = list(message)
    # mensaje a  números
    message = [alphabet.index(letter) for letter in message]
    # mensaje a Matrix
    message = [message[i:i+2] for i in range(0, len(message), 2)]

    # matriz inversa para descifrar
    inverse_matrix = [[matrix[1][1], -matrix[0][1]],
                      [-matrix[1][0], matrix[0][0]]]
    # determinante de la matriz
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    # Determinante Mod 27
    determinant = determinant % len(alphabet)
    # inverso multiplicativo determinante
    for i in range(len(alphabet)):
        x = determinant * i
        if x % len(alphabet) == 1:
            determinant = i
            break
    # matriz inversa
    for i in range(2):
        for j in range(2):
            inverse_matrix[i][j] = inverse_matrix[i][j] * determinant

    # descifrar
    decrypted = ""
    for i in range(len(message)):
        decrypted += alphabet[(inverse_matrix[0][0] * message[i]
                               [0] + inverse_matrix[0][1] * message[i][1]) % len(alphabet)]
        decrypted += alphabet[(inverse_matrix[1][0] * message[i]
                               [0] + inverse_matrix[1][1] * message[i][1]) % len(alphabet)]
    # return
    return decrypted


def main():  # Función principal
    # alfabeto
    alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    # Matrix
    matrix = [[1, 2], [3, 4]]
    key = 'BCDE'
    # mensaje
    message = input("Ingrese el mensaje : ")
    # Encriptar
    encrypted = encrypt(matrix, message, alphabet)
    encrypted_with_key = encrypt_with_key(
        convertKey(key), message, alphabet)
    # print convertKey
    print("Matrix: " + str(matrix))
    print("Matrix Key: " + str(convertKey("BCDE")))
    print("Matrix Key String = BCDE")
    print("\n")
    # Print
    print("Texto plano: " + message)
    print("Encriptado con matrix: " + encrypted)
    print("Encriptado con Key String: " + encrypted_with_key)
    print("\n")

    messa_encrypted = "CQÑO"
    decrypted = decrypt(matrix, messa_encrypted, alphabet)
    decrypted_with_key = decrypt_with_key(
        convertKey(key), messa_encrypted, alphabet)
    # print decrypted
    print("Descifrado con matrix: " + decrypted)
    print("Descifrado con Key String: " + decrypted_with_key)


if __name__ == "__main__":
    main()

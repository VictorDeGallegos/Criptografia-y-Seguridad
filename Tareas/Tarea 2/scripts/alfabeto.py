import math

# ---Desarrolladores---
# Victor Hugo Gallegos Mota
# José Demian Jiménez
# Carlos Cruz Rangel


def is_prime(n):
    """
    Verifica si un número es primo.

    :param n: Número a verificar
    :type n: int
    :return: True si el número es primo, False si no lo es.
    :rtype: bool
    """
    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True


def gcd(a, b):
    """
    Calcula el Máximo Común Divisor de dos números.

    :param a: Primer número
    :type a: int
    :param b: Segundo número
    :type b: int
    :return: Máximo Común Divisor
    :rtype: int
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def mod_inverse(a, m):
    """
    Calcula el módulo inverso de un número.

    :param a: Número a calcular su inverso
    :type a: int
    :param m: Módulo
    :type m: int
    :return: módulo inverso de `a`
    :rtype: int
    """
    a = a % m

    for x in range(1, m):
        if (a * x) % m == 1:
            return x

    return 1


def generate_keypair(p, q):
    """
    Genera las llaves pública y privada.

    :param p: Primer número primo
    :type p: int
    :param q: Segundo número primo
    :type q: int
    :return: Llaves pública y privada
    :rtype: tuple
    """
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Ambos números deben ser primos.')

    elif p == q:
        raise ValueError('p y q no pueden ser iguales')

    # n = pq
    n = p * q

    # phi = (p-1)(q-1)
    phi = (p - 1) * (q - 1)

    # Elegir un número entero e tal que e y phi(n) sean primos entre sí.
    e = 11

    # Utilizar el algoritmo de Euclides para verificar que e y phi(n) son primos entre sí.
    g = gcd(e, phi)

    while g != 1:
        e = 7
        g = gcd(e, phi)

    # Utilizar el algoritmo extendido de Euclides para generar la llave privada.
    d = mod_inverse(e, phi)

    # Retornar la llave pública (e, n) y la llave privada (d, n)
    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    """
    Encripta un mensaje.

    :param pk: Llave pública
    :type pk: tuple
    :param plaintext: Mensaje a encriptar
    :type plaintext: str
    :return: Lista de enteros
    :rtype: list
    """
    # Desempaquetar la llave pública
    key, n = pk

    # Convertir cada letra en su representación entera
    cipher = [pow(ord(char), key, n) for char in plaintext]

    # Retornar la lista de enteros
    return cipher


def decrypt(pk, ciphertext):
    """
    Desencripta un mensaje.

    :param pk: Llave privada
    :type pk: tuple
    :param ciphertext: Mensaje a desencriptar
    :type ciphertext: list
    :return: Mensaje desencriptado
    :rtype: str
    """
    # Desempaquetar la llave privada
    key, n = pk

    # Generar el texto desencriptado basado en el texto encriptado y la llave privada
    plain = [chr(pow(char, key, n)) for char in ciphertext]

    # Retornar el string de texto desencriptado
    return ''.join(plain)


if __name__ == '__main__':
    # Ejemplo de ejecución
    print('RSA Encrypter/ Decrypter')
    q = 2791
    p = 2789
    print('Generando tu llave pública/privada ahora . . .')
    public, private = generate_keypair(p, q)
    print('Tu llave pública es ', public, ' y tu llave privada es ', private)
    # obtener cifrado de cada letra del alfabeto
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    for letra in alfabeto:
        print(letra, encrypt(public, letra))

import math
# ---Desarrolladores---
# Victor Hugo Gallegos Mota
# José Demian Jiménez
# Carlos Cruz Rangel

# ---Fecha de creación---
# 07/11/2021


# Variables globales para el programa
p = 0
q = 0


def criba_cuadratica():
    # Función para factorizar un número usando la criba cuadratica
    """
    Factoriza un número usando la criba cuadrática.

    :param n: Número a factorizar
    :type n: int
    :return: Lista con los factores
    :rtype: list
    """
    n = 4245221
    x = int(math.sqrt(n))
    y = 0

    while x * x - y * y != n:  # Mientras x^2 - y^2 != n
        x = x + 1        # x = x + 1
        y = int(math.sqrt(x * x - n))  # y = sqrt(x^2 - n)

    # Agregar los factores a las variables globales p y q
    global p
    global q
    p = x + y
    q = x - y

    # imprimir cotas de base e intervalo
    print("Cotas de base e intervalo")
    print("x = " + str(x))
    print("y = " + str(y))

    # Proporcione las i de q(i) con las cuales se obtiene la soluci ́on, x, y tales que (x−y, n) = d donde de es un factor primo de n.
    print("Proporcione las i de q(i) con las cuales se obtiene la solución, x, y tales que (x−y, n) = d donde de es un factor primo de n.")
    print("i = " + str(x + y))  # i = x + y
    print("i = " + str(x - y), end="\n\n")  # i = x - y

    # imprimir la base
    print("Base")
    print("b = " + str(x + y))

    return [p, q]


def is_prime(n):  # Verifica si un número es primo
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


def mcd(a, b):  # Calcula el máximo común divisor
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
        return mcd(b, a % b)


def mod_inverse(a, m):  # Calcula el inverso modular
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


def generate_keypair(p, q):  # Genera una llave pública y privada
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
    e = 61

    # Utilizar el algoritmo de Euclides para verificar que e y phi(n) son primos entre sí.
    g = mcd(e, phi)

    while g != 1:
        e = 61
        g = mcd(e, phi)

    # Utilizar el algoritmo extendido de Euclides para generar la llave privada.
    d = mod_inverse(e, phi)

    # Retornar la llave pública (e, n) y la llave privada (d, n)
    return ((e, n), (d, n))


def calculae(phi):  # Calcula el valor de e
    """
    Calcula el valor de e.

    :param phi: Valor de phi
    :type phi: int
    :return: Valor de e
    :rtype: int
    """

    e = 2
    le = []
    while e > 1 and e < phi:
        if mcd(e, phi) == 1:
            le.append(e)
            e = e+1
        else:
            e = e+1
    # print("\nVALORES PARA (e)="+str(le))
    e = 61
    print("(e)="+str(e), end="\n\n")
    while mcd(e, phi) != 1:
        print("\n\tEliga un valor valido !!!")
        e = int(input("(e)="), end="\n\n")
    return e


def encrypt(pk, plaintext):  # Encripta un mensaje
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


def decrypt(pk, ciphertext):  # Desencripta un mensaje
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
    print('RSA Cifrado/ Descifrado', end='\n\n')
    # ELEGIMOS VALORES DE NUMEROS PRIMOS PARA (p) y (q)
    print('ELEGIMOS VALORES DE NUMEROS PRIMOS PARA (p) y (q) ')
    # get_p_q()
    # pollard()
    criba_cuadratica()

    # CALCULAMOS EL VALOR DE (n) o llave pública
    print('CALCULAMOS EL VALOR DE (n)')
    print("(n)=(p)*(q)")
    n = p * q
    print("(n)=("+str(p)+")*("+str(q)+")")
    print('(n):', n, end='\n\n')

    # CALCULAMOS EL VALOR DE (phi) o llave privada
    print('CALCULAMOS EL VALOR DE (phi)')
    print("(phi)=(p-1)*(q-1)")
    phi = (p - 1) * (q - 1)
    print("(phi)=("+str(p)+"-1)*("+str(q)+"-1)")
    print('(phi):', phi, end='\n\n')

    # ELEGIMOS UN VALOR DE (e) PARA LA LLAVE PUBLICA
    print('ELEGIMOS UN VALOR DE (e) PARA LA LLAVE PUBLICA')
    print("(e)/  1<e<phi and mcd(e,phi)==1")
    e = calculae(phi)

    # CALCULAMOS EL VALOR DE (d) PARA LA LLAVE PRIVADA
    print('CALCULAMOS EL VALOR DE (d) PARA LA LLAVE PRIVADA')
    print("(d)=e^-1 mod phi")
    d = mod_inverse(e, phi)
    print("(d)=("+str(e)+")^-1 mod ("+str(phi)+")")
    print('(d):', d, end='\n\n')

    # CALCULAMOS LLA LLAVE PUBLICA Y PRIVADA
    print('Generando la llave pública y privada . . .')
    public, private = generate_keypair(p, q)
    print('Llave pública:', public)
    print('Llave privada:', private, end='\n\n')

    # CIFRAMOS CADA LETRA DEL ALFABETO
    print('Cifrado de cada letra del alfabeto')
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    for letra in alfabeto:
        print(letra, encrypt(public, letra))

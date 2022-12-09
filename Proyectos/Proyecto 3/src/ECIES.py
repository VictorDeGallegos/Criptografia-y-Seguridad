# ---Desarrolladores---
# Victor Hugo Gallegos Mota
# José Demian Jiménez
# Carlos Cruz Rangel


# Definimos el criptosistema: K = {(E, P, m, Q, n): Q = mP}

# Variables globales de la curva elíptica
global a, b, p  # Función E: f(x) = x^3 + a*x + b (mod p)
global P  # P Punto generado (es una clave pública): P = (x_p, y_p)
global m  # m  (es una clave privada)
global Q  # Q (es una clave pública): Q = (x_q, y_q)
global n  # n (es una clave pública)


def jacobi(a, p):  # Función de Jacobi
    if a == 0 or a == 1:
        return a
    else:
        if pow(a, (p - 1) // 2, p) == 1: # a^((p-1)/2) mod p
            return 1
        else:
            return -1
    # return pow(a, (p - 1) // 2, p)


def tonelli(n, p): # Función de Tonelli-Shanks
    if jacobi(n, p) != 1:
        return 0
    elif n == 0:
        return 0
    elif p == 2:
        return p
    elif p % 4 == 3:
        return pow(n, (p + 1) // 4, p) # n^((p+1)/4) mod p

    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1

    z = 1
    while jacobi(z, p) != -1:
        z += 1

    c = pow(z, q, p) # z^q mod p
    r = pow(n, (q + 1) // 2, p) # n^((q+1)/2) mod p
    t = pow(n, q, p) # n^q mod p
    m = s
    t2 = 0

    while t != 1:
        t2 = t2 + pow(t, 2, p)
        i = 0
        while t2 % 2 == 0:
            t2 //= 2
            i += 1
        b = pow(c, 2 ** (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i

    return r


def descomprimir_punto(x):  # Descomprime un punto comprimido

    z = (pow(x[0], 3) + a*x[0] + b) % p  # z = x^3 + ax + b

    y = tonelli(z, p)
    if y % 2 == x[1] % 2:
        return x[0], y
    else:
        return x[0], p - y


def comprimir_punto(x):  # Comprime un punto

    return x[0], x[1] % 2


def encriptar_textoplano(x, k):  # Encriptar texto plano

    kP = multiplicar(k, P)
    kQ = multiplicar(k, Q)
    x0 = kQ[0]
    return comprimir_punto(kP), (x*x0) % p


def desencriptar_textoplano(y):  # Descifrar texto cifrado
    y1 = y[0]
    y2 = y[1]
    punto_descomprimido = multiplicar(m, descomprimir_punto(y1))
    x0 = punto_descomprimido[0]
    return (y2 * inverso_modular(x0, p)) % p


def multiplicar(k, A):  # Multiplicación de puntos

    N1 = A
    N2 = 'Origen'
    stringK = bin(k)
    klen = len(stringK)

    for i in range(klen-1, 1, -1):
        if stringK[i] == '1':
            N2 = sumar_puntos(N2, N1)

        N1 = sumar_puntos(N1, N1)
    return N2


def inverso_modular(x, mod):  # Inverso modular

    if x % mod == 0:
        raise Exception('El inverso modular no existe')
    return pow(x, mod-2, mod)


def sumar_puntos(x, y):  # Suma de puntos

    if x == 'Origen':
        return y
    elif y == 'Origen':
        return x
    if x[0] == y[0]:
        if x[1] == y[1]:
            slope = ((3 * (pow(x[0], 2)) + a) %
                     p) * inverso_modular((2*x[1]), p)
            slope = slope % p
        else:
            return 'Origen'
    else:
        slope = ((y[1] - x[1]) % p) * inverso_modular((y[0] - x[0]), p)
        slope = slope % p
    x3 = ((pow(slope, 2)) - x[0] - y[0]) % p
    y3 = (slope * (x[0] - x3) - x[1]) % p

    return x3, y3


# Configuración de E
# Función E: f(x) = x^3 + a*x + b (mod p)
a = -3
b = 0x64210519E59C80E70FA7E9AB72243049FEB8DEECC146B9B1
p = (pow(2, 192) - pow(2, 64) - 1)


# Configuración de P
# P Punto generado (es una clave pública): P = (x_p, y_p)
P = (0x188da80eb03090f67cbf20eb43a18800f4ff0afd82ff1012,
     0x07192b95ffc8da78631011ed6b24cdd573f977a11e794811)

# Configuración de m
# m  (es una clave privada)
m = 87686

#  Configuración de Q
# Q (es una clave pública): Q = (x_q, y_q)
Q = multiplicar(m, P)

# Configuración de n
# n (es una clave pública)
n = 0xFFFFFFFFFFFFFFFFFFFFFFFF99DEF836146BC9B1B4D22831

O = 'Origen'  # Punto de origen


def main():
    # ---Desarrolladores---
    # Victor Hugo Gallegos Mota
    # José Demian Jiménez
    # Carlos Cruz Rangel

    # Encriptar texto plano
    texto_planonormal = "Hola Mundo" # Texto plano
    #convertir texto plano a hexadecimal
    texto_plano = int.from_bytes(texto_planonormal.encode(), 'big')
    k = 123456789  # Clave secreta
    print('Texto plano: ', texto_planonormal)
    print('Texto plano en hexadecimal: ', hex(texto_plano))
    print('Clave pública: ', hex(n))
    print('Clave privada: ', hex(m))
    print('Punto generado: ', hex(P[0]), hex(P[1]))
    print('Punto público: ', hex(Q[0]), hex(Q[1]))
    print('Clave de encriptación: ', hex(k))
    texto_cifrado = encriptar_textoplano(texto_plano, k)
    print('Texto cifrado: ', hex(texto_cifrado[0][0]), hex(
        texto_cifrado[0][1]), hex(texto_cifrado[1]))

    # Descifrar texto cifrado
    print('Texto descifrado en hexadecimal: ', hex(desencriptar_textoplano(texto_cifrado)))
    
    print('Texto descifrado en lenguaje normal: ', desencriptar_textoplano(texto_cifrado).to_bytes((desencriptar_textoplano(texto_cifrado).bit_length() + 7) // 8, 'big').decode())
    

    if texto_plano == desencriptar_textoplano(texto_cifrado):  # Comprobar
        print("Éxito! 😊")
    else:
        print("Falló! 😢")
        



if __name__ == "__main__":
    main()

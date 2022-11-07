# ---Desarrolladores---
# Victor Hugo Gallegos Mota
# José Demian Jiménez
# Carlos Cruz Rangel

import random
import math


class RSA:
    def __init__(self, bit_length):
        # Para asegurar que la longitud del primo es de al menos 100 dígitos
        self.bit_length = bit_length

        # Dos números primos aleatorios
        self.p = self.get_probable_prime()
        self.q = self.get_probable_prime()
        # n = p*q
        self.n = self.p * self.q
        # Cota superior de e
        self.phi = (self.p - 1) * (self.q - 1)

        self.e_aux = self.get_probable_prime()
        # e tal que 1 < e < phi(n) y mcd(e, phi(n)) = 1
        self.e = self.get_e()
        # Satisface la congruencia de \cog \mod{\phi(n)}
        self.d = self.get_d()

    def get_probable_prime(self):  # Genera un número primo aleatorio
        return random.getrandbits(self.bit_length)

    def get_e(self):    # Calcula el valor de e
        while math.gcd(self.phi, self.e_aux) > 1:
            self.e_aux += 1

        return self.e_aux

    def get_d(self):   # Calcula el valor de d
        return pow(self.e, -1, self.phi)

    def encrypt(self, msg):  # Cifra el mensaje
        length = len(msg)
        arr_r = []

        for i in range(length):
            arr_r.append(pow(ord(msg[i]), self.e, self.n))

        return arr_r

    def decrypt(self, m):  # Descifra el mensaje
        length = len(m)
        arr_r = []

        for i in range(length):
            arr_r.append(chr(pow(m[i], self.d, self.n)))

        return ''.join(arr_r)


def main():  # Función principal
    # Creación de la instancia del cifrado RSA
    # 512 bits de longitud para que los primos sean de al menos 100 dígitos
    rsa = RSA(512)  # bajar a 10 para probar
    # Valor a usar en el cifrado y descifrado
    n = rsa.n
    e = rsa.e
    d = rsa.d

    # llave p y q
    print("Llave p: ", rsa.p)
    print("Llave q: ", rsa.q)
    print("--------------------------------")

    # N, e, d
    print("N = {}".format(n))
    print("--------------------------------")
    print("e = {}".format(e))
    print("d = {}".format(d))
    print("--------------------------------")

    # Mensaje a cifrar
    print("Mensaje a cifrar:")
    msg = "niño"
    print(msg)

    encrypted_message = rsa.encrypt(msg)

    print("Mensaje cifrado:")
    print(encrypted_message)

    print("--------------------------------")
    print("Mensaje descifrado:")

    # mensaje descifrado  (bug con 512 bits)
    decrypted_message = rsa.decrypt(encrypted_message)
    print(decrypted_message)


if __name__ == "__main__":
    main()

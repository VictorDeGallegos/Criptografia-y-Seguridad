# Hecho por Javatar
import random
import math
# importar sys.maxsize
from sys import maxsize


class RSA:
    def __init__(self, bit_length):
        # Para asegurar que la longitud del primo es de al menos 100 dígitos
        self.bit_length = bit_length

        # Dos números primos aleatorios
        self.p = self.get_probable_prime()
        self.q = self.get_probable_prime()
        # $n = p*q$
        self.n = self.p * self.q
        # Cota superior para elegir `e`
        self.phi = (self.p - 1) * (self.q - 1)

        self.e_aux = self.get_probable_prime()
        # $e$ tal que $gcd(e,\phi(n)) = 1$
        self.e = self.get_e()
        # Satisface la congruencia $de \cog \mod{\phi(n)}$
        self.d = self.get_d()

    def get_probable_prime(self):
        return random.getrandbits(self.bit_length)

    def get_e(self):
        while math.gcd(self.phi, self.e_aux) > 1:
            self.e_aux += 1

        return self.e_aux

    def get_d(self):
        return pow(self.e, -1, self.phi)

    def encrypt(self, msg):
        length = len(msg)
        arr_r = []

        for i in range(length):
            arr_r.append(pow(ord(msg[i]), self.e, self.n))

        return arr_r

    def decrypt(self, m):
        length = len(m)
        arr_r = []

        for i in range(length):
            arr_r.append(chr(pow(m[i], self.d, self.n)))

        return ''.join(arr_r)


def main():
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

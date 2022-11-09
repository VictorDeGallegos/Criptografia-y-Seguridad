# ---Desarrolladores---
# Victor Hugo Gallegos Mota
# José Demian Jiménez
# Carlos Cruz Rangel


# ---Fecha de creación---
# 09/11/2021


import math

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

# Variables globales para el programa
p = 0
q = 0

def pollard():
    """
    Algoritmo de Pollard para factorizar números grandes.
    return: Tupla con los valores de p y q
    rtype: tuple
    """
    n = 1148289976600001  # Valor de n, cambiarlo si se desea
    x = 2  # Valor inicial de x
    y = 2  # Valor inicial de y
    d = 1  # Valor inicial de d
    iteraciones = 0
    while d == 1:
        x = (x**2 + 1) % n  # f(x) = x^2 + 1
        y = (y**2 + 1) % n  # f(y) = y^2 + 1
        y = (y**2 + 1) % n  # f(y) = y^2 + 1
        d = mcd(abs(x-y), n)  # d = mcd(|x-y|, n)
        iteraciones += 1
        print("Iteraciones realizadas:", iteraciones, d)

    # Agregar los factores a las variables globales p y q
    global p
    p = d
    global q
    q = n//d
    # Imprimir los valores de p y q
    print("p =", d)
    print("q =", n//d)

    # Imprimir funcion semialeatoria del algoritmo
    print("f(x) = x^2 + 1")
 
# Driver function
if __name__ == "__main__":
 
   
    print(pollard())
     
# This code is contributed by chitranayal
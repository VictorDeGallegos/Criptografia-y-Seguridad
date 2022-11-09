# ---Desarrolladores---
# Victor Hugo Gallegos Mota
# José Demian Jiménez
# Carlos Cruz Rangel


# ---Fecha de creación---
# 09/11/2021

import random
 
# Funcion para calcular (a^n)%p

def potencia(a, n, p):
     
    # resultado inicial
    res = 1
     
    #  Si a es mayor igual a p actualizamos a 
    a = a % p 
     
    while n > 0:
         
        # Si n es impar entonces el resultado es igual al resultado *a
        if n % 2:
            res = (res * a) % p
            n = n - 1
        else:
            a = (a ** 2) % p
            n = n // 2
             
    return res % p
     
# Si n es primo entonces regresamos un true caso contrario falso
# entre mas iteraciones halla habra mas posibilidades de encontrar el resultado deseado
def esPrimo(n, k):
     
    if n == 1 or n == 4:
        return False
    elif n == 2 or n == 3:
        return True
     
   
    else:
        for i in range(k):
             
            # Agarramos un numero de forma aleatoria en el intervalo [2..n-2]
            a = random.randint(2, n - 2)
             
            # Teorema de fermat
            if potencia(a, n - 1, n) != 1:
                return False
                 
    return True
             
if __name__ == "__main__":
    k = 5 ##iteraciones 

    if esPrimo(1148289976600001, k):
        print("true")
    else:
        print("false")
   

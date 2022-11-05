# ---Desarrolladores---
# Victor Hugo Gallegos Mota
# José Demian Jiménez
# Carlos Cruz Rangel

# Script para encontrar 2 numeros que multiplciados me den un numero n

def multiplicacion():
    n = 7784099
    x = 2
    while n != 1:  # Mientras n sea diferente de 1
        if n % x == 0:  # Si el residuo de n entre x es 0
            print(x)  # Imprime x
            n = n/x  # n es igual a n entre x
        else:
            x = x+1  # Si no x es igual a x mas 1


multiplicacion()

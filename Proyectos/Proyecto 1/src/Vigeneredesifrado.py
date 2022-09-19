##Practica 1
##Desifrado de vigenere

clave='LATIN'

def crackeaVinegere(x, k):
    ind1 = ord(x)-65
    ind2 = ord(k)-65
    return (ind1-ind2)%26

def desencripta(archivo):
    file = open(archivo,'r')
    texto = file.readlines()
    r = ''
    i = 0
    for line in texto:
        for char in line:
            if char.isalpha():
                c = clave[i%len(clave)]
                r = chr(crackeaVinegere(char, c)+65)
                print(r, end='')
                i += 1
            else:
                print(char, end='')

desencripta('archivo.txt')
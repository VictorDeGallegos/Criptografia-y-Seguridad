##Practica 1
##Desifrado de vigenere
##Integrantes de Equipo 
##Jose Demian Jimenez Salgado
##Carlos Cruz Rangel
##Victor Hugo Gallegos Mota

##Clave de Vigenere
clave='LATIN'

##Funcion para llevar a cabo el ataque a vigenere
def crackeaVinegere(x, k):
    ind1 = ord(x)-65
    ind2 = ord(k)-65
    return (ind1-ind2)%26

##funcion para leer un archivo de texto el cual se va a desencriptar
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
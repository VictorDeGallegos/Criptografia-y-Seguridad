# Tarea 1
# Desifrado de vigenere
# Integrantes de Equipo
# Jose Demian Jimenez Salgado
# Carlos Cruz Rangel
# Victor Hugo Gallegos Mota
from pathlib import Path
# Clave de Vigenere
clave = 'LATIN'

# Funcion para llevar a cabo el ataque a vigenere


def crackeaVinegere(x, k):
    ind1 = ord(x)-65
    ind2 = ord(k)-65
    return (ind1-ind2) % 26

# funcion para leer un archivo de texto el cual se va a desencriptar


def desencripta(file_path):
    file_path = Path(r"textos/archivovigenere.txt")
    f = open(file_path)  # abrir el archivo
    texto = f.readlines()
    r = ''
    i = 0
    for line in texto:
        for char in line:
            if char.isalpha():
                c = clave[i % len(clave)]
                r = chr(crackeaVinegere(char, c)+65)
                print(r, end='')
                i += 1
            else:
                print(char, end='')


# funcion para leer un archivo de texto el cual se va a desencriptar
if __name__ == '__main__':
    file_path = Path(r"textos/archivovigenere.txt")
    # descencripta el archivo
    desencripta(file_path)

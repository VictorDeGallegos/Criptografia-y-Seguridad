# Tarea 1
# Desifrado de frecuencias
# Integrantes de Equipo:
# Jose Demian Jimenez Salgado
# Carlos Cruz Rangel
# Victor Hugo Gallegos Mota

from pathlib import Path


def frecuencias(file_path):

    file_path = Path(r"textos/archivo.txt")
    f = open(file_path)  # abrir el archivo

    text = f.readlines()
    # Lista con 3 valores
    # El primero la letra correspondiente, la frecuencia
    # y porcentaje, respectivamente.
    l = [[chr(65+i), 0, ''] for i in range(26)]
    total = 0  # total de letras
    for line in text:
        for char in line:
            if (char == ' ' or char == '\n' or char == '.'):
                continue
            else:
                l[ord(char)-65][1] += 1  # Aumentar frecuencia
                total += 1
    for i in range(len(l)):
        # Porcentaje
        l[i][2] = (l[i][1]*100) / total
        l[i][2] = format(l[i][2], '.2f')  # 2 decimales
    # Ordenar de mayor a menor con respecto a la frecuencia
    l.sort(key=lambda x: x[1], reverse=True)
    return l


def sustitucion(file_path):
    file_path = Path(r"textos/archivo.txt")
    f = open(file_path)  # abrir el archivo
    text = f.readlines()
    for line in text:
        for char in line:
            if char == 'R':
                print('e', end='')
            elif char == 'L':
                print('a', end='')
            elif char == 'Q':
                print('s', end='')
            elif char == 'M':
                print('o', end='')
            elif char == 'K':
                print('n', end='')
            elif char == 'I':
                print('l', end='')
            elif char == 'E':
                print('d', end='')
            elif char == 'O':
                print('q', end='')
            elif char == 'B':
                print('f', end='')
            elif char == 'T':
                print('t', end='')
            elif char == 'C':
                print('g', end='')
            elif char == 'J':
                print('m', end='')
            elif char == 'F':
                print('i', end='')
            elif char == 'S':
                print('c', end='')
            elif char == 'P':
                print('r', end='')
            elif char == 'N':
                print('p', end='')
            elif char == 'U':
                print('u', end='')
            elif char == 'Y':
                print('y', end='')
            elif char == 'A':
                print('b', end='')
            elif char == 'V':
                print('v', end='')
            elif char == 'D':
                print('h', end='')
            elif char == 'G':
                print('j', end='')
            elif char == 'H':
                print('k', end='')
            elif char == 'Z':
                print('z', end='')
            elif char == 'X':
                print('x', end='')
            elif char == 'W':
                print('w', end='')
            else:
                print(char, end='')
    f.close()


def main():
    # imprimir en forma de tabla las frecuencias de las letras
    print("Frecuencias de las letras:")
    print("Letra\tFrecuencia\tPorcentaje")
    for i in frecuencias("archivo.txt"):
        print(i[0], '\t', i[1], '\t\t', i[2], '%')
    print('\n')

    # Mostrar el texto con las letras  sustituidas
    print("Texto con las letras SUSTITUIDAS: \n")
    sustitucion("archivo.txt")


if __name__ == '__main__':
    main()

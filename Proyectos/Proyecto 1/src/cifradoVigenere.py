##Practica 1
#criptografia
##Cifrado de Vigenere
#Integrantes 
#Carlos Cruz Rangel
#Jose Demian Jimenez Salgado
#Victor Hugo Gallegos Mota

##funcion para generar la clave de cifrado
##de forma ciclica hasta que 
#la longitud de la llave sea distinta a  
#la longitud del texto original
def generaClave(string, clave):
    clave = list(clave)
    if len(string) == len(clave):
        return(clave)
    else:
        for i in range(len(string) -
                       len(clave)):
            clave.append(clave[i % len(clave)])
    return("" . join(clave))

##LA siguiente funcion se encargara de 
#encriptar el texto con la clave generada 
#previamente

def cifraTexto(string, clave):
    textocifrado = []
    for i in range(len(string)):
        x = (ord(string[i]) +
             ord(clave[i])) % 26
        x += ord('A')
        textocifrado.append(chr(x))
    return("" . join(textocifrado))
     

#esta funcion decodifica el texto cifrado en vigenere por medio del mismo texto
#cifrado y su clave de cifrado
def textoOriginal(textocifrado, clave):
    texto_original = []
    for i in range(len(textocifrado)):
        x = (ord(textocifrado[i]) -
             ord(clave[i]) + 26) % 26
        x += ord('A')
        texto_original.append(chr(x))
    return("" . join(texto_original))

#metodo main para ejecutar el programa
if __name__ == "__main__":
    string = "HOLABOB"
    keyword = "ADIOS"
    clave = generaClave(string, keyword)
    textocifrado = cifraTexto(string,clave)
    print("Ciphertext :", textocifrado)
    print("Original/Decrypted Text :",
           textoOriginal(textocifrado, clave))
 
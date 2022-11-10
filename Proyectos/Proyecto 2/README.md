# Proyecto 2 - (RSA)

[![Python](https://img.shields.io/badge/Python-3.9+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org) ![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=java&logoColor=white) ![Status badge](https://img.shields.io/badge/status-%20terminado-green?style=for-the-badge)

## Criptografía y Seguridad, Universidad Nacional Autónoma de México semestre 2023-1

> ---
>
> * **Victor Hugo Gallegos Mota** - *316160456* - [VictorDeGallegos](https://github.com/VictorDeGallegos)
> * **José Demian Jiménez** - *314291707* - [demian35](https://github.com/demian35)
> * **Carlos Cruz Rangel** - *314208682* - [CarlosCruzRangel](https://github.com/CarlosCruzRangel)
>
>
>
> ---

## Pre-requisitos 📋

*Para poder ejecutar la aplicacion es necesario tener instalado python  con versiones superiores a la 3.9 en alguno de los siguientes enviroments.*

* Global enviroment `python3`

```bash
python3 -V
Python 3.10.6
```

Tambien es necesario tener isntalado jdks para poder ejecutar el programa en java

```bash
java -version
openjdk 11.0.14 2022-01-18 LTS
OpenJDK Runtime Environment Zulu11.54+23-CA (build 11.0.14+9-LTS)
OpenJDK 64-Bit Server VM Zulu11.54+23-CA (build 11.0.14+9-LTS, mixed mode)
```

## Cifrado RSA

El cifrado rsa consiste en  generar dos numeros primos p y q, despues de esto se calcula el modulo n = p *q, despues se calcula el numero phi de n, phi(n) = (p-1)* (q-1), despues se elige un numero e que sea coprimo con phi(n), despues se calcula el inverso de e mod phi(n) que es d, despues se cifra el mensaje m con la formula c = m^e mod n, y para descifrar el mensaje se usa la formula m = c^d mod n.

### Detalles de la implentación

* La función relacionada con generar las llaves, deberá buscar números primos primos p y q distintos y aleatorios de al menos 100 dígitos.

* La función relacionada con cifrado, debe recibir como parámetros N y e (o hacer variables globales y referenciarlas) y el texto en claro que se va a cifrar (m).

* La función relacionada con descifrado,  debe recibir como parámetros N, d y el texto cifrado (criptograma) en el punto anterior.

* Incluir un método main (método principal del programa) con pruebas a estas funciones.

* Pueden agregar todos los métodos auxiliares que requieran.

## Ejecutar scripts 🚀

*Los siguientes comandos ejecutaran el programa pueden ser ejecutados con **python3*** ó con **python** si se tiene configurado el global enviroment.

Abrir la terminal pararse sobre la suguiente ruta *Criptografia-y-Seguridad/Proyectos/Proyecto 2/src*.
Y ejecutar el siguiente comando:

```bash
python3 rsa.py
```

Tambien recomendamos usar el editor de texto [Visual Studio Code](https://code.visualstudio.com/) con la extension [Code Runner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner) para poder ejecutar el script.

### Ejemplo de programa rsa.py en ejecucion 🐍

![rsa.py con 512 bits](https://user-images.githubusercontent.com/41756950/201002294-87d2cbf1-b7b6-440b-969c-e39f9379a47c.png)

Como se puede notar el mensaje descifrado no se muestra pues python tiene problemas para imprimir números tan grandes (512 bits) y al intentar descifrarlo recibimos el siguiente error:

```bash
OverflowError: Python int too large to convert to C int
```

Sin embargo, si bajamos el tamaño de los números primos a 10 dígitos, el programa funciona correctamente:

![rsa.py 10 bits](https://user-images.githubusercontent.com/41756950/201000898-95aedfce-7445-4684-9879-b19138e9c03a.png)

### Ejemplo de programa rsa.java en ejecucion ☕️

Por este bug de python, decidimos implementar el programa en java, el cual funciona correctamente con números de 512 bits ya que al ser un lenguaje de programacion altamente tipado, no tiene problemas para imprimir números tan grandes.

para compilar el programa:

```bash
javac rsa.java
```

para ejecutar el programa:

```bash
java rsa
```

![rsa en java con 512 bits](https://user-images.githubusercontent.com/41756950/201002084-b3442e8b-192a-4e2d-b3cd-0322f85673e0.png)

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien del equipo.
* 10/10 en el proyecto 2 🤓

---
⌨️ con ❤️ por  [VictorDeGallegos](https://github.com/VictorDeGallegos), [demian35](https://github.com/demian35) y [CarlosCruzRangel](https://github.com/CarlosCruzRangel)

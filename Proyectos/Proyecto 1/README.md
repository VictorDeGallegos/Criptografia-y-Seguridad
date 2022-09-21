# Proyecto 1 - (Criptosistema de Vigenère y Hill)

[![Python](https://img.shields.io/badge/Python-3.9+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)  ![Status badge](https://img.shields.io/badge/status-%20terminado-green?style=for-the-badge)

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

## Ejecutar scripts 🚀

*Los siguientes comandos ejecutaran el programa dependiendo el tipo de cifrado pueden ser ejecutados con **python3**.*

Abrir la terminal pararse sobre la suguiente ruta *Criptografia-y-Seguridad/Proyectos/Proyecto 1/src*.
Y ejecutar el siguiente comando:

```bash
python3 nombre_del_script.py
```

Tambien recomendamos usar el editor de texto [Visual Studio Code](https://code.visualstudio.com/) con la extension [Code Runner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner) para poder ejecutar los scripts.

### Cifrado Hill (SCRIPT SIN LIBRERIAS)

Realizamos 2 scripts para el cifrado Hill, uno con librerias y otro sin librerias.

```python
python3 HillSinLibrerias.py
```

**Resultado en consola:**

En este script se define la matriz de cifrado y su version en string para poder cifrar y descifrar textos planos

<img width="1027" alt="Cifrado Hill sin librerias" src="https://user-images.githubusercontent.com/41756950/191543066-2f95b6b5-6944-431b-bc83-ec069ee0fbe8.png">


### Descifrado Hill (Con librerias)

Este script se realizo para corroborar que el cifrado Hill sin librerias funciona correctamente.


* Librerias **necesarias** `sympy` `numpy`
Estar en la ruta *Criptografia-y-Seguridad/Proyectos/Proyecto 1/* y ejecutar el siguiente comando:

```bash
python3 -m pip install -r requirements.txt
```

Posteriormente ejecutar el siguiente comando:

```python
python3 hill.py
```

**Resultado en consola:**
Como se ouede notar en la imagen el resultado del cifrado Hill es el mismo que el cifrado Hill sin librerias.

<img width="1027" alt="Cifrado Hill con librerias" src="https://user-images.githubusercontent.com/41756950/191541043-6997e754-75b6-4a41-8ef4-6ef2702fafb3.png">


### Descifrado Hill (Con librerias)

```python
python3 Hill.py
```

**Resultado en consola:**
Como se puede notar en la imagen el resultado del descifrado Hill es el mismo que el descifrado Hill sin librerias.
<img width="1027" alt="Captura de Pantalla 2022-09-21 a la(s) 10 08 57 a m" src="https://user-images.githubusercontent.com/41756950/191541541-be169c47-610e-451c-9082-5b4ff43f16c6.png">


### Cifrado de vigenere
```python
python3 cifradoVigenere.py
```

**Resultado en consola:**

<img width="1027" alt="Captura de Pantalla 2022-09-21 a la(s) 10 10 53 a m" src="https://user-images.githubusercontent.com/41756950/191542037-4967e7b5-4592-496c-9ca4-bec4632ff176.png">

### Descifrado de vigenere

```python
python3 descifradoVigenere.py
```

**Resultado en consola:**

<img width="1027" alt="Captura de Pantalla 2022-09-21 a la(s) 10 12 28 a m" src="https://user-images.githubusercontent.com/41756950/191542424-7962cc53-6ecc-46c4-84f6-b43ad336ad78.png">

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien del equipo.
* 10/10 en el proyecto 1 🤓

---
⌨️ con ❤️ por  [VictorDeGallegos](https://github.com/VictorDeGallegos), [demian35](https://github.com/demian35) y [CarlosCruzRangel](https://github.com/CarlosCruzRangel)

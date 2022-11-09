# Proyecto 2 - (RSA)

[![Python](https://img.shields.io/badge/Python-3.9+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)  ![Status badge](https://img.shields.io/badge/status-en%20progreso-yellow?style=for-the-badge)

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

*Los siguientes comandos ejecutaran el programa pueden ser ejecutados con **python3*** ó con **python** si se tiene configurado el global enviroment.

Abrir la terminal pararse sobre la suguiente ruta *Criptografia-y-Seguridad/Proyectos/Proyecto 2/src*.
Y ejecutar el siguiente comando:

```bash
python3 rsa.py
```

Tambien recomendamos usar el editor de texto [Visual Studio Code](https://code.visualstudio.com/) con la extension [Code Runner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner) para poder ejecutar el script.

### Cifrado RSA

El cifrado rsa consiste en  generar dos numeros primos p y q, despues de esto se calcula el modulo n = p *q, despues se calcula el numero phi de n, phi(n) = (p-1)* (q-1), despues se elige un numero e que sea coprimo con phi(n), despues se calcula el inverso de e mod phi(n) que es d, despues se cifra el mensaje m con la formula c = m^e mod n, y para descifrar el mensaje se usa la formula m = c^d mod n.

### Detalles de la implentación

* La función relacionada con generar las llaves, deberá buscar números primos primos p y q distintos y aleatorios de al menos 100 dígitos.

* La función relacionada con cifrado, debe recibir como parámetros N y e (o hacer variables globales y referenciarlas) y el texto en claro que se va a cifrar (m).

* La función relacionada con descifrado,  debe recibir como parámetros N, d y el texto cifrado (criptograma) en el punto anterior.

* Incluir un método main (método principal del programa) con pruebas a estas funciones.

* Pueden agregar todos los métodos auxiliares que requieran.

### Ejemplo de programa en ejecucion

```bash
╭─ 🍎 victor@MacBook-Pro 🏠 ~/Documents/GitHub/Criptografia-y-Seguridad/Proyectos/Proyecto 2/src 
╰─ python3 rsa.py
Llave p:  7747351013499727576259507623476004847248552393800302370250599182763992688776377327805935186431944252163294125047325302392929090540538658456949258754087722
Llave q:  12674469735697300196804303701892625304019227788047857752007359964303639218172545805130548413010775047554605343917114160968618879146427999097225510322559286
--------------------------------
N = 98193565952426102982471415664640171953724536291962319732546850942787561817698498826697916548774586249887633445456770771254632819094239637917184060881577996472457885352773705202593945062623757666154482799587457483152849087348477945829842835722212424510086248568135613841759191776144656687835998136005189686492
--------------------------------
e = 11063012408032728650682654419321304443723284934477424041882108144294098072344354622104588431943494627475006428268220352618463318390558415396156300223392522
d = 13416196552232803343953155778449147748128031936349414528139452638400080267783214396725317178909947590131642576495617898787264826492290173015710145813249884820610205338536634202606383130699121874056254679825685625277172665024191561370374781280486938597637705814604967505548667975625474330678871605758611011698
--------------------------------
Mensaje a cifrar:
niño
Mensaje cifrado:
[41678995970275413788730076103288595052062026318382259888733609550977097008909509470376068246779374365299237808005864233152272632790844746531283205234643056250193291826681728395715690759766970700115950955280115816128220182670414562085436004133788431198374776891280824683979518466333154331311941781060823167932, 12690597294788903632191747541553714553283110802750901315094688616425997600971054000054641149317869266758790042756426425205053474919629448162505520908583515412912538385872027311884624876123910377782477463423272090416975752159156581937040890667939817354388642520579609491686476363069357550690124765051203320101, 3252013713693554012669127781573590122144718181030530724162053958407717612130912363577197778597296807701617994481389303684497683394220465944901946188605105984755775301560396001095331451437317690009998738803357229531800098631994805247404371040880351679959226607012998618984710110472308094401577255060509877649, 386043927151728261178811421693585709468661997636827512877944316736821649326778510152533182324663415520857647320201785388461416518947706921081937711197716042303399514286366459499736009401171983913700541435272869399982347204920652478921221097713552754167302410682930921681075970738791738780499414324689132897]
--------------------------------
```

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien del equipo.
* 10/10 en el proyecto 2 🤓

---
⌨️ con ❤️ por  [VictorDeGallegos](https://github.com/VictorDeGallegos), [demian35](https://github.com/demian35) y [CarlosCruzRangel](https://github.com/CarlosCruzRangel)

# Tarea 1 - Cifrados Clásicos.

[![Python](https://img.shields.io/badge/Python-3.9+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org) ![Status badge](https://img.shields.io/badge/status-%20terminado-green?style=for-the-badge)

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

* Conda enviroment `conda 4.13.0`

```bash
python -V
Python 3.9.13
```

* Global enviroment `python3`

```bash
python3 -V
Python 3.10.6
```

## Ejecutar scripts 🚀

*Los siguientes comandos ejecutaran el programa dependiendo la grafica que se desee consultar pueden ser ejecutados con **python** o **python3**.*

Abrir en su editor de texto favorito y ejetucar desde ahi o ejecutar en la terminal los siguientes comandos.

```bash
python nombre_del_script.py nombre_del_archivo.txt
```

### Cifrado por analisis de frecuencias
    
```bash
>python3 frecuencias.py archivo.txt

Frecuencias de las letras:
Letra   Frecuencia      Porcentaje
R        210             11.88 %
L        200             11.31 %
M        172             9.73 %
Q        142             8.03 %
F        141             7.98 %
K        141             7.98 %
P        117             6.62 %
S        108             6.11 %
T        92              5.20 %
E        90              5.09 %
I        88              4.98 %
U        60              3.39 %
N        56              3.17 %
J        46              2.60 %
V        24              1.36 %
A        14              0.79 %
Y        14              0.79 %
C        12              0.68 %
B        10              0.57 %
G        10              0.57 %
O        8               0.45 %
D        7               0.40 %
Z        3               0.17 %
H        1               0.06 %
W        1               0.06 %
X        1               0.06 %


Texto con las letras SUSTITUIDAS: 

la proteina spike del sarscovdos se esta adaptando debido a
presiones selectivas
la escala global de la pandemia de covid ha demostrado la evolucion
del sarscovdos y las claves de adaptacion. despues de catorce
meses desde la declaracion de la pandemis, multiples variantes
han surgido y se han fijado en la poblacion humana gracias
a extrinsecas presiones selectivas si no tambien a la capac-
idad mutacional inhernete del virus. aqui aplicamos una prueba
de evolucion de sustitucion neutra a la proteina de pico de
la proteina omicron y se comparo a la evolucion neutra de la
variente de preocupacion de los demas. realizamos comparaciones
entre las interacciones entre las proteinas s de los cov(alfa,eta,gamma,delta
y omicron) y el receptor acedos. los aminoacidos compartido
entre todas las proteinas s que se unen a acedos permanecen
constantes lo que indica que estos aminoacidos son esenc-
iales para la union precisa al receptor. los complejos rbd para
cada variate con el receptor se utilizaron par identificar los
aminoacidos involucrados en la interaccion proteina prote-
ina. la rbd de omicron establece ochenta y dos contactos frente
a los sesentaycuatro de la proteina original de wuhan por lo
tanto, el numero medio de contactos por residuos es mayor
por lo que el contacto termodinamico es mas estable. los rbd de
los cov son similares en secuencia y estructura sin embargo,
el rbd de omicron presenta la desviacion mas grande de la est-
ructura por uno punto once armsd, causado por un conjunto
de mutaciones cercanas a la glicosilacion ntresitneo cuarenta
y tres de la proteina omicron s son diferente de la proteina
original que provocan un reconocimiento reducido por parte
de los anticuerpos neutralizantes. nuestros resultados su-
guieren que las presiones selectivas son inducidas por la
vacunacion masiva en todo el mundo y por persistencia de in-
feccioes recurrentes en individuos inmunodeprimidos, que
no eliminaron la infeccion y acabaron facilitando la seleccion
de virus cuyas caracteristicas son diferentes a los cov an-
teriores, menos patogenos pero con mayor tranmisibilidad.
```

### Cifrado Vigenere

```bash
>python3 Vigeneredesifrado.py archivovigenere.txt

Texto descifrado:
E N E  SEL  U G A  R L A  S E N  O R A  E L O  D I A  R E A  L I Z
AEL  M I L   A G R  O A G  A R R  A L O  S P O  C O S  P E L O S R
OJO  S D E   M I T  I A Q  U E Y  A E S  T A M  E D I  O C A L V A

DES  P U E  S L O  S L A  V A L  O S S  E C A  L O S  E S T  I R A
LES H A C   E C R  E P E  L O S  E X T  I E N  D E Y  L O S  S O B
AHA S T A  T R A   N S F  O R M  A R L  A E S  C A S  A C A  B E L
LER A D E  M I T  I A E  N U N  E D I  F I C  I O D  E F A  N T A
SIA D E V  A R I  O S P  I S O  S C O  N R U  L O S  R I S  O S C
AIR E L E  S Y R  O S E  T O N  E S L  O H O  R N E  A D U  R A N
TEA L G U  N A S  H O R  A S E  N E L  S E C  A D O  R Y D  E S P
UES L O R  O C I  A C O  N S I  E T E  L I T  R O S  D E L  A C A
PAR  A D A  R L E  F I R  M E Z  A Y S O S T  E N A  S U C  R E A
CIO N E L  D I A  D E L  A B O  D A M  I T I  A L L  E G O  A N U
EST R A C  A S A  C O N  U N P  E I N  A D O  Q U E  M E D  I A D
OSM E T R  O S D  E A L  T U R  A S E  V E I  A I M  P R E  S I O
NAN T E C  U A N  D O A  B R I  M O S  L A P  U E R  T A P A R A
SAL I R S  E E S  C U C  H O U  N Z U  M B I  D O A  L L E V A N
TAR L A V  I S T  A A L  C I E  L O D  E S C  U B R  I M O S U N
BIC H O Q  U E S  E A C  E R C  A B A  V O L  A N D  O A T O D A
VEL O C I  D A D  Q U E  E S E  S O P  R E G  U N T  O M I M A M
AYO S E L  O Q U  E E S  A C L  A R E  T R I  U N F  A L C U A N
DOL O P U  D E D  I S T  I N G  U I R  M A S  D E C  E R C A E S
UNM A Y A  T E Y  E S O  Q U E  E S I  N T E  R R O  G O M I H E
RMA N A U  N M A  Y A T  E L E  S I N  F O R  M E E  S U N A E S
PEC I E D  E E S  C A R  A B A  J O P  E R O  U N P  O C O M A S
REC H O N  C H O  E L M  A Y A  T E E  R A D  E L M  I S M O C O
LOR R O J  O B R  I L L  A N T  E Q U  E E L  C A B  E L L O D E
MIT I A E  L I N  S E C  T O V  O L O  E N P  I C A  D A Y Z A O
SEZ A M B  U L L  O E N  E L P  E I N  A D O  A Y Q  U E A S C O
GRI T O M  I M A  M A A  Y Q U  E S U  S T O  B E R  R E O M I H
ERM A N A  A Y Q  U E B  A R B  A R I  D A D  S E H  I S T E R I
ZOM I T I  A Q U  I T E  N M E  L O P  E R O  S I N  D E S C O M
PON E R E  L P E  I N A  D O A  D V I  R T I  O N O  S A S O M A
MOS T E M  E R O  S O S  A L A  S P R  O F U  N D I  D A D E S D
EES A S E  L V A  R O J  A Y A  L O V  I D I  J O M  I P A P A E
STA U N P  O C O  A T U  R D I  D O Y  M A R  E A D  O P O R E L
OLO R D E  L A L  A C A  S A L  D E A  H I E  L M A  Y A T E N O
OBE D E C  I O L  E M E  T I M  O S U  N L A  P I Z  H U R G A M
OSC O N E  L D E  D O L  E S O  P L A  M O S  Y N A  D A E L P E
INA D O S  E G U  I A I  N T A  C T O  A D E  N T R  O D E N A D
AVA L I E  R O N  S U P  L I C  A S A  M E N  A Z A  S N I L O S
MAS R U D  O S P  R O C  E D I  M I E  N T O  S N I  M O D O S E
IMP A C I  E N T  O M I  P A P  A S E  N O S  H A C  E T A R D E
TEN D R A  S Q U  E I R  C O N  E S O  M I T  I A A  U N Q U E N
ERV I O S  A S A  B I A  Q U E  N O T  E N I  A O T  R A A L T E
RNA T I V  A L A  F I E  S T A  T R A  N S C  U R R  I A N O R M
ALM E N T  E P E  R O M  I T I  A S E  S O B  R E S  A L T A B A
ACA D A R  A T O  C U A  N D O  T E R  M I N  A M O  S D E C E N
ARY E M P  E Z O  L A M  U S I  C A M  I T I  A A H  O G O U N G
RIT O Q U  E T E  P A S  A L E  P R E  G U N  T E C  R E O Q U E
ELE S C A  R A B  A J O  E S T  A B A  I L A  N D O  S U S U R R
OME A S O  M E A  L P E  I N A  D O Y  E F E  C T I  V A M E N T
EEL E S C  A R A  B A J  O R O  J O E  S T A  B A B  A I L A N D
OEL P R I  M E R  V A L  S D E  L A N  O C H  E O B  S E R V E F
ASC I N A  D O Q  U E E  L M E  R E N  G U E  D E L  P A S T E L
DEB O D A  S T E  N I A  G R A  N D E  S S E  M E J  A N Z A S C
ONE L P E  I N A  D O D  E M I  T I A  L L E  G O E  L M O M E N
TOD E F E  L I C  I T A  R A L  O S N  O V I  O S M  I T I A S E
LEV A N T  O C O  M O T  O D O  S Y A  L A B  R A Z  A R A L A N
OVI A Z Z  E L E  S C A  R A B  A J O  D E C  I D I  O V O L A R
ENE L I N  E R I  O R D  E L P  E I N  A D O  Q U E  E S E S E R
UID O P R  E G U  N T O  L A N  O V I  A A L  G O A  S U S T A D
APA R E C  E Q U  E V I  E N E  D E T  U C A  B E Z  A T I A E S
MIA P A R  A T O  P A R  A L A  S O R  D E R  A R E  S P O N D I
OEL L A C  O N U  N A S  O N R  I S A  D E P  A N I  C O

```

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien del equipo.
* 10/10 en la tarea 1 🤓

---
⌨️ con ❤️ por  [VictorDeGallegos](https://github.com/VictorDeGallegos), [demian35](https://github.com/demian35) y [CarlosCruzRangel](https://github.com/CarlosCruzRangel)

# Qué es Python
<div style="text-align: justify">Python es un <a href="https://es.wikipedia.org/wiki/Lenguaje_de_alto_nivel">lenguaje de programación de alto nivel</a>, orientado originalmente a la ejecución de secuencias de comandos. Es un lenguaje <a href="https://es.wikipedia.org/wiki/Int%C3%A9rprete_(inform%C3%A1tica)">interpretado</a> y con una sintaxis relativamente reducida y <a href="https://es.wikipedia.org/wiki/Tipado_din%C3%A1mico">tipado dinámico</a>. Tiene soporte para múltiples paradigmas de programación, incluyendo una extensa lista de facilidades dedicadas a la <a href ="https://es.wikipedia.org/wiki/Programaci%C3%B3n_orientada_a_objetos">Programación Orientada a Objetos</a> y algunas herramientas del <a href="https://es.wikipedia.org/wiki/Programaci%C3%B3n_funcional">paradigma Funcional</a>. Cuenta con un intérprete, escrito en C, el cual se encarga de todas las tareas de bajo nivel, entre ellas: la compilación del código funte a <a href="https://es.wikipedia.org/wiki/Bytecode">código de <i>bytes</i></a> y su subsecuente ejecución, el manejo de memoria, la implementación de los <a href="https://es.wikipedia.org/wiki/Tipo_de_dato_abstracto">Tipos de Dato Abstractos</a> y algoritmos principales, la creación y destrucción de objetos (<a href="https://es.wikipedia.org/wiki/Recolector_de_basura">RB</a>), &c.</div><br>

<div style="text-align: justify">Todas estas características, junto con su reducido conjunto de palabras clave, lo posicionan como un lenguaje <i>amigable</i> para un primer acercamiento y ofrecen facilidades y abstracciones que permiten un despliegue rápido y efectivo, aún si a veces incomprendido, de soluciones concretas (programas) a problemas planteados (requisitos). Sin embargo, esa percibida facilidad puede tornarse un arma de doble filo: el programador que no entiende <b><i>qué</b></i> es lo que su programa hace está destinado al fracaso. O peor, a gastar horas, semanas, meses de su vida en el engorroso <i>debugeo</i> de código que, de haber tenido una más clara noción de cómo funcionaba, no le hubiera representado mayor dificultad.</div><br>

    
> ### ***El camino al infierno está plagado de fáciles abstracciones.***
><div style="text-align: right"><i> San Francisco de Python. </i><b>SXIII</b></div>


## Esta guía
<div style="text-align: justify">
Esta guía pretende ofrecer un recorrido no menos <i>amigable</i> que el habitual, pero sí más integral. Partidendo desde lo pequeño hasta lo grande y ofreciendo al lector las herramientas necesarias para comprender verdaderamente qué sucede en su computadora cuando el intérprete de Python hace <i>su magia</i> y como valerse de ellas para escribir <a href="https://es.wikipedia.org/wiki/Correctitud">código correcto</a>, legible, mantenible y, sobre todo, disfrutable. 
</div><br>

<div style="text-align: justify">
a
</div>

### Contenidos


-    [Primeros Pasos](/0.%20Primeros%20Pasos.md)<hr>

- i.    [Introducción](/i.%20Introduccion.md)
    - a.    Programas.
    - b.    [Esquema Compilador - Intérprete](/i.a%20Esquema%20Compilador%20-%20Interprete.png)
    - c.    [Palabras Claves, Tipos](/i.b%20Palabras%20Claves,%20Tipos.md)
    - d.    Tamaños y Memoria:
        - 1\.    [Tamaño de los tipos Principales]()
        - 2\.    [`(.py)` Imprimir Tamaños]()        
- ii.   [Básicas de Python]()
    - a.    [Los 3 mosqueteros: `str`, `int` y `list`]()
    - b.    [Prácticas "Pythonistas"]()
    - c.    Espacios de nombres:
        - _Parte 1_.    [Sistema de importación]()
        - _Parte 2_.    [Paquetes - PyPi y Pip]()                
- iii.  [Sintaxis](/iii.%20Sintaxis.md)
    - a.    [`(.py)` Sintagmas Principales](/iii.a%20Sintagmas%20Principales.py)
- iv.   [Funciones](/iv.%20Funciones.md)
- v.    Objetos:
    - _Parte 1_. [Estructura General]()
    - _Parte 2_. [Métodos "Mágicos" *(\_\_dunder\_\_)*]()
    - _Parte 3_. [Metaclases y Genéricos]() 
    - a.   [Esquema de Objetos en Memoria](/vi.%20Esquema%20de%20Objetos%20en%20Memoria.png)
    - b.   Ejemplos:
        - 1\.    [`(.py)`Lista personalizada]()
        - 2\.    [`(.py)`Metaclase ""*Singleton*""]()
        - 3\.    [`(.py)`Creación dinámica de Clases con `type()`]()  
<br>
<hr>
<div style="text-align: right">
<h3><a href="./0. Primeros Pasos.md"> Primeros Pasos ----> </a>
</h3></div><hr>

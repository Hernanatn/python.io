# *funciones*

## Definición
<p>En Python las funciones son objetos de tipo object,callable,function. Se alocan en el heap con tres punteros en el stack. Uno que señala la función en la LUT, y otros dos utilizados para propósitos de recolección de basura.</p>

Se definen con la palabra clave `def`:  
```Python
def unaFunción() -> None:
    ...
```
La forma *Pythonista* de documentar una función es utilizando doc-strings '''.  

## Argumentos
Las funciones toman dos tipos de argumentos:  
+argumentos posicionales o `args` y   
+argumentos nominales o `kwargs`

Por defecto todos los argumentos de una función son al mismo tiempo posicionales y nominales.
```Python
def otraFuncion(primerArgumento : int, segundoArgumento : bool) -> bool:
    '''
    Funcion que toma un valor entero y un booleano devuelve and entre el 'truthy' del entero y el booleano
    :param: primerArgumento [int]. el entero.
    :param: segundoArgumento [bool]. el booleano
    :return: [bool] and entre ambos parámetros.
    '''
    return (primerArgumento and segundoArgumento)
```

Se puede llamar a la función declarando los argumentos de ambas formas, pero una vez que se declaró un 'kwarg' los subsiguientes deben ser 'kwargs' también. 
```Python
valorA : bool = otraFuncion(5, segundoArgumento = False)
# >>> False
valorB : bool = otraFuncion(primerArgumento = 6, True)
# >>> SyntaxError: Positional argument follows keyword argument.
valorC : bool = otraFuncion(7, True)
# >>> True
valorD : bool = otraFuncion(primerArgumento = 0, segundoArgumento = True) # 0 es 'falsy'
# >>> False
```    

Una función puede tener valores por defecto para sus argumentos. Estos se declaran en la definición y se invocan omitiendo cada argumento en la llamada.
```Python
def funcionDefecto(primerArgumento : int = None, segundoArgumento : bool = True):
    return (primerArgumento and segundoArgumento) if primerArgumento else segundoArgumento
```
```Python
valorA : bool = otraFuncion(5)
# >>> True
valorB : bool = otraFuncion(segundoArgumento = False)
# >>> False
```    


### *Args y **Kwargs
Una función puede tomar una cantidad indefinida de argumentos, tanto posicionales como nominales.  
Los argumentos indeterminados se guardan en una `collection`, una `list[str]` para los `*args` y un `dict[str,t_argumento]` para los `**kwargs`  
> *Nota: El nombre de las colecciones se declara en la firma de la función usando estrellas*  
> *Nota: En el `dict` de `**kwargs` el nombre de cada argumento es su llave*  
```Python
def muchosArgumentos(argPrimero : int, argSegundo : float, *posicionales, **nominales):
    ...
```
Dentro de la función se puede acceder a las colecciones por su nombre. Se estila usar el sintagma `elemento in colección`.

```Python
def muchosArgumentos(argPrimero : int, argSegundo : float, *posicionales, **nominales):
    print(f'{argPrimero} es el primero. {argSegundo} es el segundo. ')
    for argPosicional en posicionales:
        print(f'{argPosicional}')
    for nombre,argNominal en nominales:
        print(f'{nombre} es la llave. {argNominal} es el argumento')
```

Los `*args` y `**kwargs` suelen usarse para:  
+Funciones que llaman otras funciones con parametros opcionales.
+Funciones que utilizan colleciones (en general diccionarios) con elementos opcionales
+Sistematizar objetos config.
```Python
from bs4 import BeautifulSoup, ResultSet, Tag, NavigableString
from requests import get as GET
from re import sub as reemplazar

def buscarBS4(url:str,etiqueta:str,atributos:dict = None,**atributosKw)-> Tag | NavigableString | None:
    
    html : str = GET(url).text #texto html de la página
    sopa : BeautifulSoup = BeautifulSoup (html,"html.parser") #creación del objeto BeautifulSoup

    if not atributos:
        dictAtributos : dict = {}
        for id, dato in atributosKw.items():
            dictAtributos[reemplazar("_","",id)] = dato
    else:
        dictAtributos : dict = atributos
    
    try:
        busqueda : ResultSet = sopa.find( 
                                        name=etiqueta,  
                                        attrs=dictAtributos
                                        )
                                        
    except Exception as e:
        print(f"[ERROR] Hubo un error al realizar la búsqueda:\n{e}\n\n")
        busqueda = None  

    return busqueda
```


## Composición de Funciones
### Funciones de orden superior (funciones como parámetros)
Aunque Python no es un lenguaje dedicado a la programación funcional, incluye algunas utilidades de ese paradigma. Entre ellas se encuentra la *composición* de funciones para generar **funciones de orden superior**.  

Una **función de orden superior** es aquella que toma otras funciones como parametro y las llama detro de su cuerpo.

```Python
from typing import Callable

#-----------ALIAS TIPOS-----------#
CategoriasNota  = tuple[list[str],int,str]
Categorizador   = Callable[[ResultSet,str],CategoriasNota]
Listador        = Callable[[Categorizador],ListaNotas]
#---------------------------------#

def categorizadorNotas(etiquetas:ResultSet, subBusqueda : str = None) -> CategoriasNota:
    '''
    :param etiquetas: [bs4.ResultSet] Resultado de una búsqueda con bs4.
    :param subBusqueda: [str] Cadena que representa la busqueda a realizar dentro del ResulSet.
    :return: [tuple] Tupla que representa la lista de notas categorizadas.
    '''
    etiquetasNota   : list[str] = []
    relevanciaNota  : int = 0
    bloqueNota      : str = ""

    ...

def listadorPerfil (categorizadorNotas : Categorizador) -> ListaNotas:
    '''
    :param categorizadorNotas:  [Callable] : La función de categorización de notas que el "scrapper" aplicará a cada objeto de tipo Nota. La función debe tomar como parámetros el ResultSet de etiquetas recuperadas con BS4 y (opcionalmente) la "Tag" de sub-búsqueda para cada etiqueta de la nota. Debe devolver un tuple[list[str],int,str] representando: la lista de etiquetas, el grado de relevancia y el bloque temático de la nota.
    :return: [ListaNotas] : Objeto de tipo ListaNotas que contiene las notas de la sección política del portal web del diario Perfil de la fecha de ejecución.
    '''
    MEDIO : str = "Perfil"
    PERFIL_POLITICA : str = "https://www.perfil.com/seccion/politica"

    ...

    etiquetasNota,relevanciaNota,bloqueNota = categorizadorNotas(etiquetas,"a")
    ...
    return listaDeNotasHoy

def listarNotas( listadorMedio : Listador, categorizadorNotas : Categorizador) -> ListaNotas: 
    return listadorMedio( categorizadorNotas )

```
El ejemplo anterior presenta 3 funciones las cuales se componen para realizar la funcionalidad deseada - i.e. producir una Lista de Notas.  
Como vemos, la función `categorizadorNotas` es una función de primer orden, una función **concreta** la cual toma ciertos parámetros que no son funciones y devuelve una tupla.  
Por su parte, `listadorPerfil` es una función de otden ligeramente superior, es parcialmente concreta entanto tiene estado interno, detalles de implementación propios y produce efectos secundarios. Pero parte de su funcionalidad (la de producir la tupla de categorías), está delegada en *cualquier* Categorizador que le sea provisto como parámetro.  
Finalmente, `listarNotas` no es más que una interfaz. Es una función de orden superior que llama a *cualquier* Listador que produzca una ListaNotas y le provee la correspondiente función categorizadora.


### Lambdas (funciones anónimas)
Se emplean con la siguiente sintaxis  
`lambda` *variable* `:` procedimiento sobre la *variable*  
Las `lambda`s pueden ser asignadas a variables, o pasadas como argumentos a funciones de orden superior.

El sintagma
```Python
miLambda = lambda nombre : nombre.upper()
```
Es equivalente a
```Python
def miLambda (nombre : str) -> str:
    return nombre.upper()
```

### @Decoradores 
Los decoradores son *`azucar sintáctico`*para funciones de orden superior funciones de orden superior que toman como parámetro una función o clase.  
Son funciones "envolventes" que pueden ser nuevamente llamadas.  
Al utilizar un decorador sobre la definición de una función, el programador le indica al compilador que cada vez que esa función sea llamada, debe ser llamada a travez del evolvente determinado por el decorador.

El sintagma
```Python
from Typing import Callable

def repetir5Veces (unaFuncion : Callable, *posicionales) -> Callable:
    for i in range (5):
        unaFuncion(*posicionales)
...
@repetir5Veces
def imprimirCuadrado(numero : int) -> int:
    print(numero*numero)
```
Es equivalente a pedirle al compilador que cada vez que se llama a `imprimirCuadrado`, en su lugar se llame
```Python
repetir5Veces(imprimirCuadrado, numero)
```

## Generadores
Los generadores son funciones que en vez de retornar un valor, "producen" múltiples valores intermedios.
Esta funcionalidad se logra utilizando la palabra clave `yield` dentro de la función.  
Para recuperar los *yields* de un generador se debe usar la función `next()`, de forma explicita o bien implícita (como por ejemplo en la implementación de iteradores).  

```Python
class MiRango():
    def __init__(self, final : int) -> None:
        self.inicio : int = 0
        self.final  : int = final

    def __iter__(self) -> Iterator[int]:
        indice : int = self.inicio
        while indice < self.final:
            yield indice
            indice +=1

for n in MiRango(5):
    print(n)

#>>> 0
#>>> 1
#>>> 2
#>>> 3
#>>> 4

rango = MiRango(4)
print(next(rango))
print(next(rango))
print(next(rango))
print(next(rango))


#>>> 0
#>>> 1
#>>> 2
#>>> 3
```

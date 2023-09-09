#funciones en Python

## Definición
<p>En Python las funciones son objetos de tipo object,callable,function. Se alocan en el heap con tres punteros en el stack. Uno que señala la función en la LUT, y otros dos utilizados para propósitos de recolección de basura.</p>

Se definen con la palabra clave `def`:  
```Python
def unaFunción() -> None:
    pass
```

La forma *Pythonista* de documentar una función es utilizando doc-strings '''.  

## Argumentos
Las funciones toman dos (2) tipos de argumentos:  
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
valorD : bool = otraFuncion(primerArgumento = 0, True) # 0 es 'falsy'
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

Una función puede tomar una cantidad indefinida de argumentos, tanto posicionales como nominales.  
Los argumentos indeterminados se guardan en una `collection`, una `list[str]` para los `*args` y un `dict[str,t_argumento]` para los `**kwargs`  
*Nota: El nombre de las colecciones se declara en la firma de la función usando estrellas*  
*Nota: En el `dict` de `**kwargs` el nombre de cada argumento es su llave*  
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
+
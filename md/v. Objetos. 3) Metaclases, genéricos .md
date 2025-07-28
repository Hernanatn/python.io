<div style="text-align: justify">
En la parte 1) del módulo de objetos se hizo particular énfasis en que todas y cada una de las entidades en Python son objetos. Todas. Las <i>clases</i>, también.
</div><br>

Cuando el intérprete corre una pieza de código como la siguiente:
```Python
class MiClase():
    ...
```
Lo que hace es *instanciar* un **objeto** con nombre `MiClase`.
Las clases son objetos especiales en python en el sentido de que son objetos capaces de crear otros objetos. Pero siguen siendo objetos.

- Se los puede asignar a variables:
```Python
unaVariableCualquiera : Any = MiClase
```
- Se les puede agregar atributos:
```Python
MiClase.atributo = 'algo'
```
- Se los puede pasar como parámetros a funciones:
```Python
print(MiClase)
#>>> <class '__main__.MiClase'>

print(unaVariableCualquiera())
#>>> <__main__.MiClase object at 0x8997b4c>
```


## `type()`
El paradigma de Clases como Objetos sugiere dos preguntas: ¿Quién arma las clases? y ¿De qué tipo es una clase?
La clases son objetos de tipo `class`, que a su vez es un tipo heredero de `type`  y que en última instancia deriva de `object`.

Sí, `type`, el mismo type que devuelve el tipo de un objeto. `type` es la clase que crea todas las clases del programador en el curso de un programa de Python. Y, a través de polimorfismo, su API está expuesta al programador.  

De la misma forma que podemos llamar
```Python
type(o: object) #>>> devuelve el tipo del objeto 'o'
```
Podemos llamar:
```Python
type(name: str, bases : tuple[_T,...], attrs : dict) #>>> devuelve un nuevo objeto del tipo clase con la estructura provista.
```
donde:  
- `name`  : una `str` el nombre de la clase;
- `base`  : una `tuple` que contiene las clases madre;
- `attrs` : un `dict` que contiene los atributos de la clase.  

<table>
<tr>
<th>El sintagma:</th>
<th>Es equivalente a:</th>
</tr>
<tr>
<td>

```Python
class Perro(Animal,Terricola):
    familia = 'mamiferos'
```     
</td>
<td>

```Python
Perro = type('Perro',(Animal,Terricola),{'familia':'mamiferos'})
```
</td>
</tr>
</table>

Incluso se pueden definir métodos usando `lambda`s o funciones:
```Python
Perro = type \
    (
        name = 'Perro',
        bases = (Animal,Terricola),
        attrs = \
        {
            #Atributos de Clase
            'familia'   :'mamiferos',
            
            #Métodos de la instancia
            '__init__'  : lambda self, nombre : setattr(self,'nombre',nombre),
            'ladrar'    : lambda self : print(f"{self.nombre}: ¡Guau Guau!")
        }
    )

juan = Perro("juan")
juan.ladrar()

#>>> juan: ¡Guau Guau!

def initGato(self, nombre):
    self.nombre = nombre

def maullar(self):
    print(f"{self.nombre}: Miau")

Gato = type \
    (
        name = 'Gato',
        bases = (Animal,Terricola),
        attrs = \
        {
            #Atributos de Clase
            'familia'   :'mamiferos',
            
            #Métodos de la instancia
            '__init__'  : initGato,
            'ladrar'    : maullar
        }
    )

carlos = Gato("carlos")
carlos.maullar()

#>>> carlos: Miau
```

En ambos ejemplos anteriores

## Metaclases

Podemos definir el tipo *Singleton* así:
```Python
class Singleton(type):
    __instancias : dict = {} # La clase guarda un diccionario de instancias.

    def __call__(cls, *posicionales, **nominales):
        if cls not in cls.__instancias: # Si no hay una instancia ya creada, se crea una nueva.
            cls.__instancias[cls] = super(Singleton, cls).__call__(*posicionales, **nominales) # Se usa la clase (cls) para determinar la llave de cada entrada en el diccionario. Garantizando que no haya coliciones.
        return cls.__instancias[cls]
```

Al derivar nuestro *Singleton* de `type` y sobrecargar su método `__call__`, prodemos utilizaar el argumento  `metaclass = ...` en todos los tipos que queremos garatizar se ajusten al patrón.

*e.g.*
```Python
class ConfiguracionGlobal(metaclass=Singleton):
    __config : dict = \
        {
            '[ajuste]' : '[valorPorDefecto]',
            ...
        }
    
    def __init__ (self, rutaConfig : str, ...) -> None:
        with open(filename = rutaConfig, mode = "r", encoding = "utf-8") as archivoConfig:
            type(self).__config = archivoConfig.read()
```

En el ejemplo anterior, al declarar `Singleton` como metaclase de `ConfiguracionGlobal`, se sobre


## Genéricos
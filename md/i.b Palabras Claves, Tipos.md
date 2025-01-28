# Palabras Claves y Tipos

## Tipos "Primitivos"
- `object`
- `bool`

### Numéricos
- `int`
- `float`
- `complex`

### Secuencias
#### Mutables
- `list`
- `bytearray`
#### Inmutables
- `str`
- `tuple`
- `range`
- `bytes`
### Conjuntos
- `set`
- `frozenset`
### Mapeo
- `dict`

## Condicionales y operadores lógicos:
- `if`; `elif`; `else`    # *Condicionales básicos*<br>
- `and`; `or`; `not`      # *Operadores Lógicos*<br>
- `True` y `False`        # *Booleanos*<br>
- `assert`	              # *Condicional que equivale a `if not [condicion]: raise AssertionError`*<br>
- `in`	                  # *Condicional que evalúa si un valor está presente en alguna `colección`*<br>
- `is`                    # *Condicional que evalua si dos variables **apuntan** al mismo objeto en memoria *<br>
<br>

## Objetos
+`class` 	# *Define una Clase*<br>
+`del`   	# *Elimina una instancia de un objeto*<br>
<br>

## Nulos
+`None`	# *Representa un valor nulo, es de tipo `NoneType`*<br>
+`pass`	# *Declaración nula en en el sentido de que no hace literalmente nada*<br>
<br>

## Valores, variables y *scope*
+`with`     # **Manejador de Contexto** *utilizado para determinar un scope basado en **estado** para un bloque*<br> 
+`global`	# *Prefixo que declara una variable de scope global*<br>
+`nonlocal`	# *Prefixo que declara una variable como no restringida al scope local*<br>
<br>

## Funciones
+`def`     # *Define una función*<br>
+`lambda`  # *Define una función anónima*<br>
+`yield`   # *Finaliza la función y retorna un **generador***<br>
+`return`  # *Finaliza la función y retorna un **valor***<br>
<br>

## Ciclos
+`while`     # *Inicia un ciclo `while`*<br>
+`for`       # *Inicia un ciclo `for`*<br>
+`break`     # *Quiebra el ciclo en el que está*<br>
+`continue`	 # *Continúa con la siguiente iteración del ciclo en el que está*<br>

## Importación
+`from`      # *Importa [algo] desde un módulo*<br>
+`import`	 # *Importa un módulo*<br>

## Manejo de Errores
+`raise`     # *Levanta una `excepción`*<br>
+`try`       # *Inicio del bloque `try`...`except` determina el bloque que se **intentará** ejecutar*<br>	
+`except`	 # *Porción del bloque `try`...`except` determina el bloque que se ejecutará en caso de que una excepción del tipo esperado sea levantada*<br>
+`finally`	 # *Final (opcional) del bloque `try`...`except` determina el bloque que se ejecutará luego, indistintamente de si hubo o no excepciones*<br>

------------------------------------------------------

## Veracidad de los valores
Todos los tipos "primitivos" de Python pueden ser implícitamente *"casteados"* a un `bool`:

### Valores *veraces*
Por defecto todos los objetos **no-vacíos** en Python son *veraces* en el sentido de que pueden ser implícitamente *"casteados"* a `True` en evaluaciones del estilo:
```Python
x : int = 5
if x: 
    print(x)

# >>> 5 
```

### Valores *falaces*
Alternativamente, los valores **vacíos** son, por defecto, *falaces*. Pueden ser *"casteados"* implícitamente a `false`

| Colecciones               | Números       | Constantes |
|---------------------------|---------------|------------|
| Listas vacías `[]`        | `int 0`       | `None`     |
| Tuplas vacías `()`        | `float 0`     | `False`    |
| Diccionarios vacíos `{}`  | `complex 0`   | -          |
| Conjuntos vacíos `set()`  | -             | -          |
| Cadenas vacías `""`       | -             | -          |
| Rangos vacíos `Range(0)`  | -             | -          |

"Sintagmas Principales"

"Comentarios"
# Esto es un comentario

'''
    Esto es una 'doc-string'
'''

"Operadores"
class operadores:
    s : int     = 2 + 2     # Suma              s = 2 + 2 = 4
    r : int     = 5 - 2     # Resta             r = 5 - 2 = 3
    m : int     = 3 * 3     # Multiplicación    m = 3 * 3 = 9
    d : float   = 22 / 8    # División          d = 22 / 8 = 2.75
    f : int     = 22 // 8   # División Entera	f = 22 // 8 = 2
    n : int     = 22 % 8    # Resto             n = 22 % 8 = 6
    e : int     = 2 ** 3    # Exponente         e = 2 ** 3 = 8

"Operadores 'aumentados'"
class operadoresAumentados:
    ent : int = 0
    bul : bool = True

    ent += 1	# ent = ent + 1
    ent -= 1	# ent = ent - 1
    ent *= 1	# ent = ent * 1
    ent /= 1	# ent = ent / 1
    ent %= 1	# ent = ent % 1

    bul &= True # bul = (bul and True)

"Bloques"

#import parcial y con alias
class importacion:
    import pandas as pd
    from typing import Callable

#tipos y alias de tipos
class tipos:
    w : int # pista de tipo int
    x : int | str # pista de tipo unión [int|str]
    y : list[str] # pista de tipo compuesto list de strings
    z : Callable[[bool],str] # pista de tipo callable que toma un booleano como parámetro y retorna un int

    funcionQueTomaStryDevuelveInt = Callable[[str],int] # alias de un tipo callable

#ciclos for indexados con 'enumarate'
def imprimirIndiceyElemento(vector: list) -> None:
    for indice,elemento in enumerate(vector): 
        print(f"{indice=}|{elemento=}")

#ciclos con else
def ciclosConElse(limiteRango : int  = 50) -> None:
    i : int
    for i in range (limiteRango):
        print(f'{i=}')
        if i > 45: break
    else: print(f'No hubo quiebres')

    j : int = 0
    while i < limiteRango:
        print(f'{j=}')
        j+=1
        if j > 45: break
    else: print(f'No hubo quiebres')

#Manejo de errores 
class ManejoDeErrores:
    
    # El tipo Exception
    class UnaExcepcion(Exception): ...
    class OtraExcepcion(UnaExcepcion):
        @classmethod
        def convertirError(cls, UnaExcepcion) -> OtraExcepcion: ... 

    #Exception Groups
    def levantarGrupoExcepciones():
        excepciones : list[Exception] = [UnaExcepcion("Ex 1"),OtraExcepcion("Ex 2 ")]
        raise ExceptionGroup("Multiples problemas", excepciones)

    def unaFuncion(*args,**kwargs) -> None: ...
    def manejarError(error) -> None: ...
    def hacerSiempre() -> None: ...
    def hacerSiNoHuboError() -> None: ...
    

    # try...except
    try:
        unaFuncion("hola",5,[2,3])
    except UnaExcepcion as e:
        manejarError(e)

    # try...finally
    try:
        unaFuncion()
    finally:
        hacerSiempre()

    # try...except...finally
    try:
        unaFuncion("hola",5,[2,3])
    except UnaExcepcion as e:
        manejarError(e)
    finally:
        hacerSiempre()

    # try...except...else
    try:
        unaFuncion("hola",5,[2,3])
    except UnaExcepcion as e:
        manejarError(e)
    else:
        hacerSiNoHuboError()

    # try...except(re-raise)...finally
    try:
        unaFuncion("hola",5,[2,3])
    except UnaExcepcion as e:
        e.add_note("La excepción sucedio tratando de correr 'unaFunción('hola',5,[2,3])'")
        raise convertirError(e)
    finally:
        hacerSiempre()

    # try...except...else...finally
    try:
        unaFuncion("hola",5,[2,3])
    except UnaExcepcion as e:
        manejarError(e)
    else:
        hacerSiNoHuboError()
    finally:
        hacerSiempre()


#comprensión de listas
def imprimirYDevolverCuadrado(numero : int) -> int:
    cuadrado : int = numero*numero
    print(numero*cuadrado)
    return cuadrado

lista : list[int] = [1,2,3,4,5,6,7,8,9,10]


"el sintagma"
listaCuadrados : list[int] = [imprimirYDevolverCuadrado(num) for num in lista if num % 2 == 0]

"es equivalente a"
listaCuadrados : list[int] = []
for num in lista:
    if num % 2 == 0:
        listaCuadrados.append(imprimirYDevolverCuadrado(num))

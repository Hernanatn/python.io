"Sintagmas Principales"

"Comentarios"
# Esto es un comentario
'''
    Esto es una 'doc-string'
'''

"Operadores"
# +     Suma            2 + 2 = 4
# -     Resta           5 - 2 = 3
# *     Multiplicación	3 * 3 = 9
# /     División        22 / 8 = 2.75
# //    División Entera	22 // 8 = 2
# %     Resto           22 % 8 = 6
# **    Exponente       2 ** 3 = 8

"Operadores 'aumentados'"
def operadores() -> None:
    ent : int = 0
    bul : bool = True

    ent += 1	# ent = ent + 1
    ent -= 1	# ent = ent - 1
    ent *= 1	# ent = ent * 1
    ent /= 1	# ent = ent / 1
    ent %= 1	# ent = ent % 1

    bul &= True # bul = (bul and True)

#import parcial y con alias
import pandas as pd
from typing import Callable

#tipos y alias de tipos
w : int # pista de tipo int
x : int | str # pista de tipo unión [int|str]
y : list[str] # pista de tipo compuesto list de strings
z : Callable[[bool],str] # pista de tipo callable que toma un booleano como parámetro y retorna un int

funcionQueTomaStryDevuelveInt = Callable[[str],int] # alias de un tipo callable

#ciclos for indexados con 'enumarate'
def imprimirIndiceyElemento(vector: list) -> None:
    for idx,b in enumerate(vector): 
        print(f"{idx=}|{b=}")

#ciclos con else
def ciclosConElse(limiteRango : int  = 50):
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

# try...except...finally en manejo de errores
def unaFuncion(*args,**kwargs):
    pass

def manejarError(error):
    pass

def hacerSiempre():
    pass

try:
    unaFuncion("hola",5,[2,3])
except Exception as e:
    manejarError(e)
finally:
    hacerSiempre()
    

#comprensión de listas
def imprimirYDevolverCuadrado(numero : int):
    cuadrado : int = numero*numero
    print(numero*cuadrado)
    return cuadrado

lista : list[int] = [1,2,3,4,5,6,7,8,9,10]


"el sintagma"
listaCuadrados : list[int] = [imprimirCuadrado(num) for num in lista if num % 2 == 0]

"es equivalente a"
listaCuadrados : list[int] = []
for num in lista:
    if num % 2 == 0:
        listaCuadrados.append(imprimirCuadrado(num))


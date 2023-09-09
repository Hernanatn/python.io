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

#alias de tipos
funcionQueTomaStryDevuelveInt = Callable[[str],int]

#ciclos for indexados con 'enumarate'
for idx,b in enumerate(vector): 
    print(f"{idx=}|{b=}")

#ciclos con else
def ciclosConCierre(limiteRango : int  = 50):
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


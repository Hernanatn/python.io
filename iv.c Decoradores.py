
from typing import Callable


def imprimible(funcion):
    def envolvente(*posicionales,**nominales):
        resultado = funcion(*posicionales,**nominales)
        print(resultado)
        return resultado
    return envolvente



bool 
@imprimible
def sumar(x: int, y: int) -> int:
    resultado : int = x+y
    return resultado

x :int = 5
y :int = 8


z :int = sumar(x,y) 
# ^^^^^^^^^^^^^^^^
# Esto, por el decorador, es equivalente a:

z : int = envolvente(sumar(x,y))

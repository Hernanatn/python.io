from sys import getsizeof

def imprimirTamano(o: object):
    print(f"Tamaño [{type(o).__name__}],{o} {getsizeof(o)}")

imprimirTamano(object)
imprimirTamano(False)


entero1 : int = 1073741823
entero2 : int = 1073741824
entero3 : int = 1990000000000000001


imprimirTamano(entero1)

imprimirTamano(entero2)
flotante1 : float = 0.0
flotante2 : float = 10737418236699999999999999966666666.997

imprimirTamano(flotante1)

complejo1 : complex = complex(1073741824,7)
imprimirTamano(complejo1)

listaVacia : list = []
imprimirTamano(listaVacia)


lista2 : list = []
for i in range(100):
    lista2.append(i)
    print(f"{len(lista2)=}")
    imprimirTamano(lista2)
    

byteArrVacio : bytearray = bytearray()
imprimirTamano(byteArrVacio)


byteArr2 : bytearray = bytearray()
for i in range(100):
    byteArr2.append(i)
    print(f"{len(byteArr2)=}")
    imprimirTamano(byteArr2)
    

imprimirTamano(None)

imprimirTamano(...)

imprimirTamano(NotImplemented)

imprimirTamano(range(0))
imprimirTamano(range(10737400000000000000000000000000000000001824))


dictVacio : list = {}
imprimirTamano(dictVacio)


dict2 : list = {}
for i in range(100):
    dict2[i] = i
    imprimirTamano(dict2)
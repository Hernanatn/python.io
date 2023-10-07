# **_e.g._** Implementación de una lista personalizada, con @total_ordering e interfaz completa.
from collections.abc import MutableSequence
from functools import total_ordering
from typing import TypeVar, Generic

_T = TypeVar('T')

@total_ordering
class MiLista(MutableSequence):

    def __init__(
        self,
        listaInicial : list[_T] = None
                ) -> None:  
        if listaInicial:
            if isinstance(listaInicial, list):
                self.data[:] = listaInicial

            elif isinstance(listaInicial, MiLista):
                self.data[:] = listaInicial.data[:]
            else:
                self.data = list(listaInicial)

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        for dato in self.data:
            yield dato    

    def __reversed__(self):
        return self.data.reverse()

    def __getitem__(self,indice : int):
        if isinstance(indice, slice):
            return self.__class__(self.data[indice])
        else:
            return self.data[indice] 

    def __contains__(self,dato : _T):
        return dato in self.data

    def __setitem__(self, indice : int, dato : _T):
        self.data[indice] = dato

    def __delitem__(self, indice : int):
        del self.data[int] 

    def __castEstatico(self, otro):
        return otro.data if isinstance(otro,MiLista) else otro

    def __eq__ (self,otro):
        return self.data == self.__castEstatico(otro)
    
    def __gt__ (self,otro):
        return self.data > self.__castEstatico(otro)

    def __add__(self, otro):
        if isinstance(otro,MiLista): self.__class__(self.data + otro.data)
        elif  isinstance(otro,type(self.data)): self.__class__(self.data + otro)

    def __radd__(self, otro):
        return self.__class__(self.data + otro.data) if isinstance(otro,MiLista) else None
    
    def __iadd__(self, otro):
        if isinstance(otro, MiLista): self.data += otro.data
        elif isinstance(otro, type(self.data)): self.data += otro
        else: self.data += list(otro)
        return self

    def agregar(self, dato : _T):
        self.data.append(dato)

    def insertar(self, indice : int, dato: _T):
        self.data.insert(indice, dato)

    def soltar(self, indice : int=-1):
        return self.data.pop(indice)

    def eliminarDato(self, dato: _T):
        self.data.remove(dato)

    def limpiar(self):
        self.data.clear()

    def copiar(self):
        return self.__class__(self)

    def contar(self, dato: _T):
        return self.data.count(dato)

    def indice(self, indice : int, *posicionales):
        return self.data.index(indice, *posicionales)

    def invertir(self):
        self.data.reverse()

    def ordenar(self, /, *posicionales, **nominales):
        self.data.sort(*posicionales, **nominales)

    def extender(self, otro):
        if isinstance(otro, MiLista): self.data.extend(otro.data)
        else: self.data.extend(otro)


    def __repr__(self):
        return f"""<{self.__class__.__name__} data: {repr(self.data)}>"""
    
    def __llave(self):
        return (self.attr_a, self.attr_b, self.attr_c)

    def __hash__(self):
        return hash(self.__llave())


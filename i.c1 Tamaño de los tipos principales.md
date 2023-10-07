# Tamaño de los tipos principales (CPython | 64-bit)

## Primitivos

| Tipo       | Tamaño     |
|------------|------------|
| `object`   | 16 bytes   |
| `bool`     | 28 bytes   |

### Numéricos

| Tipo       | Representa    | Tamaño        |
|------------|---------------|---------------|
| `int`      | Enteros       | 28 bytes (+4) |
| `float`    | Reales (PF)   | 24 bytes      |
| `complex`  | Complejos     | 32 bytes      |

## Colecciones

| Tipo         | Especie       | Tamaño vacío  | Tamaño n elem.               | C. Espacial   |
|--------------|---------------|---------------|------------------------------|---------------|
| `list`       | S. Mutable    | 56 bytes      | 56 + n^2/(2^3) + 6*n bytes   | O(n^2)        |
| `bytearray`  | S. Mutable    | 56 bytes      | 58 + 3(n^2)/4 bytes          | O(n^2)        |
| `str`        | S. Inmutable  | 49 bytes      | 49 + n bytes                 | O(n)          |
| `tuple`      | S. Inmutable  | 28 bytes      | 40 + 8*n bytes               | O(n)          |
| `range`      | S. Inmutable  | 24 bytes      | 48 bytes                     | O(1)          |
| `bytes`      | S. Inmutable  | 32 bytes      | 56 + n^2 bytes               | O(n^2)        |
| `set`        | Conjunto      | 232 bytes     | 216 + 2n* 512*(512//n) bytes | O(n)          |
| `frozenset`  | Conjunto      | 232 bytes     | 216 + 2n* 512*(512//n) bytes | O(n)          |
| `dict`       | Mapeo         | 64 bytes      | 64 + k + log2(k) + v bytes   | O(n+m)        |

## Constantes

| Constante          | Tipo                   | Tamaño     |
|--------------------|------------------------|------------|
| `None`             | `NoneType`             | 16 bytes   |
| `...` ó `Ellipsis` | `ellipsis`             | 16 bytes   |
| `NotImplemented`   | `NotImplementedType`   | 16 bytes   |




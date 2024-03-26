# Métodos en Python

A continuación, se mostrarán algunos métodos de Python, que permiten facilitar algunas tareas.

## Método zip( )
El método **zip( )**, toma dos o mas iterables y los combina en una sola estructura de datos tipo [tupla]()

Suponiendo que se tiene la siguiente tabla:
|lon |  lat|
|-|-|
|-98.5 |    37.0|
|-122.3  |  47.6|

La tabla almacena datos de coordenadas longitud (lon) y latitud (lat) y se requiere, crear un atributo de geometria para un mapa. El atributo debe tener la siguiente estructura:
```diff
POINT (x,y)
```
Donde **x**, contiene el valor de la *longitud* y **y**, almacena el valor de la *latitud*. Por medio de una [list comprehension](https://github.com/r3card0/Python-Notes/blob/main/PythonIntermediate/17_list_comprehensions.ipynb), y el método **zip( )**, se puede crear este atributo u objeto de geometría a partir de los datos de la tabla.

```python
geometry = [POINT(xy) for xy in zip(lon,lat)]
```

El resultado será:
|geometry|
|-|
|POINT(-98.5, 37.0)|
|POINT(-122.3, 47.6)|

Observa que el método **zip( )** combinó los valores de las coordendas *lon* y *lat* y creó una tupla de coordenadas.

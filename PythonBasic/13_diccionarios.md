# Diccionarios en Python
Los diccionarios son estructoras de datos que alamacenan informacion en pares. Estos pares se les conoce como keys y values. Los keys, serian como los encabezados de una tabla y los values, representan los valores de la columna.

Un diccionario, no puede tener dos keys con el mismo nombre. Los valores si pueden repetirse. 

Los diccionario son estructuras de datos ordenadas. 

A pesar que de que se pueden escribir valores repetidos en un diccionario y no levanta error. en el momento de imprimirlo, unicamente presenta un resultado.
````
dicto1 = {
    'pais':'México',
    'pais':'México',
    }

print(dicto1)
````
Output
````
{'pais': 'mexico'}
````
De esta manera se comprueba que en los diccionarios, no se repiten valores. En otro ejemplo, se muestra el mismo dicionario con keys repetidos y con valores distintos. Al momento de imprimir el dicionario, noté que muestra únicamente el último par de diccionario.
````
dicto1 = {
    'pais':'México',
    'pais':'México',
    'pais' : 'USA',
    'pais': 'Argentina'
    }
 
 print(dicto1)
 ````
 Output
 ````
 {'pais': 'Argentina'}
 ````


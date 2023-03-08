# Diccionarios en Python
Los diccionarios son estructuras de datos que alamacenan informacion en pares. Estos pares se les conoce como keys y values. Los keys, serian como los encabezados de una tabla y los values, representan los valores de la columna.

Los diccionarios se crean usando { } y separando los keys de los values con **:**
````
diccionario = {
    'key1' : value
}
````

Los diccionarios pueden almacenar varias combinaciones de datos: texto, numeros, booleanos, listas, tuplas, sets y hasta otros diccionarios. Son estructuras de datos  complejas muy usados en la industria de la tecnología para alamacenar e intercambiar información entre aplicaciones. 

Un diccionario, no puede tener dos keys con el mismo nombre.

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


Los diccionarios son estructuras de datos ordenadas. 

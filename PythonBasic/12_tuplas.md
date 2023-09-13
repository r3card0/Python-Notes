# Tuplas (tuple)

Las tuplas son *[estructuras de datos](https://github.com/r3card0/Python-Notes/blob/main/PythonBasic/11_listas.md#estructuras-de-datos)* que pueden almacenar varios tipos de elementos en una sola variable y con la particularidad de que no permite eliminar o agregar elementos(items), como si ocurre con las [listas](https://github.com/r3card0/Python-Notes/blob/main/PythonBasic/11_listas.md#listas).

## Como crear una tupla
Las tuplas se crean usando paréntesis -> "**()**"
````
my_tuple = (1,2,3,4)

print(my_tuple)

$output: (1,2,3,4)
````

o bien con el método constructor *tuple()*, cuando se desea convertir una lista o set. Este método es muy util cuando se quiere crear una tupla para que sea usada en un script *sql*.
````
my_list = [1,2,3,4]
my_new_tuple = tuple(my_list)

print(my_new_tuple)

$output: (1,2,3,4)
````
## Características de las tuplas y diferencias con las [Listas](https://github.com/r3card0/Python-Notes/blob/main/PythonBasic/11_listas.md#listas)
* Son estructuras indexadas
* No pueden ser ordenadas
* Permite valores duplicados
* No permite borrar o agregar elementos (items) -> **inmutables**
* Son iterables

|Estructura | Indexed | Sorted | Duplicates | Mutable | Iterable |
|-----------|---------|--------|------------|---------|----------|
| LISTA | YES | YES | YES | YES | YES | 
| TUPLA | YES | NO | YES | NO | YES |

## Las tuplas son estructuras indexadas
Las tuplas son estructuras que tienen indices. Los indices son elementos numéricos internos de la tupla que permite asignar una posicion única al item que compone la tupla. De esta forma, permite ordenar, eliminar y agregar items dentro de la estructura (tupla). 

![image](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.scaler.com%2Ftopics%2Fmedia%2FPython-list-index-1-1024x498.jpeg&f=1&nofb=1&ipt=a6dbfa83da9f10b83b18f8d0146536d7a61d122006e0c87efdf0a86494d1193c&ipo=images)

Los índices, permiten:
  1. accesar a uno o varios items de la tupla
  2. contar la cantidad de elementos (item) en una lista

Para el caso de las tuplas, los elementos no se pueden ordenar (sort), ni eliminar ni agregar nuevos elementos


## Como accesar a los elementos de la Tupla
Como se vio anteriormente, se puede tener acceso a los elementos de las Tuplas a través de los índices. Para acceder a un elemento de la tupla solo se debe elegir el número del índice del elemento a través de **[ ]**. 

El siguiente ejemplo muestra como se puede tener acceso al elemento 'Shale' de la tupla, rock_tuple.

````
rock_tuple = ('Sandstone','Shale','Conglomerate')

print(rock_tuple[1])

$otuput: 'Shale'
````
Además, se puede usar el *Negative Indexing*, que permite elegir un elemento empezando desde el último elemento de la tupla. **-1** se refiere al último item, **-2** se refiere al penúltimo item de la estructura (Tupla) y así consecutivamente.

````
rock_tuple = ('Sandstone','Shale','Conglomerate')

print(rock_tuple[-2])

$otuput: 'Shale'
````

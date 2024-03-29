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

### Implementar **if**, para determinar si un elemento se encuentra en la Tupla
Para saber si un elemento específico está presente en una tupla, se puede usar **if** y **in**
````
clastic_rocks_tuple = ('Gravels','Sands','Clays')

if 'Clays' in clastic_rocks_tuple:
  print("Yes, 'Clays' is in the Clastic rocks tuple")
````
## Unpacking - Tupla
Cuando se crea una Tupla, normalmente se le asignan valores. A esta asignación se le llama "packing". En inglés, "packing a tuple"

En Python, se pueden extraer los elementos de una Tupla en varias variables. Esto es llamado **"Unpacking"**. Para aplicar el *"unpacking"*, se guardaran los elementos de la tupla ````clastic_rocks_tuple````, en tres diferentes variables: ````rock1````, ````rock2```` y ````rock3```` y esto se hace de la siguiente forma:
1. Se crea una tupla de variables. Aqui es muy importante, no usar comillas simples ni dobles
2. Se iguala la tupla de variables con la tupla. Muy importante es que el numero de variables de la tupla debe ser igual al numero de elementos contenidos en la tupla

````
clastic_rocks_tuple = ('Gravels','Sands','Clays')

(rock1,rock2,rock3) = clastic_rocks_tuple

print(rock2)
````
````
$output: Sands
````
### Aplicando * en el **unpakcing**

Si el número de variables es menor que el número de elementos, se puede usar el asterico * al nombre de la vriable y los valores serán asignados a la variable en forma de lista.


````
clastic_rocks_tuple = ('Gravels','Sands','Clays')

(rock1,*rock2) = clastic_rocks_tuple

print(rock2)

````
Output:
````
$output: ['Sands', 'Clays']
````
Otro ejemplo seria:
````
colors = ('red','white','green','brown','maroon')

(fruit,*meal, milk) = colors
print(milk)
print(fruit)
print(meal)
````
Output:
````
$output: maroon
$output: red
$output: ['white', 'green', 'brown']
````
# Aplicando loop "while" en la Tupla
El metodo *len( )* determina el numero de elementos en la tupla, ´para que el loop comience desde el índice 0, refiriendose a los índices. Hay que incrementar el índice por 1 en cada iteración.
````
colors = ('red','white','green','brown','maroon')

i = 0
while i < len(colors):
    print(colors[i])
    i = i+1
````
Output:
````
$output: red
$output: white
$output: green
$output: brown
$output: maroon
````
# Aplicando loop "for" en la Tupla
````
colors = ('red','white','green','brown','maroon')
for color in colors:
    print(color)
````
Output:
````
$output: red
$output: white
$output: green
$output: brown
$output: maroon
````

Se puede aplicar el loop *for* a través de referir el número del índice, usando las funciones *range( )* y *len( )* para crear un iterable

````
colors = ('red','white','green','brown','maroon')

for color in range(len(colors)):
    print(colors[color])
````
Output:
````
$output: red
$output: white
$output: green
$output: brown
$output: maroon
````

# Unir tuplas (Join)
Usar el operador **"+"** para unir tuplas. Los elementos de la segunda tupla se agregaran después de los elementos de la primera tupla
````
colors = ('red','white','green','brown','maroon')
colors2 = ('yellow','blue','beige')

colors3 = colors + colors2
print(colors3)
````
Output:
````
$output: colors = ('red', 'white', 'green', 'brown', 'maroon', 'yellow', 'blue', 'beige')

````
# Multiplicar Tuplas
La multiplicación entre tuplas se usa para dublicar los elementos en una nueva tupla. Recordando que las tuplas son inmutables y no aceptan cambios en el contenido de los elementos.

El operador **"*"**, permite duplicar elementos en nuevas tuplas.
````
colors = ('red','white','green','brown','maroon')
new_colors = colors * 2

print(new_colors)
````
Output:
````
('red', 'white', 'green', 'brown', 'maroon', 'red', 'white', 'green', 'brown', 'maroon')
````
# Métodos de las Tuplas

| Método | Descripción |
|--------|-------------|
|count( )| Retorna el número de veces que repite un elemento en la tupla |
|index( )| Retorna la posición (indice) de un elemento en la tupla. En caso de que el elemento se repita varias veces, retorna la posición de la primera ocurrencia | 

## Método count( )
Recibe como parámetro el valor del elemento de la tupla. De esta forma retorna el número de veces que se repite el valor en la tupla.
````
colors = ('red','white','green','brown','maroon')
new_colors = colors * 2

print(new_colors.count('maroon'))
````
Output:
````
$output: 2
````

## Método index( )
Recibe como parámetro el valor del elemento de la tupla. De esta forma, se busca y retorna la posición del elemento. En caso de que no se encuentre el valor, se levanta una *exception* de error.
````
new_colors = ('red', 'white', 'green', 'brown', 'maroon', 'red', 'white', 'green', 'brown', 'maroon')

print(new_colors.index('maroon'))
````
Para este contexto, el elemento *maroon* se repite dos veces, por lo que ocupa dos posiciones diferentes. El método *index( )* retorna solo la primera posición. En este caso es el índice 4
Output:
````
$output: 4
````

En caso de que el elemento buscado no se encuentre, se levanta una *exception*, si el valor no es encontrado
````
new_colors = ('red', 'white', 'green', 'brown', 'maroon', 'red', 'white', 'green', 'brown', 'maroon')

print(new_colors.index('sucks'))
````
Output:
````
ValueError                                Traceback (most recent call last)
Cell In[33], line 3
      1 new_colors = ('red', 'white', 'green', 'brown', 'maroon', 'red', 'white', 'green', 'brown', 'maroon')
----> 3 print(new_colors.index('sucks'))

ValueError: tuple.index(x): x not in tuple
````

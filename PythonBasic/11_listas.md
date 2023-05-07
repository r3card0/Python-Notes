# Estructuras de Datos

Las *variables* pueden almacenar un elemento. Las *listas* pueden almacenar más de dos elementos. Pueden almacenar una lista de elementos. Los elementos pueden ser textos, número o booleanos. En Python se conocen como items.

Las listas pertenecen a un conjunto llamado “**estructuras de datos**”.

Las **estructuras de datos** son formas que brindan los lenguajes de programación para guardar varios valores en una variable. Estos valores o items pueden tener diferente formato, como: strings, numéricos, boleados, etc

Por lo tanto, las listas pueden almacenar varios tipos de datos en una sola variable.

Para crear una lista se hace lo siguiente:

Nombre de la variable seguido el signo de “=“, abrir corchetes [ ] y dentro de los corchetes los tipos de datos que se desean guardar.

Ejemplo 1 . Crear una lista de planetas
```
lista = ['Mercurio','Venus','Tierra🌎','Marte','Júpiter','Saturno','Urano','Neptuno']
```

# Listas 

Las listas son estructuras de datos que permiten almacenar grupos de elementos. Los valores almacenados en las listas pueden tener diversos tipos de datos (data types)
```
lista_2 = [5,'cinco',5.5, True]
```
En este ejemplo, se puede observar que la lista contiene elementos con diferentes tipos de datos (data types)

## Características de las Listas
-  estructuras indexadas
-  pueden ser ordenadas, 
-  permiten valores duplicados, 
-  permiten borrar y agregar elementos (items) -> **mutables**
-  Sin iterables


## Listas son estructuras indexadas
Las listas son estructuras que tienen indices. Los indices son elementos numéricos internos de la lista que permite asignar una posicion única al item que compone la lista. De esta forma, permite ordenar, eliminar y agregar items dentro de la lista. 

![image](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.scaler.com%2Ftopics%2Fmedia%2FPython-list-index-1-1024x498.jpeg&f=1&nofb=1&ipt=a6dbfa83da9f10b83b18f8d0146536d7a61d122006e0c87efdf0a86494d1193c&ipo=images)

Los índices, permiten:
  1. accesar a uno o varios items de la lista
  2. ordenar elementos (item) en una lista
  3. contar la cantidad de elementos (item) en una lista
  4. eliminar y agregar items en la lista


## Acceso a los items de una lista

## Métodos usados en las listas
Los métodos son usados para distintos propósitos, lo cuales pueden orderar, eliminar, borrar, contar los elementos de las listas. A continuación se verán los métodos de las listas.

|Método| ¿Qué hace? | Sintáxis |
|------|-------------|----------|
|index()|Retorna la posición (index) de un item dando su valor| list.index('valor')|
|sort()|	ordena los items alfabeticamente y de forma ascendente en numeros| list.sort()|
|reverse()	| ordena los items de forma inversa | list.reverse()|
|append()|	Agrega un item en la ultima posición de la lista| list.append('item')|
|insert()|	inserta un item dando la posición donde se quiere agregar. Recibe dos parámetros, la posición donde se insertara el elemento y  el nombre del elemento| list.insert(2,'item')|
|extend()| Agrega los items de otra lista o cualquier iterable en la útlima posición de la lista| list.extend(list2)|
|clear() |	Elimina todos los elementos de una lista. Deja la lista vacía| list.clear()|
|pop() | elimina un item de la lista. Para eliminarlo, recibe como parámetro la posición del item| list.pop(2)|
|remove()	| Elimina un item de la lista. Para eliminarlo, recibe como parámetro el valor del item| list.remove('valor'(|
|copy()	| Retorna una copia de la lista. Se puede guardar en una nueva variable| copy_of_the_list = list.copy()
|count() |Retorna el numero de veces que se repite un item en la lista| list.count('valor')|

## ¿Por qué se dice que las listas son *Mutables*

Es conocido que las listas tienen la capacidad de mutabilidad o de ser mutables. Esto quiere decir que las listas pueden cambiar. y ¿Cómo cambian?, bueno, cambian por que algún elemento puede ser borrado o agregado a la lista. Esta característica, las convierte en **estructuras de datos mutables**. Y esto se logra con los métodos previamente vistos


## Resumen

Las listas son colecciones de elementos que pueden ser almacenados en una variable. Esta colección de elementos también se le conoce como estructura de datos. Y es una estructura de datos indexada (que tiene indices), ordenada, es mutable (se puede agregar o eliminar elementos) y puede contener elementos duplicados.


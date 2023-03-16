# Python Avanzado

## Objetivo
Este nivel explica como crear y usar closures, decoradores, generadores, sets
## Temas

28. [Como funciona Python](https://github.com/r3card0/Python-Notes/blob/main/PythonProfessional/28_Como_funciona_python.ipynb)
29. [Tipado Estatico](https://github.com/r3card0/Python-Notes/blob/main/PythonProfessional/29_Tipados.ipynb)
30. Alcance de variables: Scope
31. [Closures](https://github.com/r3card0/Python-Notes/blob/main/PythonProfessional/31_Closures.ipynb)
32. [Decoradores](https://github.com/r3card0/Python-Notes/blob/main/PythonProfessional/32_Decoradores.ipynb)
33. Iteradores
34. Generadores
35. [Sets](https://github.com/r3card0/Python-Notes/blob/main/PythonProfessional/36_Sets.ipynb)
36. [Operaciones en Sets](https://github.com/r3card0/Python-Notes/blob/main/PythonProfessional/37_Sets_operaciones.ipynb)
37. [Manejo de Fechas](https://github.com/r3card0/Python-Notes/blob/main/PythonProfessional/38_Manejo_de_Fechas.ipynb)
38. Time zones

## Decoradores
Un decorador es una función que recibe como parámetro otra función, modifica la lógica y retorna una función diferente.

En el script [saludo.py](/Projects/Python_Professional_Course/decoradores/saludo.py), hay definidas dos funciones. 
* La función principal es la función *saludo* y su lógica es retornar el string 'Hola'
* La función *decorador* se implementa como el *decorador* 😝
* La función *decorador* sigue la descripción inicial . . . es una función que recibe como parámetro otra función, en este caso, la función que recibe como parámetro será la función *saludo*, modificará la lógica de esta y agregará (modificará) el string, agregando el mensaje de la *nestedfunction* 'Esto se añade a la función -saludo-'

Para aplicar el decorador se hace lo siguiente: ```saludo = decorador(saludo)```

* La función saludo se maneja como varible y se le asigna como valor la función *decorador* y a su vez recibe como parámetro la función saludo
* Se ejecuta invocando la función original: ```saludo()```

Otra forma de aplicar el decorador es usando *sugar syntax*, la cual consiste en sustituir ```saludo = decorador(saludo)```, por 

```
@decorador
def saludo():
    print('Hola')
```

Esta forma es más estilizada y Pythonica y se implementa la misma lógica de un decorador.

```
def decorador(func):
    def nestedfunction():
        print('Esto se añade a la función -saludo-')
        func()
    return nestedfunction

@decorador
def saludo():
    print('Hola')

#saludo = decorador(saludo)
saludo()
```


Otro ejemplo es el siguiente script, [mayusculas.py](/Projects/Python_Professional_Course/decoradores/mayusculas.py), el cual se requiere que una funcion reciba como parametro cualquier texto y que el decorador convierta en mayusculas al texto recibido

1. se define primero el decorador
```
def mayusculas(func):
    def convertirMayuscula(texto):
        return func(text).upper()
    return convertirMayuscula
```
2. Se define la función que recibe el texto
```
def mensaje(nombre):
    return f'{nombre}, tienes un mensaje'
```
3. aplicar el decorador
```
@mayusculas
def mensaje(nombre):
    return f'{nombre}, tienes un mensaje'
```
Output
```
007, TIENES UN MENSAJE
```
Programar un script que permita saber cuanto tiempo tarda en correr un programa cualquiera
1. definir decorador
```
from datetime import datetime

def execution_time(func):
    def wrapper():
        initial_time = datetime.now()
        func()
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print('Pasaron ' + time_elapsed.total_seconds() + 'segundos')
    return wrapper
```
* El término *wrapper* se usa para indicar que la función es una envoltura o nested function
* Las líneas initial_time y final_time utilizan el método *datetime.now()*, el cual retorna el tiempo actual en que se ejecutó la línea
* El método *total_seconds()* convierte el tiempo en segundos

2. Definir la función original
```
def random_func():
    for _ in range(1,1000000):
        pass
```
* En este cilo , se busca ejecutar el ciclo 1000000 veces
* Cuando se implementa un ciclo *for* y no interesa indicar el valor que se está recorriendo en el ciclo, se suele usar el *guión bajo*,  *'_'*
* Se aplica el termino *pass* porque lo unico que se busca es saber el tiempo que tarde en aplicar el ciclo n veces

Output

Para 1000 veces
```
Pasaron 3.2e-05 segundos
```
Para 10000000 veces
```
Pasaron 0.281018 segundos
```
Para 1000000000 veces
```
Pasaron 28.767823 segundos
```
En esta función, no hubo parametros que recibiera la función original, pero que pasa si se usa el decorador en funciones que acepte uno, dos o cualquier numero de parámetros. Para eso se puede usar *args,**kwargs

* Estos args hace referencia a argumentos posicionales
* kwargs hace referencia a parametros nombrados *keywords arguments* -> (nombre= 'Cesar')
* Los *args y los **kwargs, se agregarán en la nested function y en la func()
```
from datetime import datetime

def execution_time(func):
    def wrapper(*args,**kwargs):
        initial_time = datetime.now()
        func(*args,**kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print('Pasaron ' + str(time_elapsed.total_seconds()) + ' segundos')
    return wrapper
```
De este modo, el decorador puede ejecutarse sin errores en funciones originales que requieran recibir parámetros.

ejemplo 1. [suma.py](/Projects/Python_Professional_Course/decoradores/suma.py)

```
from datetime import datetime

def execution_time(func):
    def wrapper(*args,**kwargs):
        initial_time = datetime.now()
        func(*args,**kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print('Pasaron ' + str(time_elapsed.total_seconds()) + ' segundos')
    return wrapper

@execution_time
def suma(a:int,b:int)->int:
    return a + b


print(suma(45,56))
```
Ejmplo 2 [nombre](/Projects/Python_Professional_Course/decoradores/nombre.py)
```
from datetime import datetime

def execution_time(func):
    def wrapper(*args,**kwargs):
        initial_time = datetime.now()
        func(*args,**kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print('Pasaron ' + str(time_elapsed.total_seconds()) + ' segundos')
    return wrapper

@execution_time
def saludo(nombre='Bruce'):
    print('Hola ' + nombre)


saludo('Batman')
```
En este ejmplo, se aplican parametros nombrados *keywords arguments* -> (nombre= 'Cesar') y **kwargs permite recibir este tipo de parámetros para que el script corra correctamente.

- [Yo soy tu padre](/Projects/Python_Professional_Course/decoradores/soytupadre.py)
- [Caja](/Projects/Python_Professional_Course/decoradores/caja.py)

## Referencias
- [ ] [Programando decoradores](https://platzi.com/clases/2397-python-profesional/39530-programando-decoradores/)

# Iteradores
Los iterables son los objetos que se pueden recorrer en un ciclo. Una lista es un iterable, un diccionario, tupla, set, strings.

Los iterables son estructuras de datos divisibles en elementos únicos que se pueden recorrer en un ciclo. 

Cuando Python recorre un iterable a través de un cilco *for*, lo que sucede es que el iterable se convierte en un objeto tipo *iterador* y es el *iterador* es que puede recorrerse con un loop dentro de Python.

* En Python no existe *for*, esto es *sugar syntax*
* Internamente el lenguaje es asi
```
# Creando el iterador
my_list = [1,2,3,4,5]
my_iter = iter(my_list)

# iterando el iterador
print(next(my_iter))
```
La estructura de datos, es convertida en un iterador, y para recorrerlo, se requiere la función *next*. 

Cuando termina de recorrer los elementos, se levanta la excepción *StopIteration*

Este recorrido se aplica cada vez que se ejecuta esta función *next*, pero que pasa cuando hay un millón de elementos, para eso Python ejecuta el siguiente codigo:
## Lógica interna de *for*
```
 # Creando el iterador
my_list = [1,2,3,4,5]
my_iter = iter(my_list)

# iterando el iterador -> su alias es el ciclo for
while True:
    try:
        element = next(my_iter)
        print(elment)
    except StopIteration:
        break
```
En este código se aplica un loop infinito mediante el comando *while*, donde se define que ejecute el ciclo mientras que encuentre o se presente el valor *True*, de esta forma de crea el ciclo infinito y cuando se termine de recorrer todos los elementos, entonces será un False y cuando eso suceda levantara la exception StopIteration.

Se implementan *try* y *except* para el manejo de errores

En *try*, se busca extraer e imprimir el siguiente elemento en el iterador. En la variable *element*, se asigna la tarea de *[next](/PythonProfessional/00_Python_Avanzado.md#next)(my_iter)*, el cual retorna el siguiente elemento del iterador *my_item*

En *except*, cuando los elementos terminan de recorrerse, levanta la *exception* *[StopIteration](https://www.w3schools.com/python/python_ref_exceptions.asp)*. Esto ocurre cuando al terminarse los elementos, el comando *break* corta el ciclo.

El ciclo *for* es la *sugar syntax* y el [codigo anterior](/PythonProfessional/00_Python_Avanzado.md#lógica-interna-de-for) se representa con el siguiente:
```
for element in my_list:
    print(element)
```
El ciclo *for* en realidad es un alias del loop infinito while True antes visto.

## next()
Esta función es [*built_in*](https://docs.python.org/3/library/functions.html), [next()](https://docs.python.org/3/library/functions.html#next) y su función es retornar el siguiente elemento en un iterador

1. Tener un a estructura de datos iterable
2. Convertir en iterador iter()
3. Iterar (repasar, recorrer) el iterador

el código infinito visto, permite aplicarlo en cualquier estructura de datos que haya sido convertida en iterador. Es una manera eficiente, de extraer todos los elementos de un iterador que proviene de un iterable.

## Referencias
- [ ] [Lista de palabras built-in](https://docs.python.org/3/library/functions.html)
- [ ] [Python keyword](https://www.w3schools.com/python/python_ref_keywords.asp)
- [ ] **StopIteration**:	Raised when the next() method of an iterator has no further values
- [ ] [**iter**: Returns an iterator object](https://docs.python.org/3/library/functions.html#iter)

# ¿Cómo construir un iterador personalizado?

# Built-in Functions

#### abs()
Returna el valor absoluto de un número. El valor absoluto de 4 es 4. El valor absoluto de -4 es 4. El valor absoluto de un número es su valor en positivo.

Recibe un parámetro como argumento, ya sea un valor directo o una variable

```
x = 8
y = 8.5
z = -8

print(abs(-4))
print(abs(x))
print(abs(y))
print(abs(z))
```
#### bin()
Returns the binary representation of an integer. retorna la representación binaria de un numero entero

examples:

[Birthday](/Projects/Fun/bin.py)
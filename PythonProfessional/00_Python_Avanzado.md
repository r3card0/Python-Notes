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
# Comando ***print( )***
![Hello](https://images.pexels.com/photos/3747150/pexels-photo-3747150.jpeg?auto=compress&cs=tinysrgb&w=600&lazy=load)

[📷 Picture by Polina Z.](https://www.pexels.com/@polina-zimmerman/)

## Objetivo
Aprender el uso del comando ***print( )***.

## Usos
El comando ***print( )***, se usa para imprimir objetos en pantalla. Los objetos pueden ser, *mensajes de texto*, *resultados de operaciones artiméticas*, variables, etc.

Para imprimir mensajes de texto, es necesario que el texto este encerrado entre comillas simples **'texto'** o dobles **"texto"**. En Python, se puede ocupar ambas comillas para este fin. En inglés, el *texto* es conocido como *string*.

### Hola Mundo 
Para empezar a usar este comando, comúnmente se usa el mensaje *¡Hola Mundo!* o *Hello World!* en inglés. Puedes crear tu primer línea de código en Python
```
print("Hola Mundo") # español
```
```
print('Hello world") # english version
```

Como se ha mostrado, los textos o *strings*, deben ir marcados entre comillas simples o dobles y además, estos *string*s pueden ir almacenados en *variables*. En el siguiente ejemplo, veremos como se asigna el string *¡Hola Mundo!* a la variable *saludo*
```
saludo = "¡Hola Mundo!"
```
el comando *print*, puede imprimir el mensaje contenido en la variable *saludo*
```
print(saludo)
```
Resultado:
```
¡Hola Mundo!
```

Ahora, supongamos que se tienen dos variables que almacenan mensajes de texto. El comando *print*, puede imprimir los mensajes de ambas *variables*
```
objetivo = "Estoy aprendiendo a programar en Python 🐍"
```
Ahora podemos imprimir los mensajes de las variables, *saludo* y *objetivo* 
```
print(saludo,objetivo)
```
Resultado:
```
¡Hola Mundo! Estoy aprendiendo a programar en Python 🐍
```
El comando *print*, puede imprimir los mensajes de ambas variables y usa el separador *coma* **" , "** para distinguir ambas variables. A la acción de *juntar* dos o mas mensajes de texto *(strings)*, en programación se le conoce como *concatenar* o *concatenate* en inglés. Para

## Imprimir números
Como en los textos, el comando *print* puede imprimir números. La forma correcta es la que sigue
```
print(6)
```
Resultado:
```
6
```
Los valores numéricos no requieren de comillas simples o dobles como los textos, a menos de que se usen como texto. 

Se pueden imprimir los resultados de operaciones matematicas
```
print(3 + 4)
```
Resultado
```
7
```
Como se explico en los strings, los valores numéricos pueden ser almacenados en variables
```
edad_pedro = 25
edad_maria = 24
```
Imprimir la edad de Pedro
```
print(edad_pedro)
```
Resultado:
```
25
```


## Imprimir strings y números


En el siguiente [link](https://colab.research.google.com/drive/1oInllSDvF5xxAhKwB5Ylrz4_JNcAUrxs?usp=sharing), encontrarás un notebook para practicar.



# Funciones *Built-in*
En Python existen funciones que pertenecen al grupo ***Built-in***. Estas funciones son predeterminadas, y esto quiere decir que por si mismas ya cumplen funciones (acciones) especificas y están creadas desde el lenguaje Python. El comando *print( ), es una funcion Built-in*. Hay muchas funciones Built-in en Python y que se verán mas adelante.

# Resumen
1. El comando print() es una función predeterminada de Python y está en la lista de las funciones Built-in.
2. Se usa para imprimir mensajes de texto, los cuales deben estar escritos entre comillas simples '' ó comillas dobles "".
3. Imprime resultados ariméticos.
4. Concatena valores de varias variables.

# Referencias
- [ ] [Curso basico de Python - platzi](https://platzi.com/cursos/python/)
- [ ] [Python.org](https://www.python.org/doc/essays/blurb/)
- [ ] [Real Python-python_print](https://realpython.com/python-print/)
- [ ] [Built-in functions](https://docs.python.org/3/library/functions.html)
- [ ] [Built-in functions|print](https://docs.python.org/3/library/functions.html#print)

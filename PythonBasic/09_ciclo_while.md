# Mientras Hagas Tu Tarea o Deberes, Jugaras Videojuego o Verás la Tele

Los papás comunmente le dicen a sus hijos que les darán permiso para algo que quieran los chamacos, como salir al cine con amigos, o simplemente conectarse para disfrutar de un videojuego o película y la frase que usana los papás comunmente es algo parecido a *"Si quieres ver la tele o jugar videojuegos, termina la tarea o tus deberes"*. Pero otra forma de decirlo y que es menos comun: *"Mientras hagas tu tarea o deberes, jugarás videojuegos o verás la tele" 🎮😄*

¡Así es el ciclo **WHILE**!, ¡Mientras se cumpla una condición, ejecuta el programa!

De esta manera se comienza la sintaxis de este loop en Python comenzando con la palabra clave en inglés ***WHILE***, que para los hispano-hablantes significa: ¡**MIENTRAS**!

Ver el siguiente ejemplo, donde se quiere imprimir en pantalla del 1 al 100, de 1 en 1. Entonces, podemos decir que mientras(while) el numero sea menor de 100, imprime en pantalla los números de 1 en 1. Estas palabras podemos llevarlas al codigo:

1. Creo la variable `number` y le indico donde empieza la numeración. En esta caso empieza en 0(cero): `number = 0`
2. Comienzo el ciclo con la palabra clave *while* seguida de la variable `number`, la cual quiero evaluar, con el operador  menor que `<` y finalmente el valor de 100 y termino con `:` y doy enter -> `while number < 100:`. Al dar enter, el siguiente reng{on deberá tener una indentación. Algunos editores de texto lo ponen automáticamente, pero siempre tener en cuenta.
4. Imprimir la secuencia de numeros. `print(number)`.
3. Crear un contador en la variable `number`, indicando que incremente en secuencia de 1. `number += 1`.

El programa quedará como sigue:

```python
number = 0
while number < 100:
  number += 1
  print(number)
```

# Encontrar el valor máximo en una lista
Hay dos formas de encontrar el valor máximo en una lista:
1. Usando el método **max( )**, el cual encuentra el valor máximo de un *iterable* o lista.
2. Aplicando una sentencia **for**

## Encontrar el valor máximo de una lista con el método *max( )*
La sintaxis correcta para aplicar el método *max( )*, es la siguiente:
```python
lista = [34,54,457,23,12,89,789]
# sintaxis: max(iterable)
valor_maximo = max(lista)
# imprimir resultado
print(valor_maximo)
```
Resultado
```bash
789
```

## Encontrar el valor máximo de una lista aplicando **for**
En este caso, se usa **for** para identificar el maximo valor de una lista, **for**, recorre todos los elementos de la lista, hasta encontrar el valor máximo:
```python
lista = [34,54,457,23,12,89,789]
valor_maximo = lista[0]
for elemento in lista:
  if elemento > valor_maximo:
    valor_maximo = elemento

print(valor_maximo)
```
En este codigo se desglosa:
- La línea ```valor_maximo = lista[0]```, permite establecer el inicio del recorrido de la lista, siendo el elemento de la posicion *0*, donde empezará el recorrido
- La Línea ```for elemento in lista:```, se establece que se recorreran los elementos de la lista
- La linea ``` if elemento > valor_maximo```, con la condicional *if*, recorrera cada elemento de la lista comparandolo con el valor de la variable *valor_maximo* , este recorrido se detendra cuando se cumpla la condicion de localizar el valor máximo de la lista
- La linea ```valor_maximo = elemento```, esta linea sustituira el valor cada vez que encuentre un valor mayor al anterior, hasta que termine de recorrer todos los elementos de la lista, retornando el valor mas alto.
- La linea ``` print(valor_maximo)```, imprime el valor maximo resultante.

## ¿Cuál de las dos anteriores es mejor?
Ambos métodos recorren la lista una vez para encontrar el valor máximo. Por lo tanto, en términos de eficiencia, ambos tienen una complejidad de tiempo similar, es decir, O(n), donde "n" es el número de elementos en la lista.

Sin embargo, el método `max(lista)` proporciona una sintaxis más concisa y legible, lo que lo hace preferible en la mayoría de los casos. Además, está implementado en C, lo que significa que es más rápido que el bucle `for` en Python puro.



# Encontrar el tercer valor máximo de una lista
Hsy dos maneras principales para encontrar el segundo, tercero o cualquier valor máximo de una lista:
- Ordenando la lista
- No ordenando la lista

Ordenar la lista, es el método mas sencillo para contrar el maximo valor deseado
```python
lista = [34,54,457,23,12,89,789]
lista.sort()
valor_maximo = lista[(len(lista) - 3)] # extrae el valor de la ante-penúltima posicion

print(valor_maximo)
```
Resultato
```
89
```

Sin ordenar la lista, requiere un poco más de codigo y nuevamente se utiliza el **for**.

Un forma es encontrar el valor máximo de la lista, almacenarlo en una variable que se llame por ejemplo *maximo_valor*, para después *removerlo* de la lista,  después, se repite el paso anterior, pero esta vez se almacena en una variable llamada *segundo_maximo_valor* y nuevamente se aplica el proceso, almacenando el maximo valor en una variable llamada *tercer_maximo_valor*

Aqui una propuesta aplicando lo anterior sin usar el método *max( )*:
```python
# encontrar el tercer valor maximo de una lista
lista = [34,54,457,23,12,89,789]

maximo_valor = lista[0]
for i in lista:
    if i > maximo_valor:
        maximo_valor = i
lista.remove(maximo_valor)

segundo_maximo_valor = lista[0]
for i in lista:
    if i > segundo_maximo_valor:
        segundo_maximo_valor = i
lista.remove(segundo_maximo_valor)

tercer_maximo_valor = lista[0]
for i in lista:
    if i > tercer_maximo_valor:
        tercer_maximo_valor = i
        
print(tercer_maximo_valor)
```
Resultado
```
89
```

Ahora aplicando el método *max( )*:
```python
lista = [34,54,457,23,12,89,789]
# encontrar el maximo valor
maximo_valor = max(lista)
lista.remove(maximo_valor)

# encontrar el segundo maximo valor
segundo_maximo_valor = max(lista)
lista.remove(segundo_maximo_valor)

# encontrar el tercer maximo valor
tercer_maximo_valor = max(lista)

print(tercer_maximo_valor)
```

En resumen, el primer enfoque es válido y eficiente para encontrar el valor máximo en una lista. Sin embargo, en la mayoría de los casos, se prefiere `max(lista)` debido a su mayor claridad y velocidad.

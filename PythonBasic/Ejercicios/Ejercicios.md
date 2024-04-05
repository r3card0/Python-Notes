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


# Encontrar el tercer valor máximo de una lista

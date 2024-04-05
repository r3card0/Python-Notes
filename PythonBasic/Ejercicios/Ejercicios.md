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


# Encontra el tercer valor máximo de una lista

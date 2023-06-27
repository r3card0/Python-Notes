
# Crear una lista de ids
Un ejemplo para extraer los elementos de una lista teniendo como elementos strings. La caracteristica de estos strings es que se pueden comportar como listas. Observa el siguiente arreglo:
```
['12345,34567','94856,2384767,294873','9584763,84756','823189,138988']
```
El objetivo es que todos estos elementos queden conformados en una única lista:
```
[12345,34567,94856,2384767,294873,9584763,84756,823189,138988]
```
La lista provenia de una columna de un dataframe de pandas. Cada celda contenia una lista de ids. La manera en que resolvi este problema fue el siguiente:
1. Convertir los datos de la columna en una lista: ```lis = list(df['ids']) ```
2. Crear una lista de listas. Implmentando un ciclo *for* para recorerr cada elemento (string) de la lista, estos elementos están dividiso internamente por una coma (,). Para crear la lista de elmentos, se implmenta el método *split()*, para que divida la cadena de caracteres y la convierta en una lista. Esta lista será agregada a la lista de listas.
   ```
   list_of_lists = []
   for a in lis:
     list_of_lists.append(a.split(','))
   ```
3. Crear la lista final. Implementando dos ciclos *for*. El primer ciclo, extraer los elementos de la lista principal (list_of_lists). Estos elementos extraidos son listas en si, y el segundo ciclo se implementa para extraer los elementos y agregarlos a la lista final.

   ```
   lista_final = []
   for d in range(len(list_of_lists)):
     for f in list_of_lists[d]:
       lista_final.append(f)
   ```
De esta manera, el resultado final es una lista de elmentos de tipo numerico, elimnando strings y listas anidadas.
```
[12345,34567,94856,2384767,294873,9584763,84756,823189,138988]
```

# Como castear un string a datetime
Con el modulo datetime, se puede castear un string al formato datetime.datetime, La siguiente función es una de tantas formas que existen.
```
import datetime

def timeCasting(string):
    format = "%Y-%m-%d" 
    stringDate = datetime.datetime.strptime(string, format)
    return stringDate
```
# Como castear datetime a date
De la anterior, se puede castear del formato *datetime.datetime* al formato *date*. Solo hay que agregar el constructor *.date()*
```
import datetime

def timeCasting(string):
    format = "%Y-%m-%d" 
    stringDate = datetime.datetime.strptime(string, format).date()
    return stringDate
```
# Como obtener la fecha -> hoy
Este código retorna el siguiente formato de fecha: YYYY-DD-MM
```
today = date.today()
```

# Como hacer una resta entre fechas
Para calcular la diferencia de dias entre dos fechas, se requiere que ambas fechas esten en el mismo formato.
```
import datetime
from datetime import date

dias = date.today() - datetime.datetime.strptime('2000-01-01', "%Y-%m-%d" ).date()
```
output

```
>>> print(dias)
8453 days, 0:00:00
```

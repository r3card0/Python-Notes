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

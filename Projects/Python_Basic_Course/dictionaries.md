# How to handle dictionaries?

## How to extract keys?

* By selecting the key name
```bash
dictionary_name['key_name']
```
Example:
```bash
# Students marks
student_marks = {
  'Jason' = [20,30,40],
  'Dick' = [40,60,32],
  'Damian' = [68,50,20],
  'Tim' = [10,70,43],
  }
 
# Use a variable to assign result
byKeyName = student_marks['Dick']
print(byKeyName)
```
Output
```
[40,60,32]
```

 

* By implementing *get* method
```bash
dictionary_name.get('key_name')
```

Example:
```bash
# Students marks
student_marks = {
  'Jason' = [20,30,40],
  'Dick' = [40,60,32],
  'Damian' = [68,50,20],
  'Tim' = [10,70,43],
  }
 
# Use a variable to assign result
get_method = student_marks.get('Dick')
print(get_method)
```
Output
```
[40,60,32]
```

# How to handle dictionaries?

## How to access to the values?

### Extract values by selecting the key name
```bash
# Proper syntax
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

 

### Extract the values by implementing *get* method
```bash
# Proper syntax
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

## How to access to the keys?
### Access to keys by implementing *keys* method to get a list of keys
```bash
# Proper syntax
dictionary_name.keys()
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
keys_method = student_marks.keys()
print(keys_method)
```
Output
```
dict_keys(['Jason','Dick',Damian','Tim'])
```
### Using *for* loop to list keys
```bash
# Proper syntax
for i in dictionary_name.keys():
  print(i)
```
Example:
```bash
for i in student_marks.keys():
  print(i)
```
Output:
```
Jason
Dick
Damian
Tim
```
### Access to keys and put them in a *list* (data structure)
Example
```bash
inThisList = [] # empty list
for i in student_marks.keys():
    inThisList.append(i)
return inThisList
```
Output:
```bash
['Jason','Dick','Damian','Tim']
```

    

## How to add a new key into a dictionary?
```bash
# Proper syntax
dictionary_name['new_key_name'] = 'value' # this could be any data type
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
 
# Add new key
student_marks['Stephanie'] = [100,45,87]

# Use a variable to assign result
keys_method = student_marks.keys()
print(keys_method)
```
Output
```
dict_keys(['Jason','Dick',Damian','Tim','Stephanie'])
```

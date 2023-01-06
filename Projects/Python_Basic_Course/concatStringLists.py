## Purpose of the script
def description():
    desc: str = """
    There are two unsorted lists of teams, from Group A and Group B. 
    World Cup Qatar 2022
    Group A: Nederlands, Senegal, Ecuador, Qatar
    Group B: England, USA, Iran, Wales
    1. Print both lists
    2. Concatenate lists
    3. Sort the new list
    4. Expected output: ['Ecuador', 'England', 'Iran', 'Nederlands', 'Qatar', 'Senegal', 'USA', 'Wales']
    """
    return desc

## Input - List of numbers
def groupA():
    groupA_ = ['Nederlands', 'Senegal', 'Ecuador', 'Qatar']
    return groupA_

def groupB():
    groupB_ = ['England', 'USA','Iran','Wales']
    return groupB_

## Concatenation of lists
def concatenateLists():
    newList = groupA() + groupB()
    return newList

## Sort the list
def sortList(list_):
  list_.sort()
  return list_

## Outputs
def run():
    print(description())
    print(groupA())
    print(groupB())
    print(sortList(concatenateLists()))
    
  
## entry point
if __name__ == '__main__':
    run()

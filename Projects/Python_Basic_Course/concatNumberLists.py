## Purpose of the script
def description():
    desc: str = """
    There are two unsorted lists of numbers
    List 1: 45,67,-9,0,234,-345, 5.78, -3.78, 12, 1
    List 2: 54,0.006, -452, 45.78,-4.5
    1. Concatenate lists
    2. Sort the new list
    3. Expected output: [-452, -345, -9, -4.5, -3.78, 0, 0.006, 1, 5.78, 12, 45, 45.78, 54, 67, 234]
    """
    return desc

## Input - List of numbers
def numbersList():
    numberList_ = [45,67,-9,0,234,-345, 5.78, -3.78, 12, 1]
    return numberList_

def anotherNumbersList():
    numberList_ = [54,0.006, -452, 45.78,-4.5]
    return numberList_

## Concatenation of lists
def concatenateLists():
    newList = numbersList() + anotherNumbersList()
    return newList

## Sort the list
def sortList(list_):
  list_.sort()
  return list_

## Outputs
def run():
    print(description())
    print(numbersList())
    print(anotherNumbersList())
    print(sortList(concatenateLists()))
    
  
## entry point
if __name__ == '__main__':
    run()

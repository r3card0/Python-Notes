## Purpose of the script
def description():
    desc: str = """
    This is a list of numbers
    45,67,-9,0,234,-345, 5.78, -3.78, 12, 1
    1. Sort the list
    2. Expected output: [-345, -9, -3.78, 0, 1, 5.78, 12, 45, 67, 234]
    """
    return desc

## Input - List of numbers
def numbersList():
    numberList_ = [45,67,-9,0,234,-345, 5.78, -3.78, 12, 1]
    return numberList_

## Sort the list
def sortList(list_):
  list_.sort()
  return list_

## Outputs
def run():
    print(description())
    print(numbersList())
    print(sortList(numbersList()))
    
  
## entry point
if __name__ == '__main__':
    run()

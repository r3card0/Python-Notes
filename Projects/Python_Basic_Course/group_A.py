## Purpose of the script
def description():
    desc: str = """
    This is the list of teams of the Group A in World Cup Qatar 2022
    Nederlands, Senegal, Ecuador, Qatar
    1. Sort the list
    2. Expected output: ['Ecuador', 'Nederlands', 'Qatar', 'Senegal']
    """
    return desc

## Input - The List
def groupA():
    groupA_ = ['Nederlands', 'Senegal', 'Ecuador', 'Qatar']
    return groupA_
 
## Sort the list
def sort_list(list_):
    list_.sort()
    return list_

## Outputs
def run():
    print(description())
    print(groupA())
    print(sort_list(groupA()))
    
  
## entry point
if __name__ == '__main__':
    run()

# Static Typing in Dictionaries
from typing import Dict


def dictionary():
    dict_personnel: Dict[str,int] = {
    "Sales" : 45,
    "Marketing" : 13,
    "Management" : 4,
    "Logistics" : 3
    }

    print(dict_personnel)

if __name__=="__main__":
    dictionary()
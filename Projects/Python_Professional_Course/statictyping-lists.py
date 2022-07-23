# Static typing in lists
from typing import List


def oil_well():
    well_list: str = ["Oil-1","Oil-2","Oil-3","Oil-4","Oil-5"]
    well_number: int = [34,56,78,2]
    production: float = [4.5,67.8,34.21]
    active: bool = [True,False]
    info_mix: List[str, int, bool, float] = ["Oil-1",34, True, 4.5]
    print("Tipos de datos str -> " , well_list)
    print("Tipos de datos int -> " , well_number)
    print("Tipos de datos float -> " , production)
    print("Tipos de datos booleans -> " , active)
    print("Tipos de datos combinados -> " , info_mix)

if __name__=="__main__":
    oil_well()
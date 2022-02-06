# Static Typing in Tuples
from typing import Tuple


def workflow():
    workflow_tuple: Tuple[str] = ("Stage-1","Stage-2","Stage-3","Stage-4","Stage-5")

    print(workflow_tuple)

if __name__=="__main__":
    workflow()
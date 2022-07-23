# example of a nested function

def pan(x:str):
    def ingrediente(y:str):
        return  x + y
    return ingrediente

bread = pan("esponjoso")

print(bread(" y de chocolate"))
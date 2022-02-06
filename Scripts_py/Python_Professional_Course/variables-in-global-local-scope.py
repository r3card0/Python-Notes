# Variables names created in global and local scope.

cama = "de la recamara principal"

def recamara1():
    cama ="de la racamara 1"
    

    def recamara2():
        cama = "de la recamara 2"
        print(cama)                 # from the function recamara2
        
    recamara2()

    print(cama)                     # from the function recamara1

recamara1()

print(cama)                         # variable created in global scope
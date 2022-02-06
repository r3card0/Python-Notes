# Variable created in a global scope
techo = "blanco" # variable con alcance global

def recamara():
    cama = "individual"
    print("La cama es", cama, "y el techo es de color", techo)

recamara()

def cocina():
    campana = "acero inoxidable"
    print("La campana de la cocina es de", campana, "y se ve muy bien con el techo", techo)


if __name__=="__main__":
    cocina()
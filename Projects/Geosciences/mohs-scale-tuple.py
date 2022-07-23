# tuple of mohs scale of hardness

def encabezado():
    print("Mohs scale of hardness: ")

encabezado()

def mohs_scale():
    mohs_tuple = ('1.Talc','2.Gypsum','3.Calcite','4.Fluorite','5.Apatite',
        '6.Orthoclase','7.Quartz','8.Topaz','9.Corundum','10.Diamond')
    for hardness in mohs_tuple: # list the tuple
        print(hardness)

mohs_scale()
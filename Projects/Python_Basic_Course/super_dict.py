def description():
    """This program generates a dictionary of lists
    """

description()

def supermarket_dict():
    supermarket_dict = {
        'list 1': ['pan bimbo', 'arroz', 'pasta:coditos','pasta:spaguetti',
         'jamon','mayonesa','bolillo','pan dulce','cereal','atún','bimbollos',
         'aceite','papas fritas congeladas','Harina para hotcakes','pan molido',
         'catsup', 'mostaza'],
        'fruits': ['manzana','plátano','papaya'],
        'lacteos': ['queso cottage','mantequilla'],
        'básico': ['huevo','tortilla', 'queso','leche','Agua','tomate','cebolla'],
        'carnes': ['pollo entero','carne molida'],
        'verduras' : ['calabaza','brocoli']
    }

    for category,articulos in supermarket_dict.items():
        print(category,articulos)

    #return supermarket_dict

def  write():
    names = supermarket_dict()
    with open('./superList.csv','w') as f:
        for name in names:
            f.write(name)
            f.write('\n')

def run():
    #make_file = write()
    supermarket_dict()

if __name__ == '__main__':
    run()
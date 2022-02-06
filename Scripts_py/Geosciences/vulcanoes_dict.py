# create a dictionary of vulcanoes in America
def run():
    vulcanoes_in_america = {
        'USA' : 'Yellowstone',
        'México' : 'Popocateptl',
        'Hawai' : 'El Kilauea',
        'Colombia' : 'Nevado de Ruiz',
        'Guatemala' : 'Volcán de Fuego',
        'Nicaragua' : 'Momotombo',
        'Costa Rica' : 'Arenal',
        'Chile' : 'Villarrica',
        'Ecuador' : 'Reventador',
        'Perú' : 'Misti',
        'El Salvador' : 'Volcán de Santa Ana',
        'Panamá' : 'Volcán Barú'
    } 
    # for pais in vulcanoes_in_america.keys(): # print keys
    #     print(pais)

    # for volcan in vulcanoes_in_america.values(): # print values
    #     print(volcan)

    # for pais_volcan in vulcanoes_in_america.items(): # print keys and values = items
    #     print(pais_volcan)

    for pais, volcan in vulcanoes_in_america.items(): # another variant for printing items
        print('En ' +  pais + ' está el volcán: ' + volcan)



if __name__ == '__main__':
    run()
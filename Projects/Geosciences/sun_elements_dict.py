# Elements of the Sun 🌞

def intro():
    print(""" 
    This is a dictionary of the chemical elements of the Sun 🌞
    """)

def sun_elements():
    sun_elements_sym = {
    'H':'Hydrogeno',
    'He' : 'Helio',
    'O': 'Oxígeno',
    'N':'Nitrogeno',
    'Si':'Silicio',
    'Mg':'Magnesio',
    'Na':'Sodio',
    'K':'Potasio',
    'Ca': 'Calcio',
    'P': 'Fósforo',
    'S':'Azufre',
    'Fe':'Fierro',
    'Al':'Aluminio',
    'Cu': 'Cobre'
    }
    for symbol, element in sun_elements_sym.items():
        print(symbol,":", element)

def run():
    intro()
    sun_elements()
   


if __name__ == '__main__':
    run()
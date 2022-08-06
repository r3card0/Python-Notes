description = """
This program prints every possible sorbet duos from a given list of flavors.
This is an exercise taken from Hack in Science web page:
https://www.hackinscience.org/exercises/print-sorbet-flavors

"""

FLAVORS = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]

duos = []
menu = []

def duo():
    if len(FLAVORS) >= 2:
        for i in range(0,len(FLAVORS)):
            for j in range(0,len(FLAVORS)):
                if (i != j):
                    duos.append([FLAVORS[i],FLAVORS[j]])
        return duos

#print(duo())

def duo_sort():
    duos = duo()
    for o in range(len(duos)):
        duos[o].sort()  

    duos.sort()

    return duos

#print(duo_sort())

def coma():
    duos = duo_sort()
    for f in range(len(duos)):
        duos[f].insert(1,", ")

    return duos

#coma()

def create_menu():
    duos = coma()
    #print(len(duos))
    for y in range(len(duos)):
        if y % 2 == 0:
            #print(duos[y])
            menu.append(duos[y])
    
    return menu

# print(create_menu())


def convert_to_string():
    menu = create_menu()
    for z in menu:
        menu = ''.join(z)    
        print(menu)

convert_to_string()




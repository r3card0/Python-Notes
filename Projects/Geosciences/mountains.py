# select an option to watch the info
def mountain_info(info,elevation):
    print(info + "and its highest point is about " + str(elevation) + " m")


def choose_mountain():
    mountain_menu = int(input(""" 
    
    Sierra Madre Occidental     1
    Sierra Madre Oriental       2
    Cordillera Neovolcánica     3
    Sierra Madre del Sur        4
    Sierra Madre de Chiapas     5
    Sierra Madre de Oaxaca      6

    Please select an option: """))

    if mountain_menu == 1:
        mountain_info("The Sierra Madre Occidental is a high plateau of volcanic rock ",3311)

    elif mountain_menu == 2:
        mountain_info("The Sierra Madre Oriental is a mountain range in northeastern Mexico ",3700)

    elif mountain_menu == 3:
        mountain_info("The Trans-Mexican Volcanic Belt spans across Central-Southern Mexico from the Pacific Ocean to the Gulf of Mexico ",5767)
    
    elif mountain_menu == 4:
        mountain_info("The Sierra Madre del Sur is a mountain range in southern Mexico ",3720)

    elif mountain_menu == 5:
        mountain_info("The range runs northwest–southeast from the state of Chiapas in Mexico",4220)

    elif mountain_menu == 6:
        mountain_info("It is primarily in the state of Oaxaca, and extends north into the states of Puebla and Veracruz ",3396)

    else:
        print("Please! Choose a correct option")


if __name__=='__main__':
    choose_mountain()



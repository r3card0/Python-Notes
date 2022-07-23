import random

def description():
    """This program generates a password taking 
    characters from a set of lists
    """
description()

def password_generator():
    upperc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    lowerc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbols = ['*', '+', '-',  '@', '_', '?', '!', '&', '$', '#']
    chars = upperc + lowerc + numbers + symbols

    password = []

    for i in range(12):
        char_random = random.choice(chars)
        password.append(char_random)
    
    # convertir una lista en string
    password = ''.join(password)
    return password



def run():
    password = password_generator()
    print('Tu nueva contraseña es: ' + password)


if __name__=='__main__':
    run()
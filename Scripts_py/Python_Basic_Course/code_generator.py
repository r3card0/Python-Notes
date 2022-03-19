import random

def description():
    """This program generates a serie of random codes and save them 
    in a csv file
    """
description()

def code_generator():
    upperc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    #lowerc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    #symbols = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
    chars = upperc + numbers 

    code = []
    
    for i in range(8):
        char_random = random.choice(chars)
        code.append(char_random)
        #print(code) imprime cada iteracion
    #return code # imprime una lista de 8 caracateres, por separado
    
    # convertir una lista en string
    code = ''.join(code)
    return code

def lista():
    code_list = []
    
    for x in range(70):
        code = code_generator()
        code_list.append(code)
    return code_list


def  write():
    names = lista()
    with open('./codes.csv','w') as f:
        for name in names:
            f.write(name)
            f.write('\n')

def run():
   make_file = write()

    # code_list = lista()
    # print(code_list)


if __name__=='__main__':
    run()
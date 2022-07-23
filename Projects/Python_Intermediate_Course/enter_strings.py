# while True:
#     try:
#         x = str(input('Por favor, ingresa un texto: '))
#         break
#     except ValueError:
#         print('¡Uups! Este no es un número. ¡Por favor, intenta de nuevo :)!')


# funciones try y except
def run():
    def palindrome(word):
        # word = input('Ingresa un texto: ')
        return word == word[::-1]

    try:
        print(palindrome(word= str(input('Ingresa un texto: ')))) # en este espacio se evalua si es un string o no -> 
    except TypeError:  
        print('Solo se puede ingresar texto')


if __name__=='__main__':
    run()
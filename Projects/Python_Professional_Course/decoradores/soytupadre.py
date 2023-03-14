# decorador
def soyTuPadre(func):
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
        print('Yo soy tu padre 😎')
    return wrapper

# función original
@soyTuPadre
def luke():
    print('¿Quien eres Darth Vader? 🤔')

luke()
print('Noooooo! 😱')
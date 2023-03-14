def decorador(func):
    def nestedfunction():
        print('Esto se añade a la función -saludo-')
        func()
    return nestedfunction

@decorador
def saludo():
    print('Hola')

#saludo = decorador(saludo)
saludo()
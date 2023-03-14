def mayusculas(func):
    def convertirMayusculas(text:str):
        return func(text).upper()
    return convertirMayusculas

@mayusculas
def mensaje(name:str):
    return f'{name}, tienes un mensaje'

print(mensaje('007'))
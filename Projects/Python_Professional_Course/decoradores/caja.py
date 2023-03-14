def borders(func):
    def wrapper(text:str):
        print(" " + "_" * (1 + len(text)))
        print("/" + "_" * (len(text)) + "/|")
        #print("|" + "_" * (len(text)) + "||")
        func("|" + text + "||")
        print("|" + "_" * (len(text)) + "|/")
    return wrapper

@borders
def imprimir(texto:str):    
    print(texto)

def run():
    texto = str(input('Escribe un texto: '))
    imprimir(texto)

if __name__ == "__main__":
    run()
def description():
    """This program is an example of the usage of assert statement to avoid user input a negative number 
    """



def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    num = input("ingresa un número: ")

    # -- ASSERT STATEMENT -- 
    # método de los string isnumeric(), devuelve verdadero si el valor ingresado es tipo numérico y False si no lo es
    # nota, para que el método funcione, es recomendable eliminar int en la variable num en el input
    assert num.isnumeric() and int(num) > 0, "Se debe ingresa un número positivo" 
    
    print(divisors(int(num))) # aqui si se castea la variable num 
    print("Terminó mi programa")


if __name__ == "__main__":
    run()
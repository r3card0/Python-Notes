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
    # nota, para que el método funcione, es recomendable eliminar int en la variable num
    assert num.isnumeric(), "Se debe ingresa un número" 
    
    print(divisors(int(num))) # aqui si se castea la variable num 
    print("Terminó mi programa")


if __name__ == "__main__":
    run()
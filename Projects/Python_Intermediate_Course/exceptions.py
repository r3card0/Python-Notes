# try, except, raise exceptions
def divisors(num):
    divisors = []
    try:
        if num < 0:
            raise ValueError('No se permiten valores negativos')    
        for i in range(1,num+1):
            if num % i ==0:
                divisors.append(i)
        return divisors
    except ValueError as ve:
        print(ve)
        return False
    


def run():
    try:
        num = int(input('Ingresa un número: '))
        print(divisors(num))
        print('Terminó el programa')
    except ValueError:
        print('Debes de ingresar un número')


if __name__ == '__main__':
    run()
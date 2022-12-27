def fibonacci(num: int):
    
    if num == 0:
        return 0
    
    elif num == 1:
        return 1
    
    else:
        return fibonacci(num - 2) + fibonacci(num -1)



def fibonacciRange():
    numberRange = int(input('Enter the Fibonacci Serie Number Range: '))

    for number in range(0,numberRange):
        print(fibonacci(number), end=' ')


def run():
    fibonacciRange()


if __name__ == "__main__":
    run()

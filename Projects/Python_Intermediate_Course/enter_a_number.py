# Example of: try - except commands.
def handling():
    while True:
        try:
            x = int(input('Enter a number: '))
            break
        except ValueError:
            print('¡Uups! This is not a number. Please! Try again!: ')
    print(str(x) + ' is a number. Thanks!')

def run():
    handling()

if __name__ == '__main__':
    run()
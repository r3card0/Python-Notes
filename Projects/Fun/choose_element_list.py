
# list of integers
strings = ['zero','one','two','three','four','five','six','seven']

def return_a_string(number:int):
    try:
        try:
            number = int(number)
        except ValueError:
            return 'Please enter and integer'
        for i in range(0,number+1):
            if i <= len(strings):
                return strings[number].upper()

    except IndexError:
        return 'OTHER'

def run():
    print(return_a_string('six'))

if __name__ == "__main__":
    run()
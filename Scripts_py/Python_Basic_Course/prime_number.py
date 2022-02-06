# Evaluates if a given number by the user it's prime number or it's not

# (2) prime number expression
def prime_number(number):
    counter = 0

    for i in range(1, number + 1):
        if i == 1 or i == number:
            continue
        if number % i == 0:
            counter += 1
    if counter == 0:
        return True
    else:
        return False

# (1) user input
def enter_a_number():
    number = int(input("Enter a number: "))
    if prime_number(number):
        print("Is a prime number")
    else:
        print("Is not a prime number")

if __name__=="__main__":
    enter_a_number()
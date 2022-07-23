def guess():
    number = int(input("Please! choose a number: "))
    while number != 95:
        if number > 95:
            print("Your number is greather than my number")
            number = int(input("Please! choose a number: "))
        elif number == 95:
            print("Great! Your number is equal than mine, is 95")        
        else:
            print("Your number is less than my number")
            number = int(input("Please! choose a number: "))

if __name__=="__main__":
    guess()


       
    
    










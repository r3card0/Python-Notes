def ask_for_password():
    password = str(input("Please! Guess the password: "))
    while password != 'please':
        print("This is not the password, please, try again!")
        password = input("Please! Guess the password: ")
    if password == 'please':
        print("Finally!")
        print("Bye!")


if __name__=='__main__':
    ask_for_password()
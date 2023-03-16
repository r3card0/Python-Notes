
class Guess:
    def __init__(self) -> None:
        self.password = str(input('Please! Guess the password: '))

    def ask_password(self):
        while self.password != 'please':
            print("This is not the password, please, try again!")
            self.password = input("Please! Guess the password: ")
        if self.password == 'please':
            print("Finally!")
            print("Bye!")

def run():
    game = Guess()
    game.ask_password()

if __name__=='__main__':
    run()


# def ask_for_password():
#     password = str(input("Please! Guess the password: "))
#     while password != 'please':
#         print("This is not the password, please, try again!")
#         password = input("Please! Guess the password: ")
#     if password == 'please':
#         print("Finally!")
#         print("Bye!")



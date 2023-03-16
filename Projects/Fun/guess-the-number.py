class GuessNumber:
    def __init__(self) -> None:
        self.number = int(input("Please! choose a number: "))
    
    def guess(self):
        while self.number != 15:
            if self.number == 15:
                print("Great! Your number is equal than mine, is 15")
                print("You done!")
            elif self.number > 15:
                print("Your number is greather than my number")
                self.number = int(input("Please! choose a number: "))
            # elif self.number == 15:
            #     print("Great! Your number is equal than mine, is 15")
            #     print("You done!")
            else:
                print("Your number is less than my number")
                self.number = int(input("Please! choose a number: "))

def run():
    game = GuessNumber()
    game.guess()

if __name__ == "__main__":
    run()



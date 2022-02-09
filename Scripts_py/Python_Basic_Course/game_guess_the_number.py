# Game to guess a number between a range. Usage of random module

import random

def game():
    random_number = random.randint(1,100)
    chosen_number = int(input("Please! Choose a number between 1 to 100: "))
    play_turn = 5
    while random_number != chosen_number:
        if chosen_number < random_number:
            print("Choose a bigger number")
            play_turn -=1
        else:
            print("Choose a lower number")
            play_turn -=1
        if play_turn == 0:
            print("GAME OVER!")
            break
        print("You have " + str(play_turn) + " lifes")
        chosen_number = int(input("Choose another number: "))
    print("YOU WIN!")

if __name__=="__main__":
    game()
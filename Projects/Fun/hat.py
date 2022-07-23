from datetime import datetime
from typing import List
import random

def execution_time(func):
    def wrapper(*args,**kargs):
        start_time = datetime.now()
        func(*args,**kargs)
        end_time = datetime.now()
        elapsed_time = end_time - start_time
        print(elapsed_time.total_seconds())
    return wrapper


#@execution_time
def hogwarts(): # select a house randomly 
    houses: List [str] = ['Gryfindor','Slytherin','Hufflepuff','Ravenclaw']
    for selected_house in houses:
        selected_house = random.choice(houses)
        print('¡¡¡¡',selected_house, '!!!!!')
        break
        

#@execution_time
def hat(string:str) -> str: # the hat salute to you
    magician: str = str(input("Your name magician, please!: "))
    print('Hi ' + str(magician) + ",I am the sorting hat")
    
    talk_list: List [str] = ["let me think what are your skills . . mmhh!! yess!! I feel it! Your new house is: ", 
    "Not Slytherin, eh?...Are you sure? You could be great, you know, it's all here in your head, and Slytherin will help you on the way to greatness, no doubt about that no? Well, if you're sure...better by...",
    "The founders put some brains in me. So I could choose instead! Now slip me snug around your ears, I've never yet been wrong, I'll have a look inside your mind. And tell where you belong!",
    "I sort you into Houses. Because that is what I’m for, But this year I’ll go further, Listen closely to my song: "]
    for talk in talk_list:
        talk = random.choice(talk_list)
    print(talk)



hat('Nombre')    
hogwarts()
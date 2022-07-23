# A paremeter is a variable which will get values. A parameter is defined in a function.

def conversation(message):
    print("Hi")
    print("How are you?")
    print(message)
    print("Goodbye")

choose_option = int(input("Please, choose and option (1, 2, 3): "))
if choose_option == 1:
    conversation("You choosed the option 1 🙂")
elif choose_option == 2:
    conversation("You choosed the option 2 😊")
elif choose_option == 3:
    conversation("You choosed the option 3 😌")
else:
    print("Choose a correct option 😝")
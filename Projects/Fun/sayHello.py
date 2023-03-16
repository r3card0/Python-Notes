# Write a program tht uses input to promt a user

class Hello:
    def __init__(self) -> None:
        self.name = str(input("Please!, enter your name: "))

    def say(self):
        return f"Hello {self.name}, nice to meet you! 😊"
    
def run():
    name = Hello()
    print(name.say())


if __name__=="__main__":
    run()

# def hello():
#     name = str(input("Please!, enter your name: "))
#     print("Hello",name,"nice to meet you! 🙂")


# if __name__=="__main__":
#     hello()
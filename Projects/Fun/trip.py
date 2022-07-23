def trip():
    savings = int(input("How money did you saved?: "))
    berlin = 800
    Newyork = 400
    if savings >= berlin:
        print("Congratulations! the germans are waiting for you with jars of beer! You saved to go to Berlin!")
    elif Newyork < savings:
        print("The Statue of Liberty greets you, because you're going to travel to New York")
    else:
        print("Ok! Prepare your sandwiches, soda and mosquito repellent, because you will visit your local park. Sorry!")


if __name__=='__main__':
    trip()
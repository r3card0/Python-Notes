# choose the serie
# choose the limit
def sequence():
    step = int(input("Please, select the increment number: "))
    stop = int(input("Now, select the limit: "))
    interval = range(0, stop, step)
    for i in interval:
        print(i)
    print("Thank you! 😊 ")


if __name__=="__main__":
    sequence()
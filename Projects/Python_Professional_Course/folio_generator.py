import datetime
#from datetime import datetime

def description():
    """This program generates sales folio
    """
description()

def date():
    my_day = datetime.date.today()
    print(str(my_day.year) + str(0) + str(my_day.month) + str(my_day.day))

def increment():
    part1 = date()

    for i in range(1,11):
        print(i)
    print(part1)
    

def run():
    date()
    #increment()

if __name__ == '__main__':
    run()

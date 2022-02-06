# programa to prompt the user for hours and rate per hour
# using input to compute gross pay

def rate_hours():
    hours = float(input("Enter hours: "))
    rate = hours * 2.75
    print("Pay:",rate)

if __name__=="__main__":
    rate_hours()
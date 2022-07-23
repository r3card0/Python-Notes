# Create a list of all numbers multiples of 4, 6 and 9 until 5 digits. List comprehension
#  [element for element in iterable if condition]

def multiples_of():
    list_multiples_long = [i for i in range(99999) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    list_multiples_short = [i for i in range(99999) if i % 36 == 0]
    # both options create the same result
    print(list_multiples_long)

if __name__ =="__main__":
    multiples_of()
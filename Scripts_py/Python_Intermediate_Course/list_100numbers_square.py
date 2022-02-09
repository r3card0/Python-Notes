# Create a list of squares of the first 100 natural numbers. List comprehension
# structure [element for element in iterable if condition]

def square():
    list_square_100_numbers =[i ** 2 for i in range(1,101)]
    print(list_square_100_numbers)

if __name__=="__main__":
    square()
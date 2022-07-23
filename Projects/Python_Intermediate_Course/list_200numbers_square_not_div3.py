# Create a list of squares of the first 200 natural numbers and not be divisible by 3. List comprehension
# structure [element for element in iterable if condition]

def square2():
    list_square =[i ** 2 for i in range(1,201) if i % 3 != 0]
    print(list_square)


if __name__=="__main__":
    square2()
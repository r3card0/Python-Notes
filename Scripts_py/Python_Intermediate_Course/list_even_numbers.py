# Create a list of even numbers from another source list. List comprehension
# [element for element in iterable if condition]

def even_numbers():
    source_list = [1,2,4,5,7,8,3,21,45,78,98,101,231,343,468,456]

    list_even_numbers = [i for i in source_list if i % 2 == 0]
    print(list_even_numbers)

if __name__=="__main__":
    even_numbers()
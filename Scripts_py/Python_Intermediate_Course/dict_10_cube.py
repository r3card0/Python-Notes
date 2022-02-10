# Create a dictionary to store 10 first natural numbers as keys and their cubed values as values. Dictionary comprehension
# {keys : value for value in iterable if condition}
def run():
    dict_10 = { i : i ** 3 for i in range(1,11)}
    print(dict_10)

if __name__=="__main__":
    run()
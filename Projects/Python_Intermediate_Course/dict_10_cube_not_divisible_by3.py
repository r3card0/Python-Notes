# Create a dictionary to store the 10 first natural numbers, (but not be divisible by 3) as keys and their cubed values as values. Dictionary comprehension
# {keys : value for value in iterable if condition}
def run():
    dict_10_3 = {i : i **3 for i in range(1,11) if i % 3 != 0}
    print(dict_10_3)


if __name__=="__main__":
    run()
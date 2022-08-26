def create_set1():
    set1 = []
    elements = input('Enter a set of elements: ')
    set1.append(elements)
    set1 = set(set1)

    return set1

print(create_set1())
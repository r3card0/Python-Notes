# Returns the mean of a list of grades
# Formula to calculate mean 
# ∑n/n -> sum of grades / number of grades
from functools import reduce

list_grades = [78,89,60,45,100,70,83,90,88,65]

def mean_grades():
    mean_of = reduce(lambda r,e : r + e, list_grades) / len(list_grades)
    return print(mean_of)


if __name__=="__main__":
    mean_grades()
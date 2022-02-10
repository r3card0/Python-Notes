# create a lambda function that sorts the list in descending order

exercise_list = [100,10,10000,1,9,999,99]

exercise_list.sort(key=lambda x : 100/x)

print(exercise_list)
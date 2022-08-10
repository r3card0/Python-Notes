#

students = [(85, "Susan Maddox"), (6, "Joshua Tran"), (37, "Jeanette Wafer")]

def sort_by_mark(any_list):
    any_list.sort(reverse=True)    
    return any_list

def sort_by_name(any_list):
    any_list.sort(key=lambda a: a[1])
    return any_list

print(sort_by_mark(students))
print(sort_by_name(students))
# Static Typing in variables

def message():
    print("*****  Static Typing in variables  *****")
    print("")

message()

def var():
    a: str = "Hi, everyone!"
    b: int = 2022
    c: float = 34.67
    d: bool = True
    print("The data type of this variable is: ", (type(a)), a)
    print("The data type of this variable is: ", (type(b)), b)
    print("The data type of this variable is: ", (type(c)), c)
    print("The data type of this variable is: ", (type(d)), d)

if __name__=="__main__":
    var()
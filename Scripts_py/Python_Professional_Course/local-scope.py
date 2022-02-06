# local scope.
# A variable created in a function just can be called in the function.

def bedroom():
    bed = "maked"
    print("The bed is: ", bed)

if __name__=="__main__":
    bedroom()
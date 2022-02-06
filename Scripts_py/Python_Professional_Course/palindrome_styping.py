# create a palindrome program
# create two functions
# function 1 return a bool. Use static typing
# remove trash spaces between words
# moves 360 the word
# second function runs the first function
# the function call recieves an integer as an argument

## this program was created by the instructor

def validation(string: str)-> bool:
    string = string.replace(" ","").lower()
    return string == string[::-1]

def palindrome():
    print(validation(7657))
    
if __name__=="__main__":
    palindrome()



# determine if a word or a sentence is a palindrome
def palindrome() -> str:
    word = input("Enter a word or a sentence: ")

    def blank():
        try:
            if len(word) == 0:
                raise ValueError('Blank space not allowed')
            return word == word[::-1]
        except ValueError as ve:
            print(ve)
            return False
    blank()
    try: 
        if word == str(word):
            word = (word.replace(" ","").strip()).lower()
            if word == word[::-1]:
                print("It is a palindrome 😉 ")
            else:
                print("It's NOT a palindrome 😕 ")
    except TypeError:
        print('Your choice is not a string')   
    

def run(): 
    palindrome()

if __name__=="__main__":
    run()
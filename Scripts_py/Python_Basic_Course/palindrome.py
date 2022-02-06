# determine if a word or a sentence is a palindrome
def palindrome():
    word = str(input("Enter a word or a sentence: "))
    word = (word.replace(" ","").strip()).lower()
    if word == word[::-1]:
        print("It is a palindrome 😉 ")
    else:
        print("It's NOT a palindrome 😕 ")

if __name__=="__main__":
    palindrome()
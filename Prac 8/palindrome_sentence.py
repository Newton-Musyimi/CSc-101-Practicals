def palindromeCheck(string):
    string = string
    if word == word[::-1]: #runs if a word is equal to its inverse
        print("It is a palindrome")
    else: #runs if a word is not equal to its inverse
        print("It is not a palindrome")

def main():
    string = input("Enter a word: ") #prompts the user for input
    palindromeCheck(string)
    
if __name__ == '__main__':
    main()

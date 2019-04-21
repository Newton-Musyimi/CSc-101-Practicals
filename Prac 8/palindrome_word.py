def palindromeCheck(word): #checks whether the word is a palindrome
    if word == word[::-1]: #runs if a word is equal to its inverse
        print("It is a palindrome")
    else: #runs if a word is not equal to its inverse
        print("It is not a palindrome")

def main(): #the main function
    word = input("Enter a word: ") #prompts the user for input
    palindromeCheck(word) #calls the function that checks whether the input is a palindrome
    
    
if __name__ == '__main__': #runs the main function
    main()
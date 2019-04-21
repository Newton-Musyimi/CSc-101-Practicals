"""This is a program that encrypts text using the Ceasar Cipher"""
def ceasarEncrypt(): #this is the function that carries out the encryption
    text = str(input("Enter the text you want encrypted: ")) #takes a string from the user
    text = text.upper() #converts the string into uppercase
    n = 13 #the rotation number is assigned
    i = 0
    while i<len(text): #the loop that gets each character from the string
        character = text[i]
        if character == " ": #the if statement that allows the program to ignore the space character
            encryption = 32
        else:
            """This else statement allows the line below to execute if the character
is not a space character. The line below works by converting the character in each
iteration of the loop into its integer equivalent and adding the rotation value"""
            encryption = ((ord(character) + n) - 65)%26+65 #the line of code that carries out the encryption
        cipher = chr(encryption) #converts the new integer value into its string equivalent 
        i = i+1 #adds 1 to the iteration value in order to move to the next character in the string
        print(cipher,end="") #print out the encrypted text
ceasarEncrypt() #calls the encryption function
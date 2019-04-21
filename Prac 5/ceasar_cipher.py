"""This is a program that encrypts or decrypts data using the Ceasar Cipher by taking text
and using a specified rotation number to either encrypt the text or decrypt it. The program
allows the user to choose whether the required task is encryption or decryption"""
def ceasarEncrypt(): #defines the encryption function
    text = str(input("Enter the text you want encrypted: ")) #takes in the string of characters to be encrypted in the form of a sentence
    text = text.upper() #converts the string to uppercase
    n = int(input("Enter a rotation number less than 26: ")) #prompts the user to enter the rotation value to be used in encrypting the string
    i = 0
    while i<len(text): #creates a loop that iterates for an equivalent to the number of characters in the string
        character = text[i]
        if character == " ": #an if statement to ignore the conversion of the space character
            encryption = 32
        else:
            """This else statement allows the line below to execute if the character
is not a space character. The line below works by converting the character in each
iteration of the loop into its integer equivalent and adding the rotation value
previously assigned by the user"""
            encryption = ((ord(character) + n) - 65)%26+65 #the line of code that encrypts the string
        cipher = chr(encryption) #this line converts each integer into its string equivalent
        i = i+1 #adds 1 to the iteration value in order to move to the next character in the string
        print(cipher,end="") #prints out the encrypted value of the string
def ceasarDecrypt(): #defines the decryption function
    text = str(input("Enter the text you want decrypted: "))
    text = text.upper()
    n = int(input("Enter a rotation number less than 26: "))
    i = 0
    while i<len(text):
        character = text[i]
        if character == " ":
            decryption = 32
        else:
            """This else statement allows the line below to execute if the character
is not a space character. The line below works by converting the character in each
iteration of the loop into its integer equivalent and subtracting the rotation value
previously assigned by the user in order to decrypt the string"""
            decryption = ((ord(character) - n) - 65)%26+65 #the line that decrypts the string
        decipher = chr(decryption) #converts the integer to its string equivalent
        i = i+1 #adds 1 to the iteration value in order to move to the next character in the string
        print(decipher,end="")
def ceasarCipher():
    action = int(input("type in 1 for encryption or 2 for decryption: "))
    if action==1: 
        ceasarEncrypt() #calls the encryption function if the action choosen was encrypt
    else:
        ceasarDecrypt() #calls the decryption function if the action choosen was decrypt
ceasarCipher() #calls the cipher function
def main():
    word = input("Input your text: ")
    split_str = word.split(" ")
    result = '' # variable to store the changed text; after every change made to a word.
    for iWord in split_str:
        if iWord[0] in ['a','e','i','o','u','A','E','I','O','U']:
            result += changeV(iWord)# iWord is the initial word when it starts with vowel
        else:
            result += changeC(iWord)#iWord is the initial word when it starts with consonant
    print(result)        
def changeV(Vword):    #function that changes words starting with vowel
    Vword +="way "
    return Vword#Vword is a word that starts with vowel
def changeC(Cword):# function to change words starting with consonant
    while Cword[0] not in ['a','e','i','o','u','A','E','I','O','U']:# This always takes the first character to the end as long as it is not a vowel yet
        Cword = Cword[1:]+ Cword[0]
    Cword=Cword+ "ay "
    return Cword#Cword is a wor that starts with a consonant
if __name__ == "__main__":
    main()#calls the main function
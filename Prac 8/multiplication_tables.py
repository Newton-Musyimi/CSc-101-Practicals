def numberInput(): #a function to take the user's input
    number = int(input("Enter a number: ")) #prompts the user for a number and converts the type to an int
    return number #returns the user's input to the calling function
def multiplicationTable(): #a function to generate the multiplication table
    number = numberInput()
    number += 1 #adds 1 to the user's input
    for i in range(1,number): #for loop to iterate the same number of times as the users input
        for j in range(1,number): #for loop to iterate the same number of times as the users input
            m = i * j #gets the value of the multiplication between i and j
            print('%d x %d = %d' %(i,j,m))#prints out the multiplixation table in the format i x j = m
def main(): #the main function
    multiplicationTable() #calls the multiplicationTable() function 
    
if __name__ == '__main__': #evaluates and runs the main function when True
    main()
    
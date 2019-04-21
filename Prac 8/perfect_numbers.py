"""
For perfect numbers, the formula is
f(p) = (2**(p-1))*(2**p - 1) where p is a prime number
The algebraic function of prime numbers is
f(n) = ((n!mod(n+1))/n)*(n-1)+2
"""

def findFactorial(n): #calculates the factorial of a number
    ans = 1
    for i in range(1, n+1): #a for loop that iterates until it finds the factorial of n
        ans = ans * i
    return ans
def getPrimes(number): #generates a list of prime numbers
    lst = []
    n = 1
    while len(lst)!= number:  #runs until the number of prime numbers in the list is equivalent to the number of perfect numbers the user requires
            n_factorial = findFactorial(n) 
            prime =int( ((((n_factorial)%(n+1))/n)*(n-1))+2) #finds integer prime numbers
            if prime in lst: #prevents duplication of prime numbers obtained during truncation
                pass
            else:
                lst += [prime] #adds the generated prime number into the list
            n += 1 #adds 1 to n in order to calculate the next prime number in the sequence
    #print (lst)
    return lst
def getPerfectNumbers(): #evaluates a specified number of perfect numbers
    numbers = [] #a list to store the perfect numbers generated
    number = int(input("Enter the number of perfect numbers you want: "))
    primes = getPrimes(number)
    for i in range(len(primes)):
        n = primes[i] #sets the value of n as the index of the list of prime numbers of each iteration
        perfect_number = (2**(n-1))*(2**n - 1) #calculates each perfect number
        numbers += [perfect_number] #adds each perfect number of the iteration to the list numbers
    print('The first %d perfect numbers are' %(number) , numbers) #prints out the perfect numbers generated
    
def main(): #the main function
    getPerfectNumbers()
    
if __name__ == '__main__' : #runs the main function
    main()
    

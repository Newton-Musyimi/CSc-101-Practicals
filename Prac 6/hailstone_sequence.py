"""
def sequence_num():
    num = int(input("Enter a positive integer: "))
    while num!=1:
        if num%2==0:
            num= num/2
        elif num%2!=0:
            num=(3*num)+1
        print(int(num),end=",")
sequence_num()
        
"""
def sequence_num():
    numbers=[]
    num = int(input("Enter a positive integer: "))
    while num>1:
        if num%2==0:
            num= num/2
        elif num%2!=0:
            num=(3*num)+1
        numbers.append(num)
    return numbers
def sequence_print(numbers):
    i = len(numbers)
    for i in range(i):
       print(int(numbers[i]),end=",")
def main():
    sequence_print(sequence_num())
main()


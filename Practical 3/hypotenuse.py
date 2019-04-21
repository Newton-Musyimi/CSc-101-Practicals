a=int(input("Enter the length of one side: "))
b=int(input("Enter the length of the other side: "))
def hyp(a,b):
    height=a**2
    base=b**2
    c=(height+base)**0.5
    return c
    
print(hyp(a,b))


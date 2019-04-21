N=int(input("Enter the integer whose factorial you want to find: "))
def fact(N):
    ans = 1
    for i in range(1, N+1):
        ans = ans * i
    return ans

print(fact(N))













        #n=n*(n+1)
        #return n
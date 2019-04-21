def columnAdd():
    num1 = str(input("Num 1: "))
    num2 = str(input("Num 2: "))
    if len(num1)<len(num2):
        len_diff = len(num2) - len(num1)
        num1 = ("0" * len_diff) + num1
    elif len(num1)>len(num2):
        len_diff = len(num1) - len(num2)
        num2 = ("0" * len_diff) + num2
    ans = ""
    carry = 0
    iteration = 0
    for ind in range(len(num1)-1,-1,-1):
        col_sum = int(num1[ind]) + int(num2[ind]) + carry
        if col_sum >= 10:
            carry = col_sum//10
            col_sum = col_sum % 10
        else:
            carry = 0
        ans = str(col_sum)+ans
        if carry>0 and iteration==(len(num1)-1):
            ans = str(carry) + ans
        iteration += 1
    print(ans)
    
def main():
    columnAdd()
    
if __name__ =="__main__":
    main()
    
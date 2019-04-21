def stringSplit(string):
    s = string.split(" ")
    return s

def itemSplit(string):
    s2 = stringSplit(string)
    print(s2)
    new_str = ""
    for i in range(len(s2)):
        item = s2[i]
        if item[0]in "aeiou":
            item = item+"way"
            new_str += (item + " ")
        else:
            while item[0] not in "aeiou":
                item = item[1:]+ item[0]
            item=item+ "ay "
            new_str += (item + " ")
    print(new_str)
            
                
                
def main():
    string = input("Type in a sentence: ")
    itemSplit(string)
    
if __name__ =="__main__":
    main()


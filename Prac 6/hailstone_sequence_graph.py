def sequence_num():
    numbers=[] #this line creates an empty list
    num = int(input("Enter a positive integer: ")) #prompts the user to type in an integer for the program to evaluate
    while num!=1:    #a while statement that
        if num%2==0:
            num= num/2
        elif num%2!=0:
            num=(3*num)+1
        numbers.append(num)
    return numbers
def sequence_graph(numbers):
    iterations = len(numbers)
    urx = (len(numbers)*20)+2
    ury = (max(numbers)*5)+2
    import turtle as t
    wn = t.Screen()
    t.setworldcoordinates(-2,-2,urx,ury)
    graph = t.Turtle()
    graph.speed(10)
    graph.up()
    graph.goto(0,numbers[0]*5)
    graph.down()
    for i in range(1,iterations):
        graph.goto(i*20,(numbers[i])*5)
    wn.exitonclick()
        
def main():
    sequence_graph(sequence_num())
main()

    
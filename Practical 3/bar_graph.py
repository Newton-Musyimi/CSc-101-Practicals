"""This program creates a bar chart with random heights with the width of each bar
and the number of bars specified by the user"""
import turtle #imports the turtle module
import random #imports the random module

number_of_bars = int(input("Enter the number of bars: ")) #prompts the user for the number of bars
width_of_one_bar = int(input("Enter the width of each bar: ")) #prompts the user for the width of each bar 

bars=turtle.Turtle() 
wn=turtle.Screen()
bars.speed(10) #sets the turtle's speed to the maximum speed (JUST FOR FUN)

def barHeight(): #defines a function to generate the height of a bar
    height = int(random.random()*200) #uses the random module to generate a random height for the bar and converts it into an integer type
    return height #returns the value of the height to the call function
def drawBars(): #defines a function that generates the bar graph and draws it using the turtle module
    for i in range(number_of_bars): 
        height=barHeight() #calls the barHeight function to generate a random height for each bar in the iteration
        bars.left(90)
        bars.forward(height)
        bars.right(90)
        bars.forward(width_of_one_bar)
        bars.right(90)
        bars.forward(height)
        bars.left(90)
    bars.left(90)
    bars.left(90)
    bars.forward(width_of_one_bar*number_of_bars)


drawBars() #calls the drawBars function that generates the bar graph
wn.exitonclick() #allows the user to close the turtle graphics window by leftclicking on the window
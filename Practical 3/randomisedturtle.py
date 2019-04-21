import random
import turtle

walk=int(input("Enter the number of times you want your turtle to move forward: "))

wn=turtle.Screen()
gibberish=turtle.Turtle()
gibberish.speed(10)
def gib(walk,gibberish):
    for i in range(walk):
        gibberish.forward(30)
        gibberish.left(random.random()*360)
    
        
gib(walk,gibberish)
wn.exitonclick()
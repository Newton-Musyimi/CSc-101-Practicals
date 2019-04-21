import random
import turtle

wn = tr.Screen() #creates our game board
wn.bgcolor("black")
g = turtle.Turtle()
c = turtle.Turtle()

llx = 0
lly = 0
urx = 200
ury = 100
wn.setworldcoordinates(llx,lly,urx,ury)
number_of_dice = 
rolls = 10000
min_val = number_of_dice
max_val = number_of_dice * 6
for i in range(min_val,max_val+1):
    x = [0] * max_val
    x[ran
    graph.left(90)
    graph.forward(
def drawBar(t,height ):
    """ Get turtle t to draw one bar, of height. """
    t.left(90)
    t.forward(150)
    t.stamp()
    t.backward(150)
    t.right(90)
    t.ht()
    t.begin_fill()               # start filling this shape
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
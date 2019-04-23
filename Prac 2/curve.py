import turtle
import math

wn = turtle.Screen()
c = turtle.Turtle()

c.reset()
turtle.setworldcoordinates(160,-210,550,210)

c.up()
c.goto(180,0)
c.down()
for angle in range(180,540):
    y = math.sin(math.radians(angle))
    c.goto(angle,(y*200))


    
c.up()
c.goto(180,0)
c.down()
c.forward(360)

c.up()
c.goto(360,-201)
c.down()
c.left(90)
c.forward(410)



   
    



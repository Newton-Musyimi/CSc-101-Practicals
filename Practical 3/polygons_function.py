import turtle
sides = int(input("Enter the number of sides of the polygon: "))
size = int(input("Enter the size of each side of the polygon: "))
wn = turtle.Screen()
poly = turtle.Turtle()
def drawShape(sides,size,poly):
    for i in range(sides):
        poly.forward(size)
        poly.left(360/sides)

drawShape(sides,size,poly)
wn.exitonclick()
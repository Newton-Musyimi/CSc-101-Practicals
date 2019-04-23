import turtle

wn = turtle.Screen()
wn.bgcolor("yellow")
sq = turtle.Turtle()

sq.up()
sq.goto(-350,-100)
sq.down()
for i in range (3):
    sq.forward(100)
    sq.left(360/3)

sq.up()
sq.forward(200)
sq.color("red")
sq.down()
for i in range (4):
    sq.forward(100)
    sq.left(360/4)

sq.up()
sq.forward(200)
sq.color("blue")
sq.down()
for i in range (5):
    sq.forward(100)
    sq.left(360/5)

sq.up()
sq.forward(200)
sq.color("white")
sq.down()
for i in range (6):
    sq.forward(100)
    sq.left(360/6)

sq.up()
sq.forward(200)
sq.down()

wn.exitonclick()

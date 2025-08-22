import turtle

screen=turtle.Screen()
screen.bgcolor("Navy")
screen.setup(600, 600)
screen.title("Make a star")

t = turtle.Turtle()
t.pensize(6)
t.shape("arrow")
t.speed(1)
t.color("White")

t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)

t.right(150)
t.penup()
t.forward(100)
t.right(90)

t.pendown()
t.forward(200)
t.right(120)
t.forward(200)
t.right(120)
t.forward(200)


#t.hideturtle()
turtle.done()
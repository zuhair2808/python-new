import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Square on a Canvas")
screen.setup(500, 500)

t = turtle.Turtle()
t.color("White")
t.pensize(8)
t.speed(1)
t.shape("turtle")
t.fillcolor("White")

t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()

t.hideturtle()

turtle.done()
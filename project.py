#Initialize Turtle
import turtle
t = turtle.Turtle()
turtle.colormode(255)
t.speed(10)

#Functions
def infield():
    t.dot(80,"orange")
    t.pensize(17)
    t.color("orange","green")
    t.begin_fill()
    t.left(45)
    t.forward(220)
    t.left(110)
    t.forward(180)
    t.left(55)
    t.forward(180)
    t.left(110)
    t.forward(220)
    t.left(134)
    t.end_fill()
    t.penup()
    t.forward(120)
    t.pendown()
    t.dot(40)

def completion():
    t.right(90)
    t.penup()
    t.forward(100)
    t.left(90)
    t.pendown()
    infield()

def stands():
    t.penup()
    t.setposition(0,-250)
    t.color("grey")
    t.setheading(40)
    t.pendown()
    t.forward(330)
    t.left(45)
    t.forward(200)
    t.left(50)
    for i in range(6):
        t.forward(110)
        t.left(18)
    t.setheading(275)
    t.forward(200)
    t.setheading(321)
    t.forward(345)
    
    
    

#Main
completion()
stands()

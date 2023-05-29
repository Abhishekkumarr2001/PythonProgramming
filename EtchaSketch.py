from turtle import *
import random

tim=Turtle()
screen=Screen()
screen.title("Etch-A-Game")

tim.pensize(2)
colormode(255)
def randomcolor():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color

def forward():
    tim.forward(50)
    tim.color(randomcolor())

def backward():
    tim.backward(50)
    tim.color(randomcolor())

def left():
    tim.left(15)
    tim.color(randomcolor())

def right():
    tim.right(15)
    tim.color(randomcolor())

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
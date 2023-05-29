from turtle import *
import random
import turtle

turtle1=Turtle()

# 1st code
for _ in range(4):
    turtle1.backward(100)
    turtle1.right(90)

# 2nd code
def dashed_square():
    for _ in range(10):
        turtle1.forward(10)
        turtle1.penup()
        turtle1.forward(10)
        turtle1.pendown()

for _ in range(4):
    dashed_square()
    turtle1.right(90)

# 3rd code
def numofsides(sides):
    angle=360/sides
    for _ in range(sides):
        turtle1.forward(100)
        turtle1.right(angle)

for genshape in range(3,10):
    numofsides(genshape)

# 4th code
colour=["midnight blue", "navy", "lime", "crimson", "orange red", "magenta", "dark orange", "dark green"]
direction=[0, 90, 180, 270]
turtle1.pensize(10)
turtle1.speed("fastest")

for _ in range(25):
    turtle1.color(random.choice(colour))
    turtle1.forward(50)
    turtle1.setheading(random.choice(direction))

# 5th code
def drawcircles(gap, rad):
    for _ in range(int(360/gap)):
        turtle1.color(random.choice(colour))
        turtle1.circle(rad)
        turtle1.setheading(turtle1.heading()+gap)

drawcircles(8,140)
drawcircles(6,120)
drawcircles(4,100)

# 6th code
colormode(255)
turtle1.speed("fastest")
turtle1.penup()
turtle1.hideturtle()
turtle1.setheading(225)
turtle1.forward(300)
turtle1.setheading(0)
noofdots=100

def randomcolor():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color

for dot_count in range(1, noofdots+1):
    turtle1.dot(18,randomcolor())
    turtle1.forward(50)
    if dot_count%10==0:
        turtle1.setheading(90)
        turtle1.forward(50)
        turtle1.setheading(180)
        turtle1.forward(500)
        turtle1.setheading(0)

screen=Screen()
screen.exitonclick()

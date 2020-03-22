#!/usr/bin/env python3
import random
import turtle
tim=turtle.Turtle()

colors=['red','blue','black','gold','purple','yellow','orange']
color1=None
color2=None
def assign_colors():
    global color1,color2
    color1=random.choice(colors)
    color2=random.choice(colors)


width1=10
radius=50
assign_colors()
tim.width(width1)
tim.color(color1,color2)
tim.begin_fill()
tim.circle(radius)
tim.end_fill()

side=100
width2=20
assign_colors()
dave=turtle.Turtle()
dave.width(width2)
dave.color(color1,color2)
dave.penup()
dave.setpos(150,0)
dave.pendown()
dave.begin_fill()
for i in range(4):
    dave.forward(side)
    dave.right(90)
dave.end_fill()


width3=40
joe=turtle.Turtle()
joe.width(5)
for i in range(5):
    joe.penup()
    assign_colors()
    joe.color(color1,color2)
    rand2=random.randint(-300,250)
    rand1=random.randint(-300,250)
    joe.setpos(rand1-width3,rand2-width3)
    joe.pendown()
    joe.begin_fill()
    joe.circle(width3)
    joe.end_fill()
turtle.done()

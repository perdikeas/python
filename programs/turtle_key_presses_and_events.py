#!/usr/bin/env python3
import turtle
import random
import time

colors=['red','black','gold','blue']

tim=turtle.Turtle()
tim.speed(0)
tim.shapesize(5,5,5)
tim.width(10)
tim.shape('arrow')
tim.setpos(0,0)

len=30
def up():
    global len
    tim.setheading(90)
    tim.forward(len)

def down():
    global len
    tim.setheading(270)
    tim.forward(len)

def right():
    global len
    tim.setheading(0)
    tim.forward(len)

def left():
    global len
    tim.setheading(180)
    tim.forward(len)

def dragging(x,y):
    global colors
    turtle.ondrag(None)
    color1=random.choice(colors)
    color2=random.choice(colors)
    tim.color(color1,color2)
    tim.setheading(tim.towards(x,y))
    tim.goto(x,y)
    turtle.ondrag(dragging)
def click_left_mouse_button(x,y):
    global colors
    color1=random.choice(colors)
    color2=random.choice(colors)
    tim.color(color1,color2)
    tim.forward(50)
def click_right_mouse_button(x,y):
    tim.stamp()

def click_x_key():
    turtle.clearscreen()

turtle.color('black')
tim.hideturtle()
style=('Courier',10,'bold')
turtle.write("press arrow keys,right and left click and drag the turtle from its starting position",font=style,align='center')
time.sleep(6)
tim.showturtle()
turtle.clearscreen()


turtle.onscreenclick(click_left_mouse_button,1)
turtle.onscreenclick(click_right_mouse_button,3)
turtle.ondrag(dragging)
turtle.onkey(click_x_key,'x')
turtle.onkey(up,'Up')
turtle.onkey(down,'Down')
turtle.onkey(right,'Right')
turtle.onkey(left,'Left')
turtle.listen()
turtle.mainloop()

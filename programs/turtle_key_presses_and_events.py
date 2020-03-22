#!/usr/bin/env python3
import turtle
import random

colors=['red','black','gold','blue']

tim=turtle.Turtle()
tim.speed(5)
tim.width(5)
tim.shape('arrow')
tim.setpos(0,0)

len=100
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

def click_left_mouse_button(x,y):
    color1=random.choice(colors)
    color2=random.choice(colors)
    tim.color(color1,color2)
    tim.forward(5)

def click_right_mouse_button(x,y):
    tim.stamp()

def click_x_key():
    turtle.clearscreen()

turtle.onscreenclick(click_left_mouse_button,1)
turtle.onscreenclick(click_right_mouse_button,3)
turtle.ondrag(click_left_mouse_button,1)
turtle.ondrag(click_right_mouse_button,3)
turtle.onrelease(click_left_mouse_button,1)
turtle.onrelease(click_right_mouse_button,3)

turtle.onkey(click_x_key,'x')
turtle.onkey(up,'Up')
turtle.onkey(down,'Down')
turtle.onkey(right,'Right')
turtle.onkey(left,'Left')
turtle.listen()
turtle.mainloop()

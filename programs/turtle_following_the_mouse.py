#!/usr/bin/env python3
import turtle
import random
from turtle import Screen
screen=turtle.Screen()
screen.bgcolor('red')
tim=turtle.Turtle()
tim.speed(-1)
def dragging(x,y):
    turtle.ondrag(None)
    tim.setheading(tim.towards(x,y))
    tim.goto(x,y)
    turtle.ondrag(dragging)
colors=['red','black','gold','blue']
def tab_key_pressed():
    color1=random.choice(colors)
    tim.color(color1)
    tim.forward(50)
turtle.listen()
turtle.ondrag(dragging)
turtle.onkey(tab_key_pressed,'Tab')
screen.mainloop()

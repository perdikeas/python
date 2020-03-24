#!/usr/bin/env python3

import turtle
import random
import math

class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

#Setting up the Screen
screen=turtle.Screen()
screen.bgcolor('black')
screen.title("Space invaders")


#Setting up the border
border_pen=turtle.Turtle()
border_pen.color('white')
border_pen.penup()
border_pen.speed(0)
x=300
y=270
border_pen.setposition(-x,-y)
border_pen.pendown()
for i in range(4):
    border_pen.forward(x+y)
    border_pen.left(90)
border_pen.hideturtle()

#

def move_left():
    x=player.xcor()
    x-=player_speed
    if x<-290:
        x=-290
    player.setx(x)
def move_right():
    x=player.xcor()
    x+=player_speed
    if x>270:
        x=270
    player.setx(x)
def move_up():
    y=player.ycor()
    y+=player_speed
    if y>280:
        y=280
    player.sety(y)

def move_down():
    y=player.ycor()
    y-=player_speed
    if y<-265:
        y=-265
    player.sety(y)

#Creating the player's spaceship
player=turtle.Turtle()
player.color('blue')
player.shape('triangle')
player.shapesize(1.5,2,1.5)
player.speed(0)
player.penup()
player.setheading(90)
player.setposition(0,-260)
player_speed=15

#Creating the enemy spaceship
enemy=turtle.Turtle()
enemy.color('red')
enemy.shape('circle')
enemy.penup()
enemy.setheading(-90)
enemy.setposition(0,280)
enemy_speed=3


#player missile
missile=turtle.Turtle()
missile.shape('triangle')
missile.color('yellow')
missile.speed(0)
missile.penup()
missile.setheading(-90)
missile.setpos(player.xcor(),player.ycor()+10)
missile_speed=10


def fire_missile():
    global missile,missile_speed
    while missile.ypos()>280:
        missile.forward(missile_speed)

#enemy movement
while True:

    #player input keys binding
    turtle.listen()
    turtle.onkey(move_left,'Left')
    turtle.onkey(move_right,'Right')
    turtle.onkey(move_up,'Up')
    turtle.onkey(move_down,'Down')
    turtle.onkey(fire_missile,'space')


    if enemy.xcor()>260:
        enemy_speed*=-1
        y=enemy.ycor()
        y-=30
        enemy.sety(y)
    elif enemy.xcor()<-280:
        y=enemy.ycor()
        y-=30
        enemy.sety(y)
        enemy_speed*=-1
    if missile.ycor()>280:
        missile.hideturtle()

#!/usr/bin/env python3

import turtle
import random
import math
import time

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

class Alien():
    def __init__(self, speed):
        self.speed = speed
        self.avatar = turtle.Turtle()
        self.avatar.setposition(0, 40)
        self.avatar.color('red')
        self.avatar.setheading(-90)
        self.avatar.penup()
        self.tick = 0

    def live(self):
        self.tick += 1
        if (self.tick % 10 == 1):
            if random.randint(1,2)==1:
                self.avatar.left(random.randint(1, 10))
            else:
                self.avatar.right(random.randint(1, 10))
        self.avatar.forward(self.speed)

aliens = []


tick = 0
while True:
    tick += 1
    if (tick % 30 == 0):
        if (len(aliens)<10):
            aliens.append(Alien(3))
    for alien in aliens:
        alien.live()
    time.sleep(0)

turtle.done()


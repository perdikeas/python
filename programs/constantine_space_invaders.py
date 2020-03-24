#!/usr/bin/env python3
import random
import turtle
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
border_pen.hideturtle()
border_pen.color('green')
for i in range(4):
    border_pen.forward(x+y)
    border_pen.left(90)
    border_pen.color('white')

#defining alien class
class Alien():
    #initialization of alien instance
    def __init__(self,speed):
        self.speed=speed
        self.clone=turtle.Turtle()
        self.clone.setheading(270)
        self.clone.penup()
        self.clone.color('green')
        self.clone.speed(0)
        self.clone.goto(0,270)
        self.clone.shapesize(0.75,1.5,0.75)
        self.clone.shape('triangle')
        self.tick=0

    #method for Alien instances
    def live(self):
        self.tick+=1
        if (self.tick%5==0):
                if (random.randint(1,2)==1):
                    self.clone.left(random.randint(5,10))
                else:
                    self.clone.right(random.randint(5,10))
        self.clone.forward(self.speed)


def border_check_x(a):
    limit=300
    b=a.clone
    if ((b.xcor()>=limit) and (b.heading()>270 or b.heading()<90)):
        b.setheading(230)
    elif((b.xcor()<=-1*limit) and (b.heading()>90 and b.heading()<270)):
        b.setheading(300)

def border_check_y(a):
    limit=270
    global aliens
    b=a.clone
    if ((b.ycor()>=limit) and (b.heading()<180 and b.heading()>0)):
        b.setheading(b.heading()*-1)
    elif (b.ycor()<limit*-1):
        b.hideturtle()
        aliens.remove(a)
tick=0
aliens=[]
while True:
    #thorough border check
    for alien in aliens:
        border_check_x(alien)
        border_check_y(alien)


    tick+=1
    if (tick%40==0):
        if len(aliens)<10:
            aliens.append(Alien(3))
    for alien in aliens:
        alien.live()

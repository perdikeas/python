#!/usr/bin/env python3

import random
import turtle
import math
#global variables
tick=0
aliens=[]
missiles=[]
aliens_escaped=0
kills=0

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


spaceship=turtle.Turtle()
spaceship.speed(0)
spaceship.setheading(90)
spaceship.penup()
spaceship.shapesize(1,0.75,0.75)
spaceship.shape("triangle")
spaceship.color('turquoise')
spaceship.goto(0,-260)
spaceship_speed=10

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

colors=['red','orange','chartreuse','dark green']
#defining missile class
class Missile():
    global spaceship
    def __init__(self,speed):
        self.speed=speed
        self.avatar=turtle.Turtle()
        self.avatar.hideturtle()
        self.avatar.setheading(90)
        self.avatar.penup()
        self.avatar.color('yellow')
        self.avatar.speed(0)
        self.avatar.goto(spaceship.xcor(),spaceship.ycor()+15)
        self.avatar.shapesize(0.5,1.2,0.5)
        self.avatar.shape('triangle')
    def live(self):
        self.avatar.showturtle()
        self.avatar.forward(self.speed)
#defining alien class
class Alien():
    global colors
    #initialization of alien instance
    def __init__(self,speed):
        self.speed=speed
        self.clone=turtle.Turtle()
        self.clone.setheading(270)
        self.clone.penup()
        self.clone.health=4
        self.clone.speed(0)
        self.clone.goto(random.randint(-250,250),270)
        self.clone.shapesize(1.75,1.75,1.75)
        self.clone.shape('circle')
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
        self.clone.color(colors[self.clone.health-1])


#functions
def sqrt(a):
    return math.sqrt(a)
def distance_between(a,b):
    return sqrt( math.pow(a.xcor()-b.xcor(),2)+ math.pow(a.ycor()-b.ycor(),2))

def border_check_x(a):
    limit=265
    b=a.clone
    if ((b.xcor()>=limit) and (b.heading()>270 or b.heading()<90)):
        b.setheading(230)
    elif((b.xcor()<=-1*limit) and (b.heading()>90 and b.heading()<270)):
        b.setheading(300)

def border_check_y(a):
    limit=260
    global aliens,aliens_escaped
    b=a.clone
    if ((b.ycor()>=limit) and (b.heading()<180 and b.heading()>0)):
        b.setheading(b.heading()*-1)
    elif (b.ycor()<limit*-1):
        b.hideturtle()
        aliens.remove(a)
        aliens_escaped+=1


def right():
    global spaceship,spaceship_speed
    x=spaceship.xcor()
    x+=spaceship_speed
    spaceship.setx(x)

def left():
    global spaceship,spaceship_speed
    x=spaceship.xcor()
    x-=spaceship_speed
    spaceship.setx(x)
def add_missile():
    global missiles
    missiles.append(Missile(30))


#main loop
while aliens_escaped<10 and kills<15:
    #counter
    tick+=1

#key binding and user input
    turtle.listen()
    turtle.onkey(left,'Left')
    turtle.onkey(right,'Right')
    turtle.onkey(add_missile,'space')


    #thorough boundaries check for all turtles
    for alien in aliens:
        border_check_x(alien)
        border_check_y(alien)
        if alien.clone.health==0:
            aliens.remove(alien)
            alien.clone.hideturtle()
            kills+=1

    if spaceship.xcor()<-270:
        spaceship.setx(-270)
    elif spaceship.xcor()>265:
        spaceship.setx(265)


    #geneating new aliens
    if (tick%100==0):
        if len(aliens)<10:
            aliens.append(Alien(5))

    #alien movement
    for alien in aliens:
        alien.live()

    #missile movement
    for missile in missiles:
        missile.live()
        if missile.avatar.ycor()>270:
            missiles.remove(missile)
            missile.avatar.hideturtle()
    for missile in missiles:
        for alien in aliens:
            if distance_between(missile.avatar,alien.clone)<20:
                alien.clone.health-=1
                alien.speed-=1
                missiles.remove(missile)
                missile.avatar.hideturtle()

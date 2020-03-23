#!/usr/bin/env python3

import turtle
import time
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


#defining functions
def increase_speed():
    global speed
    speed+=1

def decrease_speed():
    global speed
    while speed>0:
        speed-=0.5
    speed=speed

def left():
    spaceship.left(20)

def right():
    spaceship.right(20)

def sq(x):
    return math.pow(x, 2)

def distance_between(a,b):
    return math.sqrt(sq(b.xcor()-a.xcor()) + sq(b.ycor()-a.ycor()))


def print_help_and_get_difficulty():
    shortCircuit = True
    if (not shortCircuit):
        #getting difficulty level
        screen.bgcolor("white")
        font=('Courier',13,'bold')
        turtle.write('You are somewhere in space when aliens approach your spaceship',font=font,align='center')
        time.sleep(3)
        turtle.clearscreen()

        turtle.write('Use your spaceship  and the arrow keys to touch them and kill them',font=font,align='center')
        time.sleep(2)
        turtle.clearscreen()

        turtle.write('You need 10 kills to win if you choose the normal difficulty level',font=font,align='center')
        time.sleep(2)
        turtle.clearscreen()

        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(Color.RED+Color.BOLD+'What difficulty level do you want 1 or 2 (2 is the hardest)'+Color.END)
        screen.bgcolor("black")
        return int(input())
    else:
        return 1



def difficultyLevelToGameConfiguration(difficulty):
    return {
    'alien_number':5 + (difficulty*5)
    , 'player_health':10 - difficulty
    , 'necessary_kills':10 + (difficulty*5)
    , 'alien_speed':2
    };



#generating alien
def generate_aliens(n):
    aliens=[]
    for i in range(n):
        alien=turtle.Turtle()
        alien.penup()
        alien.shape('circle')
        alien.color('red')
        alien.shapesize(2,2,2)
        rand1=random.randint(-300,300)
        rand2=random.randint(-270,270)
        while (rand1 <-20 or rand1>20) and (rand2<-20 or rand2>20):
            rand1=random.randint(-300,300)
            rand2=random.randint(-270,270)
        alien.setpos(rand1,rand2)
        alien.speed(0)
        aliens.append(alien)
    return aliens

def createSpaceship():
    spaceship=turtle.Turtle()
    spaceship.color('blue')
    spaceship.shape('triangle')
    spaceship.speed(0)   #animation speed not to be confused with the constant speed I define later on#setting spaceship speed
    spaceship.penup()
    return spaceship

def setKeyBindingsForUserInput():
    #Setting key bindings
    turtle.listen()
    turtle.onkey(increase_speed,'Up')
    turtle.onkey(decrease_speed,'Down')
    turtle.onkey(left,'Left')
    turtle.onkey(right,'Right')

def drawBoundary():
    tim=turtle.Turtle()
    tim.shape('arrow')
    tim.color('white')
    tim.penup()
    tim.setpos(-300,-270)
    tim.pendown()
    tim.goto(300,-270)
    tim.goto(300,270)
    tim.goto(-300,270)
    tim.goto(-300,-270)
    tim.hideturtle()


def remove_alien(alien):
    global kills
    global aliens
    kills+=1
    alien.hideturtle()
    aliens.remove(alien)

# live code below:

gameConfiguration = difficultyLevelToGameConfiguration(print_help_and_get_difficulty())

#Setting up the Screen
screen=turtle.Screen()
screen.bgcolor("black")

#setting spaceship speed
speed=1
kills=0
aliens=generate_aliens(gameConfiguration['alien_number'])
spaceship = createSpaceship()
setKeyBindingsForUserInput()

drawBoundary()

#main game loop
while kills!=gameConfiguration['necessary_kills']:
    global spaceship
    global aliens
    spaceship.forward(speed)
    for alien in aliens:
        alien.forward(gameConfiguration['alien_speed'])
        if (distance_between(spaceship,alien)<10):
            print('xx')
            remove_alien(alien)

    #Boundary check
    if spaceship.xcor()>300 or spaceship.xcor()<-300:
        spaceship.right(180)
    elif spaceship.ycor()>270 or spaceship.ycor()<-270:
        spaceship.right(180)
    for alien in aliens:
        if alien.xcor()>300 or alien.xcor()<-300:
            alien.left(180)
        elif alien.ycor()>270 or alien.ycor()<-270:
            alien.left(180)
    time.sleep(0)































turtle.done()

#!/usr/bin/env python3

import random
import pygame

pygame.init()

#global variables
game_running=True
Screenwidth=500
Screenheight=480
bullets=[]
counter=0
enemies=[]


#enemy sprite images

#enemy right images
enemy_walk_right_files=['./images/R{}E.png'.format(i) for i in range(1,12)]
#enemy left images
enemy_walk_left_files=['./images/L{}E.png'.format(i) for i in range(1,12)]


enemy_walk_right=[pygame.image.load(fname) for fname in enemy_walk_right_files]



enemy_walk_left=[pygame.image.load(fname) for fname in enemy_walk_left_files]

#player sprite images

#walking right sprites
walkRightImagesFiles = ['./images/R{}.png'.format(i) for i in range(1, 10)]
walkRight = [pygame.image.load(fname) for fname in walkRightImagesFiles]

#walking left sprites
walkLeftImagesFiles=['./images/L{}.png'.format(i) for i in range(1,10)]
walkLeft=[pygame.image.load(fname) for fname in walkLeftImagesFiles]

#setting up the screen with the same size as the background picture
win=pygame.display.set_mode((Screenwidth,Screenheight))

#other images
bg = pygame.image.load('./images/bg.jpg')
char = pygame.image.load('./images/standing.png')

# setting up a clock in order to set our fps later in the game
clock=pygame.time.Clock()

#classes and functions

#enemy class
class Enemy():
    #sprite enemy images
    enemy_walk_right=[pygame.image.load(fname) for fname in enemy_walk_right_files]
    enemy_walk_left=[pygame.image.load(fname) for fname in enemy_walk_left_files]

    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.walk_count=0
        self.vel=3


    def live(self,win):

        if self.walk_count+1 >= 33:
            self.walk_count=0

        self.move(win)

        if self.vel>0:
            win.blit(self.enemy_walk_right[self.walk_count//3],(self.x,self.y))
            self.walk_count+=1
        else:
            win.blit(self.enemy_walk_left[self.walk_count//3],(self.x,self.y))
            self.walk_count+=1


        pygame.display.update()

    def move(self,win):

        if self.vel>0:
            self.x+=self.vel

            if self.x+self.vel+self.width>Screenwidth:
                self.vel*=-1
                self.walk_count=0


        else:
            self.x+=self.vel

            if self.x<self.vel:
                self.vel*=-1





#player class
class Player():
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.velocity=5
        self.is_jump=False
        self.jump_count=10
        self.left=False
        self.right=False
        self.walk_count=0
        self.standing=True
    def draw(self):
        if  not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walk_count//3],(self.x,self.y))
                self.walk_count+=1
            elif self.right:
                win.blit(walkRight[self.walk_count//3],(self.x,self.y))
                self.walk_count+=1
        else:
            if self.right:
                win.blit(walkRight[0],(self.x,self.y))
                self.walk_count+=1
            else:
                win.blit(walkLeft[0],(self.x,self.y))
                self.walk_count+=1

        if self.walk_count+1>=27:
            self.walk_count=0

        pygame.display.update()

#creating projectile/bullet class
class Projectile():
    def __init__(self,x,y,radius,color,facing):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.facing=facing
        self.vel=15*facing
    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)



#creating an instance of the player class
man=Player(50,400,64,64)


def redraw_window():
    win.blit(bg,(0,0))
    man.draw()
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


#we begin by adding only one opponent
enemies.append(Enemy(400,400,64,64))

while game_running:
    #30 fps
    clock.tick(30)

    redraw_window()


    counter+=1

    if (counter%200==0) and len(enemies)<2:
        enemies.append(Enemy(random.randint(50,350),400,64,64))


    #enemy movement
    for enemy in enemies:
        enemy.live(win)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_running=False

    #bullet movement
    for bullet in bullets:
        if bullet.x<Screenwidth-bullet.vel and bullet.x>bullet.vel:
            bullet.x+=bullet.vel
        else:
            bullets.remove(bullet)

    #list of pressed keys
    keys=pygame.key.get_pressed()


    #binding user input
    if keys[pygame.K_SPACE]:
        if man.left:
            facing=-1
        else:
            facing=1
        if len(bullets)<5:
            bullets.append(Projectile(round(man.x+man.width//2),round(man.y+man.height//2),6,(255,0,0),facing))




    if keys[pygame.K_LEFT]:
        man.left=True
        man.right=False
        man.standing=False
        if man.x>man.velocity:
            man.x-=man.velocity

    elif keys[pygame.K_RIGHT]:
        man.standing=False
        man.right=True
        man.left=False
        if man.x<Screenwidth-man.width-man.velocity:
            man.x+=man.velocity
    else:
        man.walk_count=0
        man.standing=True


    if not man.is_jump:

        if keys[pygame.K_UP]:
            if man.right:
                man.right=True
                man.left=False
            else:
                man.right=False
                man.left=True
            man.is_jump=True
            man.standing=False

    else:

        if man.jump_count>=-10:
            neg=1
            if man.jump_count<0:
                neg=-1
            man.y-= (man.jump_count**2)*0.4*neg
            man.jump_count-=1
        else:
            man.standing=True
            man.is_jump=False
            man.jump_count=10


    win.blit(bg,(0,0))
pygame.quit()

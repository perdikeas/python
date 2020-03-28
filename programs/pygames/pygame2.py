#!/usr/bin/env python3



import random
import pygame
import math
import time



pygame.init()



#global variables

bullet_speed = 12
enemies_speed = 3

game_running=True
Screenwidth=500
Screenheight=480
bullets=[]
counter=0
enemies=[]



#rgb values


#darkgreen
color1=(0,128,0)

#orange
color2=(255,165,0)

#darkred
color3=(128,0,0)



#font for writing
font=pygame.font.SysFont('comicsans',30,True,True)

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

#setting up the bullet and background sound effect

music=pygame.mixer.music.load('./images/music.mp3')
pygame.mixer.music.play(-1)
bullet_sound=pygame.mixer.Sound('./images/shotgun.ogg')




def player_health_checking(player):
    global enemies,game_running,win,font

    necessary_kills=5


    if player.kills<necessary_kills:

        pygame.draw.rect(win,(255,255,255),(player.x+11,player.y-20,50,10))

        if player.health<=player.starting_health and player.health>=player.starting_health-5:
            pygame.draw.rect(win,color1,(player.x+11,player.y-20,50-round(2.5*(20-player.health)),10))

        elif player.health<player.starting_health-5 and player.health>=player.starting_health-15:
            pygame.draw.rect(win,color2,(player.x+11,player.y-20,50-round(2.5*(20-player.health)),10))

        elif player.health<player.starting_health-15 and player.health>0:
            pygame.draw.rect(win,color3,(player.x+11,player.y-20,50-round(2.5*(20-player.health)),10))

        else:
            player.visible=False

            game_running=False

            for enemy in enemies:
                enemy.visible=False

            win.fill((255,255,255))
            text3=font.render('The goblins killed you',1,(0,0,0))

            win.blit(text3,(150,250))

            pygame.display.update()

            time.sleep(4)

            pygame.quit()

    else:
        player.visible=False
        game_running=False

        for enemy in enemies:
            enemy.visible=False

        win.fill((255,255,255))

        text4=font.render('You slayed {} goblins'.format(necessary_kills),1,(0,0,0))

        win.blit(text4,(150,250))

        pygame.display.update()

        time.sleep(4)

        pygame.quit()




#enemy class
class Enemy():
    #sprite enemy images
    enemy_walk_right=[pygame.image.load(fname) for fname in enemy_walk_right_files]
    enemy_walk_left=[pygame.image.load(fname) for fname in enemy_walk_left_files]

    def __init__(self,x,y,width,height,facing):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.walk_count=0
        self.vel=enemies_speed
        self.health=20
        self.starting_health=20
        self.visible=True
        self.hitbox=(self.x+17,self.y+2,31,57)
        self.facing=1

    def live(self,win):
        global enemies,man
        pygame.draw.rect(win,(255,255,255),(self.x+11,self.y-20,50,10))
        if self.health<=20 and self.health>15:
            pygame.draw.rect(win,color1,(self.x+11,self.y-20,50-round(2.5*(20-self.health)),10))
        elif self.health<=15 and self.health>5:
            pygame.draw.rect(win,color2,(self.x+11,self.y-20,50-round(2.5*(20-self.health)),10))
        elif self.health<=5 and self.health>0:
            pygame.draw.rect(win,color3,(self.x+11,self.y-20,50-round(2.5*(20-self.health)),10))
        else:
            man.kills+=1
            self.visible=False
            enemies.remove(self)


        if self.walk_count+1 >= 33:
            self.walk_count=0

        self.move(win)

        if self.facing>0:
            win.blit(self.enemy_walk_right[self.walk_count//3],(self.x,self.y))
            self.walk_count+=1
        else:
            win.blit(self.enemy_walk_left[self.walk_count//3],(self.x,self.y))
            self.walk_count+=1

        self.hitbox=(self.x+17,self.y+2,31,57)

        pygame.display.update()


    def move(self,win):


        self.x+=self.vel*self.facing

        if self.x+self.vel*self.facing+self.width>Screenwidth:
            self.facing*=-1
            self.walk_count=0

        if self.x<self.vel:
            self.facing*=-1

    def is_touching_bullet(self):
        self.health-=2


#player class
class Player():
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=4
        self.is_jump=False
        self.jump_count=10
        self.left=False
        self.right=False
        self.walk_count=0
        self.standing=True
        self.health=20
        self.starting_health=20
        self.visible=True
        self.kills=0
        self.hitbox=(self.x+17,self.y+11,29,52)


    def draw(self):
        if self.visible:

            if not(self.standing):
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
            self.hitbox=(self.x+17,self.y+11,29,52)


    def hit(self):
        self.health-=0.2


    pygame.display.update()

#creating projectile/bullet class

class Projectile():
    def __init__(self,x,y,radius,color,facing):
        global bullet_speed
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.facing=facing
        self.vel=bullet_speed*facing


    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)



#creating an instance of the player class
man=Player(50,400,64,64)


def redraw_window():

    win.blit(bg,(0,0))

    man.draw()
    text1=font.render('Man health: {}'.format(man.health),1,(0,0,0))
    text2=font.render('Man now has {} kills'.format(man.kills),1,(0,0,0))

    win.blit(text1,(300,50))
    win.blit(text2,(40,50))

    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()




#we begin by adding only one opponent
enemies.append(Enemy(400,400,64,64,random.choice([-1,1])))


while game_running:


    #30 fps
    clock.tick(30)


    #drawing functions
    redraw_window()



    player_health_checking(man)



    counter+=1

    #always have enemies on the screen
    if  len(enemies)<1:
        enemies.append(Enemy(random.randint(20,400),400,64,64,random.choice([-1,1])))



    #enemy movement
    for enemy in enemies:
        enemy.live(win)
        if man.hitbox[1]<enemy.hitbox[1]+enemy.hitbox[3] and man.hitbox[1]+ man.hitbox[3]>enemy.hitbox[1]:
            if man.hitbox[0]<enemy.hitbox[0]+enemy.hitbox[2] and man.hitbox[0] + man.hitbox[2]>enemy.hitbox[0]:
                man.hit()


    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            game_running=False


    #bullet movement
    for bullet in bullets:
        for enemy in enemies:
            if bullet.y-bullet.radius>=enemy.hitbox[1] and bullet.y+bullet.radius<enemy.hitbox[1]+enemy.hitbox[3]:
                if bullet.x+bullet.radius>=enemy.hitbox[0] and bullet.x-bullet.radius<enemy.hitbox[0]+enemy.hitbox[2]:
                    bullets.remove(bullet)
                    enemy.is_touching_bullet()



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
        if len(bullets)<1:
            bullets.append(Projectile(round(man.x+man.width//2),round(man.y+man.height//2),6,(0,0,0),facing))
            



    if keys[pygame.K_LEFT]:
        man.left=True
        man.right=False
        man.standing=False
        if man.x>man.vel:
            man.x-=man.vel

    elif keys[pygame.K_RIGHT]:
        man.standing=False
        man.right=True
        man.left=False
        if man.x<Screenwidth-man.width-man.vel:
            man.x+=man.vel
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

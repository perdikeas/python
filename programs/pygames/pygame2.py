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


def sq(x):
    return math.pow(x, 2)

class Point():
    def __init__(self, x, y):
        self.x=x
        self.y=y

def distance_between(p1, p2):
    return math.sqrt(sq(p1.x-p2.x)+sq(p1.y-p2.y))

def diagonal_of_being(being):
    return math.sqrt(sq(being.width)+sq(being.height))

def collision_between_sprites(man, enemy):
    center_of_man = Point(man.x+man.width/2, man.y+man.height/2)
    center_of_enemy = Point(enemy.x+enemy.width/2, man.y+enemy.height/2)
    d = distance_between(center_of_man, center_of_enemy)
    return d<=diagonal_of_being(man)/6+diagonal_of_being(enemy)/6+(man.vel+enemy.vel)*0.1

def bullet_hits_target(bullet, enemy):
    center_of_enemy = Point(enemy.x+enemy.width/2, man.y+enemy.height/2)
    d = distance_between(bullet, center_of_enemy)
    return d<=diagonal_of_being(enemy)/4+(bullet.vel+enemy.vel)*0.2





def player_health_checking(player):
    global enemies,game_running,win,font

    necessary_kills=1


    if player.kills<necessary_kills:
        if player.health<=player.starting_health and player.health>=player.starting_health-5:
            pygame.draw.rect(win,color1,(player.x,player.y-20,55+player.health-player.starting_health,10))
        elif player.health<player.starting_health-5 and player.health>=player.starting_health-15:
            pygame.draw.rect(win,color2,(player.x,player.y-20,55+player.health-player.starting_health,10))
        elif player.health<player.starting_health-15 and player.health>0:
            pygame.draw.rect(win,color3,(player.x,player.y-20,55+player.health-player.starting_health,10))
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

        text4=font.render('You slayed 10 goblins',1,(0,0,0))

        win.blit(text4,(150,250))

        pygame.display.update()
        time.sleep(4)
        pygame.quit()




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
        self.vel=enemies_speed
        self.health=20
        self.starting_health=20
        self.visible=True
    def live(self,win):
        global enemies,man

        if self.health<=20 and self.health>15:
            pygame.draw.rect(win,color1,(self.x,self.y-20,55+self.health-self.starting_health,10))
        elif self.health<=15 and self.health>5:
            pygame.draw.rect(win,color2,(self.x,self.y-20,55+self.health-self.starting_health,10))
        elif self.health<=5 and self.health>0:
            pygame.draw.rect(win,color3,(self.x,self.y-20,55+self.health-self.starting_health,10))
        else:
            man.kills+=1
            self.visible=False
            enemies.remove(self)


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
enemies.append(Enemy(400,400,64,64))


while game_running:


    #30 fps
    clock.tick(30)


    #drawing functions
    redraw_window()

    player_health_checking(man)
    #adding new enemies if there are none on the screen
    counter+=1

    #always have enemies on the screen
    if  len(enemies)<1:
        enemies.append(Enemy(random.randint(50,400),400,64,64))


    #enemy movement
    for enemy in enemies:
        enemy.live(win)
        if collision_between_sprites(man, enemy):
            man.health-=0.2

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            game_running=False


    #bullet movement
    for bullet in bullets:
        if bullet.x<Screenwidth-bullet.vel and bullet.x>bullet.vel:
            bullet.x+=bullet.vel
        else:
            bullets.remove(bullet)
        for enemy in enemies:
            d = distance_between(bullet,enemy)
#            if d<d_min:
 #               d_min = d
  #              print('minimum distance so far is: {}'.format(d_min))
#            if d <  ((abs(bullet.vel)+abs(enemy.vel))/2 + 32)*1.1:
            if bullet_hits_target(bullet, enemy):
                bullets.remove(bullet)
                enemy.health-=1




    #list of pressed keys
    keys=pygame.key.get_pressed()


    #binding user input
    if keys[pygame.K_SPACE]:
        if man.left:
            facing=-1
        else:
            facing=1
        if len(bullets)<3:
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

#!/usr/bin/env python3
import pygame
pygame.init()

Screenwidth=700
Screenheight=700
x=20
y=600
width=50
height=50
velocity=7

window=pygame.display.set_mode((Screenwidth,Screenheight))

pygame.display.set_caption("First game")

is_jumping=False
jump_count=10

run=True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.draw.rect(window,(255,0,0),(x,y,width,height))
    pygame.display.update()

    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if x>velocity:
            x-=velocity
    if keys[pygame.K_RIGHT]:
        if x<Screenwidth-width-velocity:
            x+=velocity
    if not is_jumping:
        if keys[pygame.K_UP]:
            if y>velocity:
                y-=velocity
        if keys[pygame.K_DOWN]:
            if y<Screenheight-height-velocity:
                y+=velocity
        if keys[pygame.K_SPACE]:
            is_jumping=True

    else:
        if jump_count>=-10:
            neg=1
            if jump_count<0:
                neg=-1
            y-= (jump_count**2)*0.5*neg
            jump_count-=1
        else:
            is_jumping=False
            jump_count=10

    window.fill((0,0,0))
pygame.quit()

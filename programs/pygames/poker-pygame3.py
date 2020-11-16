#!/usr/bin/env python3.7

import pygame

pygame.init()

#setting up the screen width and screen height
Screenwidth=400
Screenheight=350

#loading the background
bg=pygame.image.load("casino_bg.jpg")

#setting up pygame window
win=pygame.display.set_mode((Screenwidth,Screenheight))

#inserting background
win.blit(bg,(0,0))
pygame.display.update()

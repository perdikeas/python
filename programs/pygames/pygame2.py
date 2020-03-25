#!/usr/bin/env python3

import random
import pygame

pygame.init()

wn=pygame.display.set_mode((500,500))
pygame.display.set_caption("Second game")

walkRightImagesFiles = ['./images/R{}.png'.format(i) for i in range(1, 10)]
walkRight = [pygame.image.load(fname) for fname in walkRightImagesFiles]

if False:
    walkRight = [pygame.image.load('R1.png')
    , pygame.image.load('R2.png')
    , pygame.image.load('R3.png')
    , pygame.image.load('R4.png')
    , pygame.image.load('R5.png')
    , pygame.image.load('R6.png')
    , pygame.image.load('R7.png')
    , pygame.image.load('R8.png')
    , pygame.image.load('R9.png')]

#walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
#bg = pygame.image.load('bg.jpg')
#char = pygame.image.load('standing.png')

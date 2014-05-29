from __future__ import print_function
import pygame, sys, random, time
from pygame.locals import *

pygame.init()
pygame.event.set_blocked(VIDEORESIZE)   #Non-resizable window
window = pygame.display.set_mode((185,185))   #Window size
bg = pygame.Surface(window.get_size())
bg.fill((138,138,138))
height = 40
width = 40
margin = 5

numnames = [2,4,8,16,32,64,128,256,512,1024,2048]
numblocks = []

for x in numnames:
    numname = "data/images/%i.jpg"%x
    numblocks.append(numname)

block_images = []

for x in numblocks:
    blockimg = pygame.image.load(x).convert()
    block_images.append(blockimg)

axislocs = [[5,5],[50,5],[95,5],[140,5],
            [5,50],[50,50],[95,50],[140,50],
            [5,95],[50,95],[95,95],[140,95],
            [5,140],[50,140],[95,140],[140,140]]
def gen_loc():#Generates a random location
    randloc = random.randint(0,16)
    return(randloc)

def initial(): #Generates first two blocks
    gen_loc(rloc)
    pointx = axislocs[rloc][0]
    pointy = axislocs[rloc][1]
    randnum = random.randit(1,10)

    if randnum == 10:
        initimg = block_images[1]
    else:
        initimg = block_images[0]

    window.blit(initimg , (pointx,pointy))

while True:
        
    window.blit(bg, (0,0))
    
    for row in range(4):
        for column in range(4):
            pygame.draw.rect(window,(198,198,198),[(margin+width)*column+margin,(margin+height)*row+margin,width,height])
            
    initial()
    
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

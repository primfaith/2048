#TETRIS ALPHA
#CHRISTIAN JENSEN & Robert Pallante
#CHANGELOG IN FOLDER
from __future__ import print_function
import pygame, sys, random, time
from pygame.locals import *
#=================================
pygame.font.init
pygame.init()
pygame.event.set_blocked(VIDEORESIZE)   #Non-resizable window
window = pygame.display.set_mode((550, 600))   #Window size
pygame.display.set_caption('2048')
#=========Gobal Varis==============
ver = 0.01
score = 0
finalscore = 0
time = 0
clockspeed = 20
direction = None
scoretextfont=pygame.font.Font(None,36)
losetextfont=pygame.font.Font(None,72)
#==============music===============
pygame.mixer.music.load('theme.ogg')
pygame.mixer.music.play()
#==============Functions============
#Verison output
def verison():
    print (ver, "Made by covxx & primitive")
#Score write system
def scoring():
    with open ("score.txt", "a") as es: #opens score keeping
        print ("==================")
        print ("==================")
        n4s = raw_input("Whats your name?: ")
        print(score,n4s,  file = es) #prints score to file
def play():
    ##scoring()
    print ("hey this works")
#======================== MENU ========================
def menu():
    while True:
        pygame.mouse.set_visible(True)
        window.fill((204,204,204))
        losetextfont.set_underline(True)
        losetextfont.set_bold(True)
        title=losetextfont.render('2048',1,(0,0,0))
        titlepos = title.get_rect(center=(300,200))
        window.blit(title,titlepos)
        losetextfont.set_underline(False)
        losetextfont.set_bold(False)
        playbutton=losetextfont.render('PLAY',1,(255,255,255),(0,102,153))
        playbuttonpos=playbutton.get_rect(center=(300,350))
        window.blit(playbutton,playbuttonpos)
        pygame.draw.rect(window,(0,0,0),playbuttonpos,3)
        pygame.draw.rect(window,(0,0,0),playbuttonpos,3)
        version=scoretextfont.render('Version: Alpha ', 1, (0,0,0))
        versionpos=version.get_rect(left=0, bottom=600)
        window.blit(version,versionpos)
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP and event.button == 1:
                if playbuttonpos.collidepoint(event.pos):
                    return None
                elif inspos.collidepoint(event.pos):
                    instructions()
#======================== MENU END===================
verison()
menu()
play()




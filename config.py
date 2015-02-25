__author__ = 'Administrator'
import pygame
import random
import sys
import eztext
import pygame.mixer
pygame.mixer.init()
pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
running = 1
black = (0, 0, 0)
white = (255, 255, 255)
pygame.mixer.music.load("music.wav")
jump_sound = pygame.mixer.Sound("jump.wav")
image1 = pygame.image.load('running1.PNG').convert_alpha()
image2 = pygame.image.load("running2.PNG").convert_alpha()
image3 = pygame.image.load("running3.PNG").convert_alpha()
image4 = pygame.image.load("running4.PNG").convert_alpha()
image5 = pygame.image.load("running5.PNG").convert_alpha()
image6 = pygame.image.load("running6.PNG").convert_alpha()
image7 = pygame.image.load("running7.PNG").convert_alpha()
image8 = pygame.image.load("running8.PNG").convert_alpha()
image9 = pygame.image.load("running9.PNG").convert_alpha()
image10 = pygame.image.load("running10.PNG").convert_alpha()
image11 = pygame.image.load("running11.PNG").convert_alpha()
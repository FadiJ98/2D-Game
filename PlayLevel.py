import pygame
import os
import sys
import Tiny_Dude_Hero
import LevelNode
import main

#Pygame.init
pygame.init()
#This is our main loop where we will do EVERYTHING related to actually playing the game.
screen = main.screen

#This implementation should be changed depending on settings.
running = True

#Main Function
def GameLoop(Map): 
    #Main Loop
    while running:
        screen.fill(0,0,0) #Fill the screen with black.

        #Properly draw the Map using a 2d array of TerrainSprites given by LevelNode upon running LevelNode.StartLevel
        for i in range(len(Map)):
            for j in range(len(Map[i])):
                Map[i][j].Draw()





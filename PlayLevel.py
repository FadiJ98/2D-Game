import pygame
import os
import sys
import Tiny_Dude_Hero
from TerrainSprite import TerrainSprite

#Pygame.init
pygame.init()

#This implementation should be changed depending on settings.
running = True

Background = pygame.image.load(os.path.join(r"2D Game Images\Level_Tiles_Sets\Level_1","TileSet3SC.png"))
clock = pygame.time.Clock()
#Main Function
def GameLoop(Map,screen): 
    #Main Loop
    flagFrame = 0 #A counter which increments by 1 every loop to go through the different animation frames of the flag.
    while running:
        delta_time = clock.tick(60) / 1000
        screen.blit(Background,(0,0)) #Fill the screen with background image.

        #Properly draw the Map using a 2d array of TerrainSprites given by LevelNode upon running LevelNode.StartLevel
        for i in range(len(Map)):
            for j in range(len(Map[i])):
                #If statement to detect if the item being drawn is the end flag.
                if Map[i][j].type == 99:
                    Map[i][j].Draw(flagFrame,screen)
                    flagFrame+=1
                    continue
                Map[i][j].Draw(screen)

        #If the current frame of the flag's animation is the eighth (which would be out of bounds) reset it to the first frame.
        if flagFrame >= 8:
            flagFrame = 0
        pygame.display.update()
                


import pygame
import os
import sys
import Tiny_Dude_Hero
from TerrainSprite import TerrainSprite

#Pygame.init
pygame.init()

#This implementation should be changed depending on settings.
running = True

Background = pygame.image.load(os.path.join(r"C:\Users\sacor\source\repos\FadiJ98\2D-Game\2D Game Images\Level_Tiles_Sets\Level_1","TileSet3SC.png"))
#Background.load(os.path.join(r"C:\Users\sacor\source\repos\FadiJ98\2D-Game\2D Game Images\Level_Tiles_Sets\Level_1","Tile Set 3.png"))
#Main Function
def GameLoop(Map,screen): 
    #Main Loop
    while running:
        screen.blit(Background,(0,0)) #Fill the screen with background image.

        #Properly draw the Map using a 2d array of TerrainSprites given by LevelNode upon running LevelNode.StartLevel
        for i in range(len(Map)):
            for j in range(len(Map[i])):
                Map[i][j].Draw(screen)

        pygame.display.update()
                


import pygame
import sys
import os

#Initialize some basic colors for testing purposes.
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

#Terrain implementation using sprites.
class TerrainSprite(pygame.sprite.Sprite):

    def __init__(self,type,x,y):
        self.type = type #Determines the image and rect of this sprite.
        self.isActive = False #Determines the state of the sprite, for instance, an active door sprite is open, while an inactive door sprite is closed.awd
        self.Color = (0,0,0) #Contains the color of the block for testing purposes.
        self.Coords = (0,0)
        width = 16
        height = 16

        #Initialize Sprite Constructor.
        pygame.sprite.Sprite.__init__(self)
        

        match self.type:
            case 0:
                #print("Case 0")
                self.image = pygame.Surface([width,height])
                self.image.fill(WHITE)
                self.rect = self.image.get_rect() #Defines the Sprites Rect based on the image size (in this case the surface size)
                self.rect.x = x #Set's the Sprite's Rect X position Which should also change where the surface and sprite are.
                self.rect.y = y #Same as above but for Y position.
                self.Coords = (x,y)
            case 1:
                #print("Case 1")
                self.image = pygame.Surface([width,height])
                self.image.fill(RED)
                self.Color = RED
                self.rect = self.image.get_rect() #Defines the Sprites Rect based on the image size (in this case the surface size)
                self.rect.x = x #Set's the Sprite's Rect X position Which should also change where the surface and sprite are.
                self.rect.y = y #Same as above but for Y position.
                self.Coords = (x,y)
            case 2: 
                pass #Write some code for damaging the player as this is a damaging block.
            case 3:
                pass #Write some code for a platform which can be passed through from the bottom but not fall through from the top.
            case 98: 
                pass #This section will stay like this as terrain type 98 is the player spawn point, which will have no collision cause it's just where the player starts.
            case 99:
                if self.isActive == True:
                    pass #Write some code for the end goal
    def Draw(self,screen):
        #A quick method which draws the given sprite onto the screen.
        screen.blit(self.image,self.Coords)
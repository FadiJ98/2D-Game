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
        #self.Color = (0,0,0) #Contains the color of the block for testing purposes.
        self.Coords = (x,(1016-y)) #y starts at 1016 = bottom left corner - 64, because images are generated down and right.
        width = 64
        height = 64

        #Initialize Sprite Constructor.
        pygame.sprite.Sprite.__init__(self)

        match self.type:
            case 0:
                #This will literally be air. So we don't need to worry about it.
                self.image = None
                self.rect = (0,0,0,0)
                pass
            case 1:
                #For Grass Block Center
                self.image = pygame.image.load(os.path.join(r"2D Game Images\Level_Tiles_Sets\Level_1\Individual Tiles","Tile1.png"))
                self.rect = self.image.get_rect() #Defines the Sprites Rect based on the image size (in this case the surface size)
                self.rect.x = x #Set's the Sprite's Rect X position Which should also change where the surface and sprite are.
                self.rect.y = y #Same as above but for Y position.
            case 1.1:
                #For Grass Block left
                self.image = pygame.image.load(os.path.join(r"2D Game Images\Level_Tiles_Sets\Level_1\Individual Tiles","Tile3.png"))
                self.rect = self.image.get_rect() #Defines the Sprites Rect based on the image size (in this case the surface size)
                self.rect.x = x #Set's the Sprite's Rect X position Which should also change where the surface and sprite are.
                self.rect.y = y #Same as above but for Y position.
            case 1.2:
                #For Grass Block right
                self.image = pygame.image.load(os.path.join(r"2D Game Images\Level_Tiles_Sets\Level_1\Individual Tiles","Tile4.png"))
                self.rect = self.image.get_rect() #Defines the Sprites Rect based on the image size (in this case the surface size)
                self.rect.x = x #Set's the Sprite's Rect X position Which should also change where the surface and sprite are.
                self.rect.y = y #Same as above but for Y position.
            case 2: 
                #For Dirt Block Center
                self.image = pygame.image.load(os.path.join(r"2D Game Images\Level_Tiles_Sets\Level_1\Individual Tiles","Tile2.png"))
                self.rect = self.image.get_rect() #Defines the Sprites Rect based on the image size (in this case the surface size)
                self.rect.x = x #Set's the Sprite's Rect X position Which should also change where the surface and sprite are.
                self.rect.y = y #Same as above but for Y position.
            case 2.1: 
                #For Dirt Block Left
                self.image = pygame.image.load(os.path.join(r"2D Game Images\Level_Tiles_Sets\Level_1\Individual Tiles","Tile5.png"))
                self.rect = self.image.get_rect() #Defines the Sprites Rect based on the image size (in this case the surface size)
                self.rect.x = x #Set's the Sprite's Rect X position Which should also change where the surface and sprite are.
                self.rect.y = y #Same as above but for Y position.
            case 2.2: 
                #For Dirt Block Right
                self.image = pygame.image.load(os.path.join(r"2D Game Images\Level_Tiles_Sets\Level_1\Individual Tiles","Tile6.png"))
                self.rect = self.image.get_rect() #Defines the Sprites Rect based on the image size (in this case the surface size)
                self.rect.x = x #Set's the Sprite's Rect X position Which should also change where the surface and sprite are.
                self.rect.y = y #Same as above but for Y position.
            case 3:
                pass #Write some code for a platform which can be passed through from the bottom but not fall through from the top.
            case 98: 
                pass
            case 99:
                if self.isActive == True:
                    pass #Write some code for the end goal
    def Draw(self,screen):
        #A quick method which draws the given sprite onto the screen.
        if self.image == None:
            return
        else:
            screen.blit(self.image,self.Coords)
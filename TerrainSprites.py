import pygame
import sys
import os

#Terrain implementation using sprites.
class TerrainSprites(pygame.sprite.Sprite):

    def __init__(self,type,width,height):
        self.type = type #Determines the image and rect of this sprite.
        self.isActive = False #Determines the state of the sprite, for instance, an active door sprite is open, while an inactive door sprite is closed.awd

        #Initialize Sprite Constructor.
        pygame.sprite.Sprite.__init__(self)


        match self.type:
            case 0:
                pass
            case 1:
                self.image = pygame.Surface([width,height])
                #Temporary
            case 2: 
                pass #Write some code for damaging the player as this is a damaging block.
            case 3:
                pass #Write some code for a platform which can be passed through from the bottom but not fall through from the top.
            case 98: 
                pass #This section will stay like this as terrain type 98 is the player spawn point, which will have no collision cause it's just where the player starts.
            case 99:
                if self.isActive == True:
                    pass #Write some code for the end goal
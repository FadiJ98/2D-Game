import pygame
import os
import sys


class EndFlag(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.type = 99
        self.x = x
        self.y = 1016 - y
        self.frames = []
        self.frames.append(pygame.image.load(os.path.join(r"2D Game Images\Level_Tiles_Sets\Level_1\Flag Frames","Flag1.png")))
        self.frames.append(pygame.image.load(os.path.join(r"2D Game Images\Level_Tiles_Sets\Level_1\Flag Frames","Flag2.png")))
        self.frames.append(pygame.image.load(os.path.join(r"2D Game Images\Level_Tiles_Sets\Level_1\Flag Frames","Flag3.png")))
        self.frames.append(pygame.image.load(os.path.join(r"2D Game Images\Level_Tiles_Sets\Level_1\Flag Frames","Flag4.png")))
        self.frames.append(pygame.image.load(os.path.join(r"2D Game Images\Level_Tiles_Sets\Level_1\Flag Frames","Flag5.png")))
        self.frames.append(pygame.image.load(os.path.join(r"2D Game Images\Level_Tiles_Sets\Level_1\Flag Frames","Flag6.png")))
        self.frames.append(pygame.image.load(os.path.join(r"2D Game Images\Level_Tiles_Sets\Level_1\Flag Frames","Flag7.png")))
        self.frames.append(pygame.image.load(os.path.join(r"2D Game Images\Level_Tiles_Sets\Level_1\Flag Frames","Flag8.png")))

        pygame.sprite.Sprite.__init__(self)
    #Function for drawing the various frames of the flag.
    def Draw(self,curFrame,screen):
        screen.blit(self.frames[curFrame],(self.x,self.y))
    def collidesWith():
        pass

import pygame
import sys
import os
import Terrain

class LevelNode:
    def __init__(self, worldID, levelID, Name):
        #This is a linked list data type.
        #This is so that we can hold data about the level in the level selector, including whether the level can be selected at all, and also the neighboring levels for navigation purposes.
        #neighboring levels are classified into left, right, up, down, (and maybe a special identifier), this is because world navigation will be done with arrow keys/wasd
        self.levelAvailable = False
        self.levelName = Name
        self.worldId = worldID #The numeric identification of what world this level is in.
        self.levelId = levelID #The numeric identification of what level this level is.
        self.leftLevel = None #This is a pointer to the level to the left of this level.
        self.rightLevel = None #This is a pointer to the level to the left of this level.
        self.upLevel = None #This is a pointer to the level to the left of this level.
        self.downLevel = None #This is a pointer to the level to the left of this level.
        self.initMap = None #This will be a 2d array containing relevant data about about this level's terrain and collision layout.
        self.terrainMap = None #This will be a 2d array containing terrain object data.

        #Ignore everything related to collisionMap. Once I finish adapting to sprites it will become defunct.
        self.collisionMap = None #This will be a 2d array contianing pygame shapes that will act as collision boxes for players and monsters.
    
    
    def addLink(self,direction,Node):
            if direction == 0:
                self.leftLevel = Node
            elif direction == 1:
                self.rightLevel = Node
            elif direction == 2:
                self.upLevel = Node
            elif direction == 3:
                self.downLevel = Node
            else:
                print("You screwd up")
        
    def setAvailability(self,availability):
            self.levelAvailable = availability

    def setLevelMap(self,inMap):
        self.initMap = inMap

    def createLevel(self):
        if self.availability == None: 
            print("Level Not available, did not load.")
            return

        #Here we loop through the initMap and use it's data to construct collision boxes and terrain objects.
        for i in range(self.initMap.length()):
            for j in range(self.initMap.length()):
                
                #This section will be heavily modified Once I adapt to using sprites.
                match self.initMap[i][j]:
                    case 0: #when initMap is 0, that means that no collision boxes nor terrain objects are generated there.
                        self.collisionMap[i][j] = None 
                        self.terrainMap[i][j] = None

                    case 1: #when initMap is 1, that means that this is a standard terrain block.
                        pass #self.collisionMap[i][j] = pygame.Rect(i*20,j*20,20,20)
                        #self.terrainMap[i][j] = Terrain(1)


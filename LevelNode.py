
import pygame
import sys
import os
from EndFlag import EndFlag
from TerrainSprite import TerrainSprite
import PlayLevel

class LevelNode:
    def __init__(self, worldID, levelID, Name):
        #This is a linked list data type.
        #This is so that we can hold data about the level in the level selector, including whether the level can be selected at all, and also the neighboring levels for navigation purposes.
        #neighboring levels are classified into left, right, up, down, (and maybe a special identifier), this is because world navigation will be done with arrow keys/wasd
        self.availability = False
        self.levelName = Name
        self.worldId = worldID #The numeric identification of what world this level is in.
        self.levelId = levelID #The numeric identification of what level this level is.
        self.leftLevel = None #This is a pointer to the level to the left of this level.
        self.rightLevel = None #This is a pointer to the level to the left of this level.
        self.upLevel = None #This is a pointer to the level to the left of this level.
        self.downLevel = None #This is a pointer to the level to the left of this level.
        self.initMap = [] #This will be a 2d array containing relevant data about about this level's terrain and collision layout.
        self.terrainMap = []#This will be a 2d array containing terrain object data.
        
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
        self.availability = availability

    def setLevelMap(self,inMap):
        self.initMap = inMap
        for i in range(len(self.initMap)):
            self.terrainMap.append([])
            for j in range(len(self.initMap[i])):
                self.terrainMap[i].append(0)
        #For testing Purposes
        #print(self.initMap, self.terrainMap)

    def StartLevel(self,screen):
        #print("TEST Level Start")
        if self.availability == False:
            #print("level not available, did not load")
            return
        else:
            #print("TEST: Creating Level")
            #screen.fill((0,0,0))
            self.createLevel()
            #print(self.terrainMap)
            PlayLevel.GameLoop(self.terrainMap,screen)
            pass #If necessary this is where we'll enable player controls.

    def createLevel(self):
        if self.availability == False: 
            print("Level Not available, did not load.")
            return

        #Here we loop through the initMap and use it's data to construct collision boxes and terrain objects.
        
        for i in range(len(self.initMap)):
            for j in range(len(self.initMap[i])):
                #This section will be heavily modified Once I adapt to using sprites.
                Type = self.initMap[i][j]
                if Type == 99:
                    self.terrainMap[i][j] = EndFlag(i*64,j*64)
                    continue
                self.terrainMap[i][j] = TerrainSprite(Type,i*64,j*64)
                 
                ''' #Getto Block Commenting Method
                match self.initMap[i][j]:
                    case 0: #when initMap is 0, that means that no collision boxes nor terrain objects are generated there.
                        self.terrainMap[i][j] = TerrainSprite(0,i*64,j*64)

                    #Cases 1-2 are for regular solid terrain blocks, the differences are between what image they use.
                    case 1: #when initMap is 1, that means that this is a standard top terrain (grass) block.
                        self.terrainMap[i][j] = TerrainSprite(1,i*64,j*64)
                    case 1: #when initMap is 1, that means that this is a standard top terrain (grass) block.
                        self.terrainMap[i][j] = TerrainSprite(1,i*64,j*64)
                    case 1: #when initMap is 1, that means that this is a standard top terrain (grass) block.
                        self.terrainMap[i][j] = TerrainSprite(1,i*64,j*64)
                    case 1.1: #when initMap is 1, that means that this is a standard inner terrain block.
                        self.terrainMap[i][j] = TerrainSprite(1.1,i*64,j*64)
                    case 1.11: #when initMap is 1, that means that this is a standard left edge terrain block.
                        self.terrainMap[i][j] = TerrainSprite(1.2,i*64,j*64)
                    case 1.12: #when initMap is 1, that means that this is a standard right edge terrain block.
                        self.terrainMap[i][j] = TerrainSprite(1.3,i*64,j*64)
                '''


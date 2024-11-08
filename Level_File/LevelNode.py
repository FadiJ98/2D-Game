
import pygame
import sys
import os

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


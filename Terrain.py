
class Terrain:
    def __init__(self,type):
        self.type = type
        self.isActive = False #This is for blocks who's collision may change depending on external triggers. Such as the end goal,

    #This function is what runs when the player (or an enemy?) collides with a terrain object.
    def collide(self):
        match self.type:
            case 0:
                pass #Type 0 is when the terrain is air. AKA. A zone where there is no collisions nor anything drawn.
            case 1:
                pass #Write some code for stopping players as this is a solid block.
            case 1.1:
                pass #This code will be the same as above,
            case 2: 
                pass #Write some code for damaging the player as this is a damaging block.
            case 3:
                pass #Write some code for a platform which can be passed through from the bottom but not fall through from the top.
            case 98: 
                pass #This section will stay like this as terrain type 98 is the player spawn point, which will have no collision cause it's just where the player starts.
            case 99:
                #if goal.isOpen == True
                pass #Write some code for the end goal

    #This function will be run to draw the sprite corresponding with 
    def drawTerrain(self,Box):
        pass
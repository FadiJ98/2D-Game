import PlayLevel
from TerrainSprite import TerrainSprite


class LevelNode:
    def __init__(self, worldID, levelID, Name):
        """
        Represents a single level in a level selector.
        """
        self.availability = False
        self.levelName = Name
        self.worldId = worldID  # The numeric ID of the world this level belongs to.
        self.levelId = levelID  # The numeric ID of this level within its world.
        self.leftLevel = None
        self.rightLevel = None
        self.upLevel = None
        self.downLevel = None
        self.initMap = []  # 2D array for terrain and collision data.
        self.terrainMap = []  # 2D array for terrain sprite data.

    def addLink(self, direction, node):
        """
        Links this level node to another level node in a specific direction.
        :param direction: 0 = left, 1 = right, 2 = up, 3 = down
        :param node: The LevelNode to link to.
        """
        if direction == 0:
            self.leftLevel = node
        elif direction == 1:
            self.rightLevel = node
        elif direction == 2:
            self.upLevel = node
        elif direction == 3:
            self.downLevel = node
        else:
            raise ValueError("Invalid direction. Use 0 (left), 1 (right), 2 (up), or 3 (down).")

    def setAvailability(self, availability):
        """
        Sets the availability status of this level.
        :param availability: Boolean indicating if the level is playable.
        """
        self.availability = availability

    def setLevelMap(self, inMap):
        """
        Sets the initial terrain map for the level.
        :param inMap: 2D array containing terrain type data.
        """
        self.initMap = inMap
        self.terrainMap = [[0 for _ in row] for row in inMap]  # Initialize terrainMap with the same dimensions.

    def StartLevel(self, screen):
        """
        Starts the level if it is available.
        :param screen: Pygame screen to render the level.
        """
        if not self.availability:
            print(f"Level '{self.levelName}' is not available and cannot be started.")
            return

        print(f"Starting level: {self.levelName}")
        self.createLevel()
        PlayLevel.GameLoop(self.terrainMap, screen)

    def createLevel(self):
        """
        Constructs the level's terrain based on initMap.
        """

        if not self.availability:
            print(f"Level '{self.levelName}' is not available for creation.")
            return

        print(f"Creating terrain for level: {self.levelName}")

        for i, row in enumerate(self.initMap):
            for j, cell in enumerate(row):
                # Create a TerrainSprite for each cell in the map.
                self.terrainMap[i][j] = TerrainSprite(cell, j * 64, i * 64)
        print(f"Terrain created for level: {self.levelName}")

import pygame
import os

# Initialize some basic colors for testing purposes
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Global debug flag
DEBUG_MODE = False  # Set to True to draw rectangles instead of images

# Terrain implementation using sprites
class TerrainSprite(pygame.sprite.Sprite):
    def __init__(self, type, x, y):
        self.rect = None
        self.type = type  # Determines the image and rect of this sprite
        self.isActive = False  # Determines the state of the sprite
        self.Coords = (x, (1016 - y))  # Adjust y-coordinate to fit bottom-left origin
        width = 64
        height = 64

        # Initialize Sprite Constructor
        pygame.sprite.Sprite.__init__(self)

        match self.type:
            case 0:
                # Air: no image, no collision
                self.image = None
                self.rect = pygame.Rect(0, 0, 0, 0)
            case 1:
                # Grass Block Center
                self.image = pygame.image.load(os.path.join(
                    r"2D Game Images\Level_Tiles_Sets\Level_1\Individual Tiles", "Tile1.png"))
                self.rect = self.image.get_rect()
                self.rect.x = self.Coords[0]
                self.rect.y = self.Coords[1]
            case 1.1:
                # Grass Block Left
                self.image = pygame.image.load(os.path.join(
                    r"2D Game Images\Level_Tiles_Sets\Level_1\Individual Tiles", "Tile3.png"))
                self.rect = self.image.get_rect()
                self.rect.x = self.Coords[0]
                self.rect.y = self.Coords[1]
            case 1.2:
                # Grass Block Right
                self.image = pygame.image.load(os.path.join(
                    r"2D Game Images\Level_Tiles_Sets\Level_1\Individual Tiles", "Tile4.png"))
                self.rect = self.image.get_rect()
                self.rect.x = self.Coords[0]
                self.rect.y = self.Coords[1]
            case 2:
                # Dirt Block Center
                self.image = pygame.image.load(os.path.join(
                    r"2D Game Images\Level_Tiles_Sets\Level_1\Individual Tiles", "Tile2.png"))
                self.rect = self.image.get_rect()
                self.rect.x = self.Coords[0]
                self.rect.y = self.Coords[1]
            case 2.1:
                # Dirt Block Left
                self.image = pygame.image.load(os.path.join(
                    r"2D Game Images\Level_Tiles_Sets\Level_1\Individual Tiles", "Tile5.png"))
                self.rect = self.image.get_rect()
                self.rect.x = self.Coords[0]
                self.rect.y = self.Coords[1]
            case 2.2:
                # Dirt Block Right
                self.image = pygame.image.load(os.path.join(
                    r"2D Game Images\Level_Tiles_Sets\Level_1\Individual Tiles", "Tile6.png"))
                self.rect = self.image.get_rect()
                self.rect.x = self.Coords[0]
                self.rect.y = self.Coords[1]
            case 3:
                pass  # Placeholder for platforms or other blocks
            case 98:
                pass  # Placeholder for special blocks
            case 99:
                if self.isActive:
                    pass  # Placeholder for end goal logic

    def Draw(self, screen):
        """Draws the sprite image onto the screen if DEBUG_MODE is False."""
        if DEBUG_MODE:
            # Draw rectangle for debugging
            pygame.draw.rect(screen, RED, self.rect, 2)  # Outline the rect in red
        else:
            if self.image:
                # Draw the sprite's image
                screen.blit(self.image, self.Coords)

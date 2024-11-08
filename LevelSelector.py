import pygame
import sys
import os
from Level_File import LevelNode

# Initialize Pygame
pygame.init()

# Colors
LIGHT_BROWN = (205, 133, 63)
DARK_BROWN = (139, 69, 19)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HIGHLIGHT_COLOR = (240, 128, 128)

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Level Selector Map")

# Draw rounded rectangle function
def draw_rounded_rect(surface, color, rect, border_radius):
    pygame.draw.rect(surface, color, rect, border_radius=border_radius)

# Draw button function
def draw_button(surface, rect, text, font, mouse_pos):
    if rect.collidepoint(mouse_pos):
        draw_rounded_rect(surface, HIGHLIGHT_COLOR, rect, border_radius=20)
    else:
        draw_rounded_rect(surface, LIGHT_BROWN, rect, border_radius=20)

    text_surf = font.render(text, True, BLACK)
    surface.blit(text_surf, (rect.x + (rect.width - text_surf.get_width()) // 2, 
                             rect.y + (rect.height - text_surf.get_height()) // 2))

# Main function of LevelSelector with Back button functionality
def level_selector(screen):
    # Initialize font for the button text
    font = pygame.font.SysFont(None, 36)

    # Back button
    back_button_rect = pygame.Rect(20, 20, 100, 50)  # Positioned at the top-left

    # Initialization of levels
    originLevel = LevelNode.LevelNode(0,0,"New Beginnings")
    secondLevel = LevelNode.LevelNode(0,1,"Placeholder Name")
    originLevel.setAvailability(True)
    originLevel.addLink(0, secondLevel)
    selected_level = originLevel

    while True:
        screen.fill(BLACK)
        mouse_pos = pygame.mouse.get_pos()  # Get the current mouse position

        # Draw the Back button
        draw_button(screen, back_button_rect, "Back", font, mouse_pos)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and selected_level.rightLevel.levelAvailability:
                    selected_level = selected_level.rightLevel
                elif event.key == pygame.K_LEFT and selected_level.leftLevel.levelAvailability:
                    selected_level = selected_level.leftLevel
                elif event.key == pygame.K_UP and selected_level.upLevel.levelAvailability:
                    selected_level = selected_level.upLevel
                elif event.key == pygame.K_DOWN and selected_level.downLevel.levelAvailability:
                    selected_level = selected_level.downLevel
                elif event.key == pygame.K_RETURN and selected_level.levelAvailability:
                    selected_level.playLevel()
                elif event.key == pygame.K_DELETE:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(mouse_pos):
                    return  # Exit the level_selector function to go back to the main menu

        pygame.display.update()

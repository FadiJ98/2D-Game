#If everything goes right this will become the level selector.
#Currently contributor Sam
#Vision Statement. 
    #Although at first this will likely be as simple as a blank screen and a list, I eventually plan to make this a level selection screen in the same vein as mario 3's level selector.
    #The player will be able to control a small avatar who can then

#Import necessary libraries
import pygame
import sys
import os

#initialize Pygame
pygame.init()

# Colors copied from options (since that's where I copied the draw functions from)
LIGHT_BROWN = (205, 133, 63)
DARK_BROWN = (139, 69, 19)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HIGHLIGHT_COLOR = (240, 128, 128)

## Some copied functions from main and Options
# Create a function to draw rounded rectangles (for buttons, sliders, etc.)
def draw_rounded_rect(surface, color, rect, border_radius):
    pygame.draw.rect(surface, color, rect, border_radius=border_radius)

# Create a function to draw sliders with arrow buttons and wooden theme
def draw_slider(surface, rect, value, max_value, left_arrow, right_arrow):
    # Draw rounded background for the slider
    draw_rounded_rect(surface, LIGHT_BROWN, rect, border_radius=15)

    # Draw the slider handle based on the current value
    handle_position = (rect.x + int((value / max_value) * rect.width), rect.y + 5)
    handle_rect = pygame.Rect(handle_position[0], rect.y + 5, 30, rect.height - 10)  # Adjust handle size
    draw_rounded_rect(surface, DARK_BROWN, handle_rect, border_radius=10)

    # Draw arrows on each side of the slider
    pygame.draw.polygon(surface, DARK_BROWN, left_arrow)
    pygame.draw.polygon(surface, DARK_BROWN, right_arrow)

# Create a function to draw toggle buttons with rounded edges
def draw_toggle(surface, rect, state):
    color = LIGHT_BROWN if state else DARK_BROWN
    draw_rounded_rect(surface, color, rect, border_radius=15)
    # Draw an indicator to show if it is enabled or disabled
    indicator_rect = pygame.Rect(rect.x + (rect.width - 60 if state else 10), rect.y + 10, 40, rect.height - 20)
    draw_rounded_rect(surface, WHITE, indicator_rect, border_radius=10)

# Create a function to draw buttons with rounded corners
def draw_button(surface, rect, text, font, mouse_pos):
    if rect.collidepoint(mouse_pos):
        draw_rounded_rect(surface, HIGHLIGHT_COLOR, rect, border_radius=20)
    else:
        draw_rounded_rect(surface, LIGHT_BROWN, rect, border_radius=20)

    text_surf = font.render(text, True, BLACK)
    surface.blit(text_surf, (rect.x + (rect.width - text_surf.get_width()) // 2, 
                             rect.y + (rect.height - text_surf.get_height()) // 2))

# Main function of LevelSelector
def level_selector():
    while True:
        
        mouse_pos = pygame.mouse.get_pos()

        #Start tracking events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


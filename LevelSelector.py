#If everything goes right this will become the level selector.
#Currently contributor Sam
#Vision Statement. 
    #Although at first this will likely be as simple as a blank screen and a list, I eventually plan to make this a level selection screen in the same vein as mario 3's level selector.
    #The player will be able to control a small avatar who can then

#Import necessary libraries
import pygame
import sys
import os
#import levelNode

#initialize Pygame
pygame.init()

# Colors copied from options (since that's where I copied the draw functions from)
LIGHT_BROWN = (205, 133, 63)
DARK_BROWN = (139, 69, 19)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HIGHLIGHT_COLOR = (240, 128, 128)

# Set up the game window (width, height) (Again copied, thanks Fadi)
window_size = (1920, 1080)
screen = pygame.display.set_mode(window_size, pygame.RESIZABLE)
#pygame.display.set_caption("2D Game with GIF")

#Setting up black background

## Some copied functions from Options although I'll probably end up deleting the unused ones.
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


#This is the function for the levels linked list
import pygame
import sys
import os

def levelNode(worldID, levelID, Name):
    #This is a linked list data type.
    #This is so that we can hold data about the level in the level selector, including whether the level can be selected at all, and also the neighboring levels for navigation purposes.
    #neighboring levels are classified into left, right, up, down, (and maybe a special identifier), this is because world navigation will be done with arrow keys/wasd
    levelLinks = [None]*4
    levelAvailable = False
    levelName = Name
    worldId = worldID #The numeric identification of what world this level is in.
    levelId = levelID #The numeric identification of what level this level is.
    leftLevel = levelLinks[0] #This is a pointer to the level to the left of this level.
    rightLevel = levelLinks[1] #This is a pointer to the level to the left of this level.
    upLevel = levelLinks[2] #This is a pointer to the level to the left of this level.
    downLevel = levelLinks[3] #This is a pointer to the level to the left of this level.
    
    def addLink(direction,Node):
        levelLinks[direction] = Node
        
    def setAvailability(availability):
        levelAvailable = availability
    
#def playLevel():
    #When the actual level function is available this is where we will link to.



#Main function of LevelSelector
def level_selector():
    #Initiation of the first levels
    #WorldList = [levelNode]*10 #Not ready to be implented yet.
    originLevel = levelNode(0,0,"New Beginnings")
    secondLevel = levelNode(0,1,"Placeholder Name")
    originLevel.setAvailability(True)
    originLevel.addLink(0,secondLevel)
    selected_level = originLevel

    #When we are ready to create more levels we can make them here
    #Main loop
    while True:
        screen_width, screen_height = screen.get_size()  # Dynamically get the window size

        #Since the plan is to use a mario 3 style level selection screen im not going to bother rendering the gif. Black background anyone?
        pygame.draw.rect(screen,BLACK,pygame.rect(0,0,screen_width,screen_height))
        mouse_pos = pygame.mouse.get_pos() #Although I copied it over, I might not use it much


        #Start tracking events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #Check for key presses. Specifically
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if selected_level.rightLevel.levelAvailability == True:
                        selected_level = selected_level.rightLevel
                if event.key == pygame.K_LEFT:
                    if selected_level.leftLevel.levelAvailability == True:
                        selected_level = selected_level.leftLevel
                if event.key == pygame.K_UP:
                    if selected_level.upLevel.levelAvailability == True:
                        selected_level = selected_level.upLevel
                if event.key == pygame.K_DOWN:
                    if selected_level.downLevel.levelAvailability == True:
                        selected_level = selected_level.downLevel

                if event.key == pygame.K_RETURN:
                    if selected_level.levelAvailability == True:
                        selected_level.playLevel()

            #if event.type == pygame.Button_Left:
                #if play_button.collidepoint(mouse_pos):
                    #if selected_level.levelAvailability == True:
                        #selected_level.playLevel()

        #This is where the buttons and menus and other such graphical options will be created.
        LevelDisplay = pygame.rect(20,(screen_height-(screen_height//4)),screen_width-20,screen_height-20)
        draw_rounded_rect(screen,LIGHT_BROWN,LevelDisplay,40)
from turtle import Screen
import pygame
import sys
import os
from Level_File.LevelNode import LevelNode
from TerrainSprite import TerrainSprite

# Initialize Pygame
pygame.init()

# Colors
LIGHT_BROWN = (205, 133, 63)
DARK_BROWN = (139, 69, 19)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
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

def draw_button_locked(surface, rect, text, font, mouse_pos):
    draw_rounded_rect(surface, GRAY, rect, border_radius=20)

    text_surf = font.render(text, True, BLACK)
    surface.blit(text_surf, (rect.x + (rect.width - text_surf.get_width()) // 2, 
                             rect.y + (rect.height - text_surf.get_height()) // 2))

# Main function of LevelSelector with Back button functionality
def level_selector(screen):
    # Initialize font for the button text
    font = pygame.font.SysFont(None, 36)

    #Variable to control which world is selected.
    curWorld = 1

    # Back button
    back_button_rect = pygame.Rect(20, 20, 100, 50)  # Positioned at the top-left

    # Bottom Banner Rectangle
    banner_rect = pygame.Rect(0,400,800,200)

    # Play Button
    play_button_rect = pygame.Rect(550,475,100,50)

    # World Change Buttons
    left_button_rect = pygame.Rect(20,475,100,50)
    right_button_rect = pygame.Rect(680,475,100,50)

    # Level Buttons
    Level_Button1 = pygame.Rect(50, 100, 200, 100)
    Level_Button2 = pygame.Rect(300, 100, 200, 100)
    Level_Button3 = pygame.Rect(550, 100, 200, 100)
    Level_Button4 = pygame.Rect(50, 250, 200, 100)
    Level_Button5 = pygame.Rect(300, 250, 200, 100)
    Level_Button6 = pygame.Rect(550, 250, 200, 100)

    # Initialization of levels
    Level1 = LevelNode(1,0,"New Beginnings")
    Level2 = LevelNode(1,1,"Placeholder Name")
    Level3 = LevelNode(1,2,"Placeholder")
    Level4 = LevelNode(1,3,"Placeholder")
    Level5 = LevelNode(1,4,"Placeholder Name")
    Level6 = LevelNode(1,5,"Placeholder")
    Level7 = LevelNode(2,0,"Placeolder")
    Level8 = LevelNode(2,1,"Placeholder Name")
    Level9 = LevelNode(2,2,"Placeholder")
    Level10 = LevelNode(2,3,"Placeholder")
    Level11 = LevelNode(2,4,"Placeholder Name")
    Level12 = LevelNode(2,5,"Placeholder")
    Level13 = LevelNode(3,0,"Placeolder")
    Level14 = LevelNode(3,1,"Placeholder Name")
    Level15 = LevelNode(3,2,"Placeholder")
    Level16 = LevelNode(3,3,"Placeholder")
    Level17 = LevelNode(3,4,"Placeholder Name")
    Level18 = LevelNode(3,5,"Placeholder")
    Level1.setAvailability(True)
    Level1.setLevelMap([[0,1,0],[1,0,1],[0,1,0]])
    selected_level = None

    #TEST
    testSprite = TerrainSprite(1,300,300)

    while True:
        if curWorld == 1:
            screen.fill(BLACK) #Replace this with world 1 or 2 or 3 background depending on current world.
        elif curWorld == 2:
            screen.fill(GRAY)
        elif curWorld == 3:
            screen.fill(RED)


        mouse_pos = pygame.mouse.get_pos()  # Get the current mouse position

        #Testing Drawing Sprites
        testSprite.Draw()

        # Draw the Back button
        draw_button(screen, back_button_rect, "Back", font, mouse_pos)
        
        # Draw the bottom Banner
        pygame.draw.rect(screen,LIGHT_BROWN,banner_rect)

        # Draw the world changing buttons
        draw_button(screen,left_button_rect,"Prev\nWorld",font,mouse_pos)
        draw_button(screen,right_button_rect,"Next\nWorld",font,mouse_pos)

        # Draw the Play button
        draw_button(screen,play_button_rect,"Play",font,mouse_pos)

        #Drawing Level buttons for each world. If we're currently looking at world 1 levels, we will draw those buttons. Etc.
        if curWorld == 1:
            if Level1.availability == True:
                draw_button(screen, Level_Button1, "1", font, mouse_pos)
            else:
                draw_button_locked(screen, Level_Button1, "1", font, mouse_pos)
            if Level2.availability == True:
                draw_button(screen, Level_Button2, "2", font, mouse_pos)
            else:
                draw_button_locked(screen, Level_Button2, "2", font, mouse_pos)
            if Level3.availability == True:
                draw_button(screen, Level_Button3, "3", font, mouse_pos)
            else:
                draw_button_locked(screen, Level_Button3, "3", font, mouse_pos)
            if Level4.availability == True:
                draw_button(screen, Level_Button4, "4", font, mouse_pos)
            else:
                draw_button_locked(screen, Level_Button4, "4", font, mouse_pos)
            if Level5.availability == True:
                draw_button(screen, Level_Button5, "5", font, mouse_pos)
            else:
                draw_button_locked(screen, Level_Button5, "5", font, mouse_pos)
            if Level6.availability == True:
                draw_button(screen, Level_Button6, "6", font, mouse_pos)
            else:
                draw_button_locked(screen, Level_Button6, "6", font, mouse_pos)

        if curWorld == 2:
            if Level7.availability == True:
                draw_button(screen, Level_Button1, "7", font, mouse_pos)
            else:
                draw_button_locked(screen, Level_Button1, "7", font, mouse_pos)
            if Level8.availability == True:
                draw_button(screen, Level_Button2, "8", font, mouse_pos)
            else:
                draw_button_locked(screen, Level_Button2, "8", font, mouse_pos)
            if Level9.availability == True:
                draw_button(screen, Level_Button3, "9", font, mouse_pos)
            else:
                draw_button_locked(screen, Level_Button3, "9", font, mouse_pos)
            if Level10.availability == True:
                draw_button(screen, Level_Button4, "10", font, mouse_pos)
            else:
                draw_button_locked(screen, Level_Button4, "10", font, mouse_pos)
            if Level11.availability == True:
                draw_button(screen, Level_Button5, "11", font, mouse_pos)
            else:
                draw_button_locked(screen, Level_Button5, "11", font, mouse_pos)
            if Level12.availability == True:
                draw_button(screen, Level_Button6, "12", font, mouse_pos)
            else:
                draw_button_locked(screen, Level_Button6, "12", font, mouse_pos)

        if curWorld == 3:
            if Level13.availability == True:
                draw_button(screen, Level_Button1, "13", font, mouse_pos)
            else:
                draw_button_locked(screen, Level_Button1, "13", font, mouse_pos)
            if Level14.availability == True:
                draw_button(screen, Level_Button2, "14", font, mouse_pos)
            else:
                draw_button_locked(screen, Level_Button2, "14", font, mouse_pos)
            if Level15.availability == True:
                draw_button(screen, Level_Button3, "15", font, mouse_pos)
            else:
                draw_button_locked(screen, Level_Button3, "15", font, mouse_pos)
            if Level16.availability == True:
                draw_button(screen, Level_Button4, "16", font, mouse_pos)
            else:
                draw_button_locked(screen, Level_Button4, "16", font, mouse_pos)
            if Level17.availability == True:
                draw_button(screen, Level_Button5, "17", font, mouse_pos)
            else:
                draw_button_locked(screen, Level_Button5, "17", font, mouse_pos)
            if Level18.availability == True:
                draw_button(screen, Level_Button6, "18", font, mouse_pos)
            else:
                draw_button_locked(screen, Level_Button6, "18", font, mouse_pos)


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

                if curWorld == 1:
                    if Level_Button1.collidepoint(mouse_pos):
                        #Change bottom banner to include level information.
                        if Level1.availability == True:
                            print("TEST Level Should Start")
                            Level1.StartLevel() #Initialize Level 1
                    if Level_Button2.collidepoint(mouse_pos):
                        if Level2.availability == True:
                            #Initialize Level 2
                            Level2.StartLevel
                    if Level_Button3.collidepoint(mouse_pos):
                        if Level3.availability == True:
                            #Initialize Level 3
                            Level3.StartLevel
                    if Level_Button4.collidepoint(mouse_pos):
                        if Level4.availability == True:
                            #Initialize Level 4
                            Level4.StartLevel
                    if Level_Button5.collidepoint(mouse_pos):
                        if Level5.availability == True:
                            #Initialize Level 4
                            Level5.StartLevel
                    if Level_Button6.collidepoint(mouse_pos):
                        if Level6.availability == True:
                            #Initialize Level 3
                            Level6.StartLevel
                
                if curWorld == 2:
                    if Level_Button1.collidepoint(mouse_pos):
                        if Level7.availability == True:
                            Level7.StartLevel#Initialize Level 7
                    if Level_Button2.collidepoint(mouse_pos):
                        if Level8.availability == True:
                            #Initialize Level 8
                            Level8.StartLevel
                    if Level_Button3.collidepoint(mouse_pos):
                        if Level9.availability == True:
                            #Initialize Level 9
                            Level9.StartLevel
                    if Level_Button4.collidepoint(mouse_pos):
                        if Level10.availability == True:
                            #Initialize Level 10
                            Level10.StartLevel
                    if Level_Button5.collidepoint(mouse_pos):
                        if Level11.availability == True:
                            #Initialize Level 11
                            Level11.StartLevel
                    if Level_Button6.collidepoint(mouse_pos):
                        if Level12.availability == True:
                            #Initialize Level 12
                            Level12.StartLevel

                if curWorld == 3:
                    if Level_Button1.collidepoint(mouse_pos):
                        if Level13.availability == True:
                            Level13.StartLevel#Initialize Level 13
                    if Level_Button2.collidepoint(mouse_pos):
                        if Level14.availability == True:
                            #Initialize Level 14
                            Level14.StartLevel
                    if Level_Button3.collidepoint(mouse_pos):
                        if Level15.availability == True:
                            #Initialize Level 15
                            Level15.StartLevel
                    if Level_Button4.collidepoint(mouse_pos):
                        if Level16.availability == True:
                            #Initialize Level 16
                            Level16.StartLevel
                    if Level_Button5.collidepoint(mouse_pos):
                        if Level17.availability == True:
                            #Initialize Level 17
                            Level17.StartLevel
                    if Level_Button6.collidepoint(mouse_pos):
                        if Level18.availability == True:
                            #Initialize Level 18
                            Level18.StartLevel
                    




        pygame.display.update()
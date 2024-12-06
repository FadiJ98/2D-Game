from traceback import print_tb

import pygame
import sys
from Tiny_Dude_Hero import Hero

pygame.init()

running = True

# Load background
Background = pygame.image.load('2D Game Images/Level_Tiles_Sets/Level_1/TileSet3SC.png')


# Define a spawn point for the hero
SPAWN_POINT = (800, 900)  # Example spawn point coordinates (x=100, y=500)

terrainDict = {}



# Main Function
def GameLoop(Map, screen):
    global running
    hero = Hero(*SPAWN_POINT)
    clock = pygame.time.Clock()

    #Homeless Element That Should Be somewhere else but isn't because I'm a big dum so it's here for ease of access. From Sam.
    for i in range(len(Map)):
        for j in range(len(Map[i])):
            terrainDict[f"{i},{j}"] = Map[i][j].rect

    while running:
        delta_time = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if not hero.throwing:
                        hero.throwing = True
                        hero.throw_frame = 0
                        hero.rock_spawned = False

                if event.key == pygame.K_e:
                    hero.use_ability()

        #Checking if player is currently colliding with anything.
        # Checking if player is currently colliding with anything.
        #colRect = hero.rect.collidedict(terrainDict, True)

        for cord, rect in terrainDict.items():
            if isinstance(rect, pygame.Rect):
                if hero.rect.colliderect(rect):  # Check collision
                    # Determine the direction of collision
                    overlap_x = min(hero.rect.right - rect.left, rect.right - hero.rect.left)
                    overlap_y = min(hero.rect.bottom - rect.top, rect.bottom - hero.rect.top)

                    if overlap_x < overlap_y:
                        # Horizontal collision
                        if hero.rect.centerx < rect.centerx:
                            # Hero is to the left of the object
                            hero.x = rect.left - hero.rect.width
                        else:
                            # Hero is to the right of the object
                            hero.x = rect.right
                    else:
                        # Vertical collision
                        if hero.rect.centery < rect.centery:
                            # Hero is above the object
                            hero.y = rect.top - hero.rect.height
                            hero.velocity_y = 0  # Stop downward motion
                            hero.on_ground = True
                        else:
                            # Hero is below the object (unlikely unless jumping through platforms)
                            hero.y = rect.bottom
                            hero.velocity_y = 0  # Stop upward motion


        # Clear the screen with the background image
        screen.blit(Background, (0, 0))

        # Draw the map

        for i in range(len(Map)):
            for j in range(len(Map[i])):
                Map[i][j].Draw(screen)

        # Update and draw the hero
        hero.update(delta_time)
        hero.draw(screen)

        # Update the display
        pygame.display.update()

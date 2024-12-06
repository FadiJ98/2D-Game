from traceback import print_tb
from types import NoneType

import pygame
import sys
from Tiny_Dude_Hero import Hero
from enemy import Enemy



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

    # Create a list of enemies with different positions
    enemies = [
        Enemy(500, 800),
        Enemy(600, 800),
        Enemy(700, 800),
    ]

    clock = pygame.time.Clock()

    # Initialize the terrainDict for collision detection
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

        # Handle collisions between rocks and enemies
        for rock in hero.rocks:
            for enemy in enemies[:]:  # Use slicing to allow modification of the list during iteration
                if enemy.rect.colliderect(rock.rect):
                    print("Rock hit enemy!")
                    enemies.remove(enemy)  # Remove the enemy when hit by a rock

        # Handle collisions for hero and enemies with terrain
        for cord, rect in terrainDict.items():
            if isinstance(rect, pygame.Rect):
                # Handle hero collision
                if hero.rect.colliderect(rect):
                    overlap_x = min(hero.rect.right - rect.left, rect.right - hero.rect.left)
                    overlap_y = min(hero.rect.bottom - rect.top, rect.bottom - hero.rect.top)

                    if overlap_x < overlap_y:
                        # Horizontal collision
                        if hero.rect.centerx < rect.centerx:
                            hero.x = rect.left - hero.rect.width
                        else:
                            hero.x = rect.right
                    else:
                        # Vertical collision
                        if hero.rect.centery < rect.centery:
                            hero.y = rect.top - hero.rect.height
                            hero.velocity_y = 0
                            hero.on_ground = True
                        else:
                            hero.y = rect.bottom
                            hero.velocity_y = 0

                # Handle enemy collision
                for enemy in enemies:
                    if enemy.rect.colliderect(rect):
                        overlap_x = min(enemy.rect.right - rect.left, rect.right - enemy.rect.left)
                        overlap_y = min(enemy.rect.bottom - rect.top, rect.bottom - enemy.rect.top)

                        if overlap_x < overlap_y:
                            # Horizontal collision
                            if enemy.rect.centerx < rect.centerx:
                                enemy.x = rect.left - enemy.rect.width
                                enemy.direction = "left"  # Reverse direction
                            else:
                                enemy.x = rect.right
                                enemy.direction = "right"  # Reverse direction
                        else:
                            # Vertical collision
                            if enemy.rect.centery < rect.centery:
                                enemy.y = rect.top - enemy.rect.height
                                enemy.velocity_y = 0
                            else:
                                enemy.y = rect.bottom
                                enemy.velocity_y = 0

        # Clear the screen with the background image
        screen.blit(Background, (0, 0))

        # Draw the map
        for i in range(len(Map)):
            for j in range(len(Map[i])):
                Map[i][j].Draw(screen)

        # Update and draw the hero
        hero.update(delta_time)
        hero.draw(screen)

        # Update and draw all enemies
        for enemy in enemies:
            enemy.update(delta_time, terrainDict)
            enemy.draw(screen)

        # Update the display
        pygame.display.update()



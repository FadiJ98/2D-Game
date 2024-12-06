import pygame
import sys
from Tiny_Dude_Hero import Hero

pygame.init()

running = True

# Load background
Background = pygame.image.load('2D Game Images/Level_Tiles_Sets/Level_1/TileSet3SC.png')


# Define a spawn point for the hero
SPAWN_POINT = (800, 1000)  # Example spawn point coordinates (x=100, y=500)

# Main Function
def GameLoop(Map, screen):
    global running
    hero = Hero(*SPAWN_POINT)
    clock = pygame.time.Clock()

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

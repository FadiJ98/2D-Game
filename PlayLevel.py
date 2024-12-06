import pygame
import sys
from Tiny_Dude_Hero import Hero
from enemy import Enemy
from PauseMenu import pause_menu

pygame.init()

running = True

# Load background
Background = pygame.image.load('2D Game Images/Level_Tiles_Sets/Level_1/TileSet3SC.png')

# Define a spawn point for the hero
SPAWN_POINT = (800, 900)  # Example spawn point coordinates (x=100, y=500)

terrainDict = {}

# Load background music
pygame.mixer.init()
GAME_MUSIC = 'OST/World_1.mp3'  # Replace with the path to your music file


# Main Function
def GameLoop(Map, screen):
    global running
    hero = Hero(*SPAWN_POINT)

    # Create a list of enemies with different positions
    enemies = [
        Enemy(500, 800, left_bound=200, right_bound=900)
    ]

    clock = pygame.time.Clock()

    # Start the background music
    pygame.mixer.music.load(GAME_MUSIC)
    pygame.mixer.music.play(-1)  # Play indefinitely

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

                if event.key == pygame.K_ESCAPE:
                    # Pause music and call the pause menu
                    pygame.mixer.music.pause()
                    result = pause_menu(screen)
                    if result == "main_menu":  # If returning to the main menu
                        pygame.mixer.music.stop()
                        return "main_menu"
                    # Resume music after exiting the pause menu
                    pygame.mixer.music.unpause()

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

    # Stop the music when exiting the game loop
    pygame.mixer.music.stop()

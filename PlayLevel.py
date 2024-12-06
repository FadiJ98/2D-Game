import pygame
import sys
from Tiny_Dude_Hero import Hero
import os
from TerrainSprite import TerrainSprite
from entities import Enemy
from utility import *
pygame.init()

class Game:
    def __init__(self, hero):

        self.assets = {
            # 'particle/particle' : Animation(load_images('particles/particle'), image_dur=6, loop=False),
            'enemy/idle' : Animation(load_images('idle'), 6),
            'enemy/run' : Animation(load_images('walk'), 4)
        }
        #enemy creation
        enemy_size = (8, 15) # change this to the enemy size
        pos_1 = (0, 0)
         # change this to the projectile object the player shoots
        # pos_2 = (0, 0)
        # pos_3 = (0, 0)
        self.enemies = []
        self.enemies.append(Enemy(self,pos_1, enemy_size))
        # self.enemies.append(Enemy(self,pos_2, enemy_size))
        # self.enemies.append(Enemy(self,pos_3, enemy_size))

        self.particles = []
        self.sparks = []
running = True

# Load background
Background = pygame.image.load('2D Game Images/Level_Tiles_Sets/Level_1/TileSet3SC.png')


# Define a spawn point for the hero
SPAWN_POINT = (800, 900)  # Example spawn point coordinates (x=100, y=500)

# Main Function
def GameLoop(Map, screen):
    global running
    hero = Hero(*SPAWN_POINT)
    clock = pygame.time.Clock()
    game = Game(hero)
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

              
        rock = hero.rocks
        #draw the enemies and check if the player killed them
        for enemy in game.enemies.copy():
            kill = game.enemies.update(screen, rock)
            game.enemies.render(screen, offset = (0,0))
            if kill:
                game.enemies.remove(enemy)
            hurt = game.enemies.check_hurt(hero)
            if hurt:
                hero.take_damage(10)
        # Update and draw the hero
        hero.update(delta_time)
        hero.draw(screen)

        # Update the display
        pygame.display.update()



                


import math
import random

import pygame

from particle import Particle
from spark import Spark

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0]
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}
        
        self.action = ''
        self.anim_offset = (-3, -3)
        self.flip = False
        self.set_action('idle')
        
        self.last_movement = [0, 0]
    
    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
    
    def set_action(self, action):
        if action != self.action:
            self.action = action
            self.animation = self.game.assets[self.type + '/' + self.action].copy()
        
    def update(self, movement=(0, 0)):
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}
        
        frame_movement = (movement[0]*self.game.speed + self.velocity[0], movement[1] + self.velocity[1])
        
        self.pos[0] += frame_movement[0]
    
        
        self.pos[1] += frame_movement[1]
        
        
                
        if movement[0] > 0:
            self.flip = False
        if movement[0] < 0:
            self.flip = True
            
        self.last_movement = movement
        
        self.velocity[1] = min(5, self.velocity[1] + 0.1)
        
        if self.collisions['down'] or self.collisions['up']:
            self.velocity[1] = 0
            
        self.animation.update()
        
    def render(self, surf, offset=(0, 0)):
        surf.blit(pygame.transform.flip(self.animation.img(), self.flip, False), (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1]))
        
class Enemy(PhysicsEntity):
    def __init__(self, game, pos, size):
        super().__init__(game, 'enemy', pos, size)
        
        self.walking = 0
    def update (self, screen, rock, movement = (0, 0)):
        if self.walking:
            #move right
            if self.pos[0] < screen.get_width() - 50 and self.flip == False:
                movement = (movement[0] + 0.5 if self.flip else 0.5, movement[1])
            #move left
            elif self.pos[0] > 0 and self.flip == True:
                movement = (movement[0] - 0.5 if self.flip else 0.5, movement[1])
            else:
                #change directions
                self.flip = not self.flip   
            self.walking = max(0, self.walking - 1)
            if not self.walking:
                pass
                #this is where the enemy will shoot
        # this will randomly input the amount of ground the enemy will walk before pausing
        elif random.random() < 0.01:
            self.walking = random.randint(30, 120)
        
        super().update( movement=movement)
        if movement[0] != 0:
            self.set_action('run')
        else:
            self.set_action('idle')
        
        #check for collisions
        if self.rect().colliderect(rock.rect()):
            return True
        
    def check_hurt(self, player):
        if self.rect().colliderect(player.rect()):
            return True


    
      

import pygame
import sys
pygame.init()
class Enemy(pygame.sprite.Sprite):
    # this class should take in a sprite group, a sprite sheet (should only need the running animation, for now atleast)
    # the position it should be placed, how fast it should move, the main screen display variable, how tall and wide each part of the image is and the player

    def __init__(self,groups, loaded_image, x , y, mov_speed, screen, width, height, player):
        super().__init__(groups)
        self.image = loaded_image
        self.rect = pygame.Rect(x, y, width, height)
        self.facing = "left"
        self.mov_speed = mov_speed
        self.screen = screen
        self.width = width
        self.height = height
        self.old_rect = self.rect.copy()
        self.is_alive = True
        self.player = player
        #sprites
        self.sprites = []
        self.sprite_index = 0
        self.insert_image()


    def walk(self):
        if self.facing == "left" and self.rect.x <= 0:
            self.facing = "right" 
            self.rect.x += 2 * self.mov_speed
        elif self.facing == "right" and self.rect.x >= 750:
            self.facing = "left"
            self.rect.x -= 2 * self.mov_speed
        else:
            pass
        if self.facing == "left":
            self.rect.x -= self.mov_speed
        else:
            self.rect.x += self.mov_speed

    def insert_image(self):
        for i in range(self.image.get_width() // self.width):
            self.sprites.append(self.get_image(i, 2))
        
    
    def get_image(self, frame, scale, color = (0, 0 , 0)):
        image = pygame.Surface((self.width, self.height)).convert_alpha()
        image.blit(self.image, (0, 0), ((frame * self.width), 0 , self.width, self.height))
        image = pygame.transform.scale(image, (self.width * scale, self.height * scale))
        image.set_colorkey(color)
        return image
    
    # this will detect when the player kills the enemy by jumping on its head
    def collisions(self, direction):
        collision_sprites = pygame.sprite.spritecollide(self,self.player,True)
        if collision_sprites:
            if direction == "vertical":
                for sprite in collision_sprites:
                    # checking for a collision coming from the top
                    if self.rect.top <= sprite.rect.bottom and self.old_rect.top >= sprite.old_rect.bottom:
                        self.alive = False
                    


    def update(self):
        if self.is_alive == True:
            self.draw()
            self.walk()
            self.collisions("vertical")
    
    def draw(self):
        self.sprite_index += 0.2
        if (self.sprite_index >= len(self.sprites)):
            self.sprite_index = 0
        if self.facing == "left":
            image = pygame.transform.flip((self.sprites[int(self.sprite_index)]), True, False)
            image.set_colorkey((0,0,0))
            self.screen.blit(image, self.rect)
        else:
            self.screen.blit(self.sprites[int(self.sprite_index)], self.rect)


    #Add a function where when an enemy dies drops a coin
    



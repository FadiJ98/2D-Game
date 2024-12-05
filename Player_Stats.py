import pygame
import time
import sys
import os

pygame.init()

# character stats and abilities
MAX_HEALTH = 3
BASE_DAMAGE = 20
SHIELD_DURATION = 10  # 10 seconds shield duration for time-based protection
BUFF_DURATION = 10  # 10 seconds buff for double damage
COOLDOWN_ABILITY = 10  # Cooldown of 10 seconds for special ability

# Player class with stats
class Player:
    def __init__(self):
        self.health = MAX_HEALTH
        self.attack_damage = BASE_DAMAGE
        self.shield_active = False
        self.shield_hit_based = False
        self.shield_timer = 0
        self.buff_active = False
        self.ability_on_cooldown = False
        self.cooldown_timer = 0
        self.buff_timer = 0

    def take_damage(self, damage):
        if not self.shield_active:
            self.health -= damage
            print(f"Player took damage! Current health: {self.health}")
        elif self.shield_hit_based:
            print("Player shield absorbed the hit!")
            self.shield_active = False  
        if self.health < 0:
            self.health = 0

    def activate_shield(self, hit_based=False):
        self.shield_active = True
        self.shield_hit_based = hit_based
        if not hit_based:
            self.shield_timer = SHIELD_DURATION
            print(f"Time-based shield activated for {SHIELD_DURATION} seconds!")
        else:
            print("Hit-based shield activated!")

    def activate_buff(self):
        self.buff_active = True
        self.buff_timer = BUFF_DURATION
        self.attack_damage = BASE_DAMAGE * 2
        print("Buff activated! Double damage for 10 seconds!")

    def use_ability(self):
        if not self.ability_on_cooldown:
            print("Special ability used!")
            self.ability_on_cooldown = True
            self.cooldown_timer = COOLDOWN_ABILITY
        else:
            print("Ability is on cooldown!")

    def update(self, delta_time):
        # Update shield timer (if time-based)
        if self.shield_active and not self.shield_hit_based:
            self.shield_timer -= delta_time
            if self.shield_timer <= 0:
                self.shield_active = False
                print("Time-based shield expired!")

        # Update buff timer
        if self.buff_active:
            self.buff_timer -= delta_time
            if self.buff_timer <= 0:
                self.buff_active = False
                self.attack_damage = BASE_DAMAGE
                print("Buff expired! Damage returned to normal.")

        # Update ability cooldown
        if self.ability_on_cooldown:
            self.cooldown_timer -= delta_time
            if self.cooldown_timer <= 0:
                self.ability_on_cooldown = False
                print("Ability is ready to use again!")

    # Placeholder for claiming collectables (shield and buff)
    def collect_shield(self, hit_based=False):
        self.activate_shield(hit_based)

    def collect_buff(self):
        self.activate_buff()

# Main game loop 
player = Player()
running = True
clock = pygame.time.Clock()

while running:
    delta_time = clock.tick(60) / 1000  # Convert milliseconds to seconds

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard event for activating ability
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:  # Use ability with 'E' key
                player.use_ability()

    player.update(delta_time)
pygame.quit()

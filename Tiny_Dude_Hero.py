import pygame

pygame.init()

# Constants for screen size and hero scale
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCALE_FACTOR = 3
WALK_SPEED = 5
RUN_SPEED = 8  # Increased speed for running

# Initialize the screen
fullscreen = False  # Set to True for fullscreen mode
if fullscreen:
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()  # Get actual screen size in fullscreen
else:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hero Animation")

# Load spritesheets without "jump"
spritesheets = {
    "throw": pygame.image.load('2D Game Images/Heros/With_Rock/Tiny_Dude_Hero_With_Rock/Throw.png').convert_alpha(),
    "death": pygame.image.load('2D Game Images/Heros/With_Rock/Tiny_Dude_Hero_With_Rock/Death.png').convert_alpha(),
    "idle": pygame.image.load('2D Game Images/Heros/With_Rock/Tiny_Dude_Hero_With_Rock/Idle.png').convert_alpha(),
    "hurt": pygame.image.load('2D Game Images/Heros/With_Rock/Tiny_Dude_Hero_With_Rock/Hurt.png').convert_alpha(),
    "push": pygame.image.load('2D Game Images/Heros/With_Rock/Tiny_Dude_Hero_With_Rock/Push.png').convert_alpha(),
    "run": pygame.image.load('2D Game Images/Heros/With_Rock/Tiny_Dude_Hero_With_Rock/Run.png').convert_alpha(),
    "walk": pygame.image.load('2D Game Images/Heros/With_Rock/Tiny_Dude_Hero_With_Rock/Walk.png').convert_alpha()
}

# Load the rock image for throwing
rock_image = pygame.image.load('2D Game Images/Heros/With_Rock/Tiny_Dude_Hero_With_Rock/Rock1.png').convert_alpha()
rock_image = pygame.transform.scale(rock_image, (16 * SCALE_FACTOR, 16 * SCALE_FACTOR))

# Define frame counts without "jump"
frame_counts = {
    "throw": 4,
    "death": 4,
    "idle": 4,
    "hurt": 4,
    "push": 4,
    "run": 6,
    "walk": 6
}

# Function to load frames from a spritesheet
def load_frames(spritesheet, num_frames):
    frame_width = spritesheet.get_width() // num_frames
    frame_height = spritesheet.get_height()
    frames = []
    for i in range(num_frames):
        frame = spritesheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
        frame = pygame.transform.scale(frame, (frame_width * SCALE_FACTOR, frame_height * SCALE_FACTOR))
        frames.append(frame)
    return frames

# Initialize animations dictionary by loading frames for each action
animations = {action: load_frames(spritesheet, frame_counts[action]) for action, spritesheet in spritesheets.items()}

# Rock class for handling rock throws
class Rock:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        # Adjust the rock size to make it smaller
        self.image = pygame.transform.scale(rock_image, (12 * SCALE_FACTOR, 12 * SCALE_FACTOR))
        self.speed = 10

    def update(self):
        self.x += self.speed if self.direction == "right" else -self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# Player class with stats and abilities
MAX_HEALTH = 3
BASE_DAMAGE = 20
SHIELD_DURATION = 10  # 10 seconds shield duration for time-based protection
BUFF_DURATION = 10  # 10 seconds buff for double damage
COOLDOWN_ABILITY = 10  # Cooldown of 10 seconds for special ability

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
        if self.shield_active and not self.shield_hit_based:
            self.shield_timer -= delta_time
            if self.shield_timer <= 0:
                self.shield_active = False
                print("Time-based shield expired!")

        if self.buff_active:
            self.buff_timer -= delta_time
            if self.buff_timer <= 0:
                self.buff_active = False
                self.attack_damage = BASE_DAMAGE
                print("Buff expired! Damage returned to normal.")

        if self.ability_on_cooldown:
            self.cooldown_timer -= delta_time
            if self.cooldown_timer <= 0:
                self.ability_on_cooldown = False
                print("Ability is ready to use again!")

    def collect_shield(self, hit_based=False):
        self.activate_shield(hit_based)

    def collect_buff(self):
        self.activate_buff()

# Hero class to manage the hero's state and animation
import pygame
import time

pygame.init()

# Constants for screen size and hero scale
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCALE_FACTOR = 3
WALK_SPEED = 5
RUN_SPEED = 8  # Increased speed for running

# Initialize the screen
fullscreen = False  # Set to True for fullscreen mode
if fullscreen:
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()  # Get actual screen size in fullscreen
else:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hero Animation")

# Load spritesheets without "jump"
spritesheets = {
    "throw": pygame.image.load('2D Game Images/Heros/With_Rock/Tiny_Dude_Hero_With_Rock/Throw.png').convert_alpha(),
    "death": pygame.image.load('2D Game Images/Heros/With_Rock/Tiny_Dude_Hero_With_Rock/Death.png').convert_alpha(),
    "idle": pygame.image.load('2D Game Images/Heros/With_Rock/Tiny_Dude_Hero_With_Rock/Idle.png').convert_alpha(),
    "hurt": pygame.image.load('2D Game Images/Heros/With_Rock/Tiny_Dude_Hero_With_Rock/Hurt.png').convert_alpha(),
    "push": pygame.image.load('2D Game Images/Heros/With_Rock/Tiny_Dude_Hero_With_Rock/Push.png').convert_alpha(),
    "run": pygame.image.load('2D Game Images/Heros/With_Rock/Tiny_Dude_Hero_With_Rock/Run.png').convert_alpha(),
    "walk": pygame.image.load('2D Game Images/Heros/With_Rock/Tiny_Dude_Hero_With_Rock/Walk.png').convert_alpha()
}

# Load the rock image for throwing
rock_image = pygame.image.load('2D Game Images/Heros/With_Rock/Tiny_Dude_Hero_With_Rock/Rock1.png').convert_alpha()
rock_image = pygame.transform.scale(rock_image, (16 * SCALE_FACTOR, 16 * SCALE_FACTOR))

# Define frame counts without "jump"
frame_counts = {
    "throw": 4,
    "death": 4,
    "idle": 4,
    "hurt": 4,
    "push": 4,
    "run": 6,
    "walk": 6
}

# Function to load frames from a spritesheet
def load_frames(spritesheet, num_frames):
    frame_width = spritesheet.get_width() // num_frames
    frame_height = spritesheet.get_height()
    frames = []
    for i in range(num_frames):
        frame = spritesheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
        frame = pygame.transform.scale(frame, (frame_width * SCALE_FACTOR, frame_height * SCALE_FACTOR))
        frames.append(frame)
    return frames

# Initialize animations dictionary by loading frames for each action
animations = {action: load_frames(spritesheet, frame_counts[action]) for action, spritesheet in spritesheets.items()}

# Rock class for handling rock throws
class Rock:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        # Adjust the rock size to make it smaller
        self.image = pygame.transform.scale(rock_image, (12 * SCALE_FACTOR, 12 * SCALE_FACTOR))
        self.speed = 10

    def update(self):
        self.x += self.speed if self.direction == "right" else -self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# Player class with stats and abilities
MAX_HEALTH = 3
BASE_DAMAGE = 20
SHIELD_DURATION = 10  # 10 seconds shield duration for time-based protection
BUFF_DURATION = 10  # 10 seconds buff for double damage
COOLDOWN_ABILITY = 10  # Cooldown of 10 seconds for special ability

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
        if self.shield_active and not self.shield_hit_based:
            self.shield_timer -= delta_time
            if self.shield_timer <= 0:
                self.shield_active = False
                print("Time-based shield expired!")

        if self.buff_active:
            self.buff_timer -= delta_time
            if self.buff_timer <= 0:
                self.buff_active = False
                self.attack_damage = BASE_DAMAGE
                print("Buff expired! Damage returned to normal.")

        if self.ability_on_cooldown:
            self.cooldown_timer -= delta_time
            if self.cooldown_timer <= 0:
                self.ability_on_cooldown = False
                print("Ability is ready to use again!")

    def collect_shield(self, hit_based=False):
        self.activate_shield(hit_based)

    def collect_buff(self):
        self.activate_buff()

# Hero class to manage the hero's state and animation
class Hero(Player):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.action = "idle"
        self.direction = "right"
        self.current_frame = 0
        self.velocity_y = 0
        self.on_ground = True
        self.walking = False
        self.running = False
        self.width = animations["idle"][0].get_width()
        self.height = animations["idle"][0].get_height()
        self.rocks = []
        self.last_throw_time = 0
        self.throwing = False  # Track if currently throwing
        self.throw_frame = 0  # Track throw animation frame
        self.rock_spawned = False  # Track if the rock has been released
        # Add rect for collision detection
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, delta_time):
        super().update(delta_time)
        current_time = time.time()

        # Handle throwing (independent of other states)
        if self.throwing:
            self.throw_frame += 0.2  # Increment throw animation frame
            # Release rock during a specific frame of the throw animation
            if not self.rock_spawned and int(self.throw_frame) == 2:  # Example: Spawn rock on the 3rd frame
                rock_x = self.x + (self.width if self.direction == "right" else -16 * SCALE_FACTOR)
                rock_y = self.y + self.height // 2
                self.rocks.append(Rock(rock_x, rock_y, self.direction))
                self.rock_spawned = True  # Ensure rock is only released once during the throw

            # Check if throw animation has completed
            if int(self.throw_frame) >= len(animations["throw"]):
                self.throwing = False  # Reset throwing state
                self.throw_frame = 0  # Reset throw frame counter
                self.rock_spawned = False  # Reset rock release flag for the next throw

        # Update movement and state
        self.action = "idle"
        self.walking = False
        self.running = False

        keys = pygame.key.get_pressed()
        speed = WALK_SPEED
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            speed = RUN_SPEED
            self.running = True

        if keys[pygame.K_d]:
            self.x += speed
            self.direction = "right"
            self.walking = True
        elif keys[pygame.K_a]:
            self.x -= speed
            self.direction = "left"
            self.walking = True

        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = -10
            self.on_ground = False
            self.current_frame = 0

        # Gravity and boundary checks
        self.y += self.velocity_y
        self.velocity_y += 0.3

        if self.x < 0:
            self.x = 0
        elif self.x + self.width > SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - self.width

        if self.y >= SCREEN_HEIGHT - self.height:
            self.y = SCREEN_HEIGHT - self.height
            self.on_ground = True
            self.velocity_y = 0

        # Set action based on state
        if not self.on_ground:
            self.action = "walk" if self.walking else "idle"
        elif self.walking:
            self.action = "run" if self.running else "walk"

        # Update animation frame for the base action
        self.current_frame += 0.2
        if self.current_frame >= len(animations[self.action]):
            self.current_frame = 0

        # Update rocks
        for rock in self.rocks:
            rock.update()

        # Update the rect position for collision detection
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        # Determine which frame to draw
        if self.throwing:
            frame = animations["throw"][int(self.throw_frame)]
        else:
            frame = animations[self.action][int(self.current_frame)]

        if self.direction == "left":
            frame = pygame.transform.flip(frame, True, False)

        screen.blit(frame, (self.x, self.y))

        # Draw all thrown rocks
        for rock in self.rocks:
            rock.draw(screen)

# Main function to initialize and run the game
def main():
    hero = Hero(100, SCREEN_HEIGHT - 150)
    running = True
    clock = pygame.time.Clock()

    while running:
        delta_time = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Change throw trigger to "Enter" key
                    if not hero.throwing:
                        hero.throwing = True
                        hero.throw_frame = 0
                        hero.rock_spawned = False  # Reset rock release flag for new throw

                if event.key == pygame.K_e:
                    hero.use_ability()

        hero.update(delta_time)
        screen.fill((0, 0, 0))
        hero.draw(screen)
        pygame.display.flip()

    pygame.quit()

# Main guard to prevent running when imported
if __name__ == "__main__":
    main()

# Main function to initialize and run the game
def main():
    hero = Hero(100, SCREEN_HEIGHT - 150)
    running = True
    clock = pygame.time.Clock()

    while running:
        delta_time = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Change throw trigger to "Enter" key
                    if not hero.throwing:
                        hero.throwing = True
                        hero.throw_frame = 0
                        hero.rock_spawned = False  # Reset rock release flag for new throw

                if event.key == pygame.K_e:
                    hero.use_ability()

        hero.update(delta_time)
        screen.fill((0, 0, 0))
        hero.draw(screen)
        pygame.display.flip()

    pygame.quit()

# Main guard to prevent running when imported
if __name__ == "__main__":
    main()
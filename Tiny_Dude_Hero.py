import pygame
import time

# Initialize Pygame
pygame.init()

# Constants for screen size and hero scale
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCALE_FACTOR = 3
WALK_SPEED = 5
RUN_SPEED = 8  # Increased speed for running

# Set up the display
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
        self.image = rock_image
        self.speed = 10

    def update(self):
        # Move the rock in the direction it was thrown
        self.x += self.speed if self.direction == "right" else -self.speed


    def draw(self, screen):
        # Draw the rock on the screen
        screen.blit(self.image, (self.x, self.y))

# Hero class to manage the hero's state and animation
class Hero:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.action = "idle"
        self.direction = "right"
        self.current_frame = 0
        self.velocity_y = 0
        self.on_ground = True
        self.walking = False
        self.running = False
        self.width = animations["idle"][0].get_width()  # Width of hero sprite
        self.height = animations["idle"][0].get_height()  # Height of hero sprite
        self.rocks = []  # List to hold rocks thrown by the hero
        self.rocks = [rock for rock in self.rocks if 0 <= rock.x <= SCREEN_WIDTH]
        self.last_throw_time = 0  # Last time the throw was used

    def update(self, keys, mouse_buttons):
        current_time = time.time()  # Current time for handling delays
        previous_action = self.action
        self.action = "idle"
        self.walking = False
        self.running = False

        # Movement
        speed = WALK_SPEED
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:  # Sprinting with Shift key
            speed = RUN_SPEED
            self.running = True

        if keys[pygame.K_d]:  # Move right
            self.x += speed
            self.direction = "right"
            self.walking = True
        elif keys[pygame.K_a]:  # Move left
            self.x -= speed
            self.direction = "left"
            self.walking = True

        # Jumping with Space key
        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = -10
            self.on_ground = False
            self.current_frame = 0  # Reset frame for jump start

        # Apply gravity
        self.y += self.velocity_y
        self.velocity_y += 0.3  # Gravity effect

        # Prevent the player from going out of bounds horizontally
        if self.x < 0:
            self.x = 0
        elif self.x + self.width > SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - self.width

        # Prevent the player from going out of bounds vertically
        if self.y >= SCREEN_HEIGHT - self.height:
            self.y = SCREEN_HEIGHT - self.height
            self.on_ground = True
            self.velocity_y = 0

        # Throwing with left-click (mouse button 1) with a 0.5-second delay
        if mouse_buttons[0]:  # Left-click
            if current_time - self.last_throw_time >= 0.5:  # 0.5 second delay
                self.action = "throw"
                rock_x = self.x + (self.width if self.direction == "right" else -16 * SCALE_FACTOR)
                rock_y = self.y + self.height // 2
                self.rocks.append(Rock(rock_x, rock_y, self.direction))  # Use rock_image for throw
                self.last_throw_time = current_time  # Reset the timer for throw

        # Determine action based on state
        if self.action not in ["throw"]:
            # If airborne, show sprint animation if sprinting
            if not self.on_ground:
                if self.running:
                    self.action = "run"  # Show sprint (run) animation in air if sprinting
                else:
                    self.action = "walk" if self.walking else "idle"
            else:
                # Grounded state
                if self.walking:
                    self.action = "run" if self.running else "walk"
                else:
                    self.action = "idle"

        # Update frame index based on movement speed (faster for running)
        if self.running:
            self.current_frame += 0.5  # Faster frame progression for sprinting
        else:
            self.current_frame += 0.2  # Normal frame progression for walking

        if self.current_frame >= len(animations[self.action]):
            self.current_frame = 0  # Reset frame index after reaching the end

        # Update each rock's position
        for rock in self.rocks:
            rock.update()

    def draw(self, screen):
        # Draw the hero
        frame = animations[self.action][int(self.current_frame)]
        if self.direction == "left":
            frame = pygame.transform.flip(frame, True, False)
        screen.blit(frame, (self.x, self.y))

        # Draw each rock
        for rock in self.rocks:
            rock.draw(screen)

# Main game loop
hero = Hero(100, SCREEN_HEIGHT - 100)
clock = pygame.time.Clock()
running = True

while running:
    screen.fill((30, 30, 30))  # Clear the screen with a dark background

    keys = pygame.key.get_pressed()
    mouse_buttons = pygame.mouse.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update hero state and draw
    hero.update(keys, mouse_buttons)
    hero.draw(screen)

    pygame.display.flip()
    clock.tick(60)  # Control the frame rate

pygame.quit()

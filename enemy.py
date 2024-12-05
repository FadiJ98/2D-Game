import pygame
pygame.init()

# Constants for screen size and enemy scale
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCALE_FACTOR = 3  # Adjust scale for proper display

# Initialize the screen
fullscreen = False  # Set to True for fullscreen mode
if fullscreen:
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()  # Get actual screen size in fullscreen
else:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Enemy Animation Test")

# Load spritesheets for enemy states
spritesheets = {
    "idle": pygame.image.load('2D Game Images/Monsters/Monster 1/Monster_1_Idle-removebg-preview.png').convert_alpha(),
    "walk": pygame.image.load('2D Game Images/Monsters/Monster 1/Monster_1_Walk.png').convert_alpha(),
    "attack": pygame.image.load('2D Game Images/Monsters/Monster 1/Monster_1_Attack.png').convert_alpha(),
    "death": pygame.image.load('2D Game Images/Monsters/Monster 1/Monster_1_Death.png').convert_alpha()
}

# Frame counts for each state
frame_counts = {
    "idle": 4,
    "walk": 6,
    "attack": 4,
    "death": 4
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
animations = {state: load_frames(spritesheets[state], frame_counts[state]) for state in spritesheets}

# Enemy class with multiple animations
class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = "idle"  # Current state: idle, walk, attack, or death
        self.direction = "right"  # Direction the enemy is facing
        self.current_frame = 0  # Current animation frame
        self.width = animations["idle"][0].get_width()
        self.height = animations["idle"][0].get_height()
        self.mov_speed = 5  # Movement speed
        self.alive = True  # Whether the enemy is alive
        self.player_detected = False  # Whether a player is in range

    def update(self):
        # Update logic based on state
        if not self.alive:
            self.state = "death"
        elif self.player_detected:
            self.state = "attack"
        elif self.state == "walk":
            # Move left or right
            if self.direction == "right":
                self.x += self.mov_speed
            elif self.direction == "left":
                self.x -= self.mov_speed

            # Keep enemy within screen bounds
            if self.x < 0:
                self.x = 0
                self.direction = "right"
            elif self.x + self.width > SCREEN_WIDTH:
                self.x = SCREEN_WIDTH - self.width
                self.direction = "left"

        # Update animation frame
        self.current_frame += 0.2
        if self.current_frame >= len(animations[self.state]):
            self.current_frame = 0

    def draw(self, screen):
        # Get the current frame of the animation
        frame = animations[self.state][int(self.current_frame)]

        # Flip the frame if the enemy is facing left
        if self.direction == "left":
            frame = pygame.transform.flip(frame, True, False)

        # Draw the frame
        screen.blit(frame, (self.x, self.y))

    def detect_player(self, player_x, player_y):
        """Detects if the player is within attack range."""
        distance = abs(self.x - player_x)
        if distance < 200:
            self.player_detected = True
            self.state = "attack"
        else:
            self.player_detected = False
            self.state = "walk"

# Initialize the enemy at a specific position
enemy = Enemy(500, 500)

# Main game loop
running = True
clock = pygame.time.Clock()

# Fake player position for testing
player_x, player_y = 800, 500

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update logic
    enemy.detect_player(player_x, player_y)  # Fake player detection
    enemy.update()

    # Draw everything
    screen.fill((0, 0, 0))  # Clear the screen
    enemy.draw(screen)  # Draw the enemy
    pygame.display.flip()  # Update the display

    # Cap the frame rate
    clock.tick(60)

pygame.quit()

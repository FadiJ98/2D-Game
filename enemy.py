import pygame

# Global debug flag
DEBUG_MODE = False  # Set this to True to enable rectangle debugging

WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Screen constants
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCALE_FACTOR = 1

# Initialize Pygame
pygame.init()

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

def load_frames(spritesheet, num_frames):
    """Loads frames from a spritesheet."""
    frame_width = spritesheet.get_width() // num_frames
    frame_height = spritesheet.get_height()
    frames = []
    for i in range(num_frames):
        frame = spritesheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
        frame = pygame.transform.scale(frame, (frame_width * SCALE_FACTOR, frame_height * SCALE_FACTOR))
        frames.append(frame)
    return frames

# Initialize animations
animations = {state: load_frames(spritesheets[state], frame_counts[state]) for state in spritesheets}

class Enemy:
    def __init__(self, x, y, left_bound=None, right_bound=None, screen_size=(SCREEN_WIDTH, SCREEN_HEIGHT)):
        self.x = x
        self.y = y
        self.state = "idle"  # Start in idle state
        self.direction = "right"  # Initial direction
        self.current_frame = 0
        self.width = animations["idle"][0].get_width()
        self.height = animations["idle"][0].get_height()
        self.mov_speed = 2  # Slower walking speed
        self.velocity_y = 0
        self.on_ground = False  # Tracks if the enemy is on the ground
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.screen_width, self.screen_height = screen_size
        self.left_bound = left_bound if left_bound is not None else self.x - 100
        self.right_bound = right_bound if right_bound is not None else self.x + 100
        self.timer = 2  # Timer for idle and walking durations

    def update(self, delta_time, terrain_dict):
        self.velocity_y += 0.3  # Simulate gravity
        self.y += self.velocity_y
        self.on_ground = False  # Reset ground status

        # Vertical collision handling
        for rect in terrain_dict.values():
            if self.rect.colliderect(rect):
                if self.rect.bottom > rect.top and self.rect.centery < rect.centery:
                    self.y = rect.top - self.height
                    self.velocity_y = 0
                    self.on_ground = True
                elif self.rect.top < rect.bottom and self.rect.centery > rect.centery:
                    self.y = rect.bottom
                    self.velocity_y = 0

        self.rect.y = self.y  # Update rect position vertically

        # State switching logic
        self.timer -= delta_time
        if self.state == "idle" and self.timer <= 0:
            self.state = "walk"
            self.timer = 3  # Walk for 3 seconds
            self.direction = "right" if self.direction == "left" else "left"  # Alternate direction

        elif self.state == "walk" and self.timer <= 0:
            self.state = "idle"
            self.timer = 2  # Idle for 2 seconds

        # Handle walking logic
        if self.state == "walk":
            if self.direction == "right":
                self.x += self.mov_speed * delta_time * 60
            elif self.direction == "left":
                self.x -= self.mov_speed * delta_time * 60

            # Horizontal collision with terrain
            for rect in terrain_dict.values():
                if self.rect.colliderect(rect):
                    if self.rect.right > rect.left and self.x < rect.left:
                        self.x = rect.left - self.width
                        self.direction = "left"
                    elif self.rect.left < rect.right and self.x > rect.right:
                        self.x = rect.right
                        self.direction = "right"

            # Boundaries handling
            if self.x <= self.left_bound:
                self.x = self.left_bound
                self.direction = "right"
            elif self.x + self.width >= self.right_bound:
                self.x = self.right_bound - self.width
                self.direction = "left"

        self.rect.x = self.x  # Update rect position horizontally

        # Animation frame update
        self.current_frame += 0.2
        if self.current_frame >= len(animations[self.state]):
            self.current_frame = 0

    def draw(self, screen):
        frame = animations[self.state][int(self.current_frame)]
        if self.direction == "left":
            frame = pygame.transform.flip(frame, True, False)
        screen.blit(frame, (self.x, self.y))





import pygame

# Initialize Pygame
pygame.init()

# Screen settings (set to 1920x1080 resolution, non-resizable)
screen_width = 1920  # Width set to 1920
screen_height = 1080  # Height set to 1080
screen = pygame.display.set_mode((screen_width, screen_height))  # No pygame.RESIZABLE flag
pygame.display.set_caption("Non-Resizable Character Window - 1920x1080")

# Colors
BLACK = (0, 0, 0)

# Load the spritesheets
walk_spritesheet = pygame.image.load('Group_Project_resources_main/Dude_Monster_Walk_6.png').convert_alpha()
idle_image = pygame.image.load('Group_Project_resources_main/Dude_Monster.png').convert_alpha()
jump_spritesheet = pygame.image.load('Group_Project_resources_main/Dude_Monster_Jump_8.png').convert_alpha()

# Define some constants
SPRITE_WIDTH = walk_spritesheet.get_width() // 6  # There are 6 frames in the walk spritesheet
SPRITE_HEIGHT = walk_spritesheet.get_height()  # Height of each frame in the spritesheet
NUM_WALK_FRAMES = 6  # Number of frames in the walking animation
NUM_JUMP_FRAMES = 8  # Number of frames in the jumping animation
SCALE_FACTOR = 2  # Scale the character by 2x
GRAVITY = 0.03  # Lower gravity for an even slower fall
JUMP_STRENGTH = -5  # Reduced jump strength for slower upward motion, like Mario

# Function to slice the spritesheet into individual frames
def load_frames(spritesheet, num_frames, width, height):
    frames = []
    for i in range(num_frames):
        frame = spritesheet.subsurface(pygame.Rect(i * width, 0, width, height))
        frame = pygame.transform.scale(frame, (width * SCALE_FACTOR, height * SCALE_FACTOR))
        frames.append(frame)
    return frames

# Load all the frames for walking and jumping
walk_frames = load_frames(walk_spritesheet, NUM_WALK_FRAMES, SPRITE_WIDTH, SPRITE_HEIGHT)
jump_frames = load_frames(jump_spritesheet, NUM_JUMP_FRAMES, SPRITE_WIDTH, SPRITE_HEIGHT)

# Scale the idle image to match the size of walking frames
idle_image = pygame.transform.scale(idle_image, (SPRITE_WIDTH * SCALE_FACTOR, SPRITE_HEIGHT * SCALE_FACTOR))

# Player class to handle movement, animation, jumping, and idle state
class Player:
    def __init__(self, x, y, speed=0.3):
        self.x = x
        self.y = y
        self.speed = speed
        self.current_frame = 0
        self.walking = False
        self.jumping = False
        self.direction = "right"
        self.velocity_y = 0  # Vertical velocity for jumping
        self.on_ground = True  # To check if the player is on the ground

    def move(self, keys, screen_width, screen_height):
        self.walking = False
        if keys[pygame.K_a]:  # Move left with 'A' key
            self.x -= self.speed
            self.walking = True
            self.direction = "left"
        if keys[pygame.K_d]:  # Move right with 'D' key
            self.x += self.speed
            self.walking = True
            self.direction = "right"

        # Ensure the player stays within the screen bounds
        if self.x < 0:  # Don't allow moving past the left edge
            self.x = 0
        if self.x + SPRITE_WIDTH * SCALE_FACTOR > screen_width:  # Don't allow moving past the right edge
            self.x = screen_width - SPRITE_WIDTH * SCALE_FACTOR

        if keys[pygame.K_SPACE] and self.on_ground:  # Jump with 'Spacebar'
            self.jumping = True
            self.velocity_y = JUMP_STRENGTH
            self.on_ground = False

        if self.walking and not self.jumping:
            self.animate_walk()

    def jump(self, screen_height):
        # Apply gravity when jumping
        if self.jumping:
            self.y += self.velocity_y
            self.velocity_y += GRAVITY

            # Ensure the player stays within the screen bounds (for vertical movement)
            if self.y >= screen_height - SPRITE_HEIGHT * SCALE_FACTOR:  # Prevent falling below the ground
                self.y = screen_height - SPRITE_HEIGHT * SCALE_FACTOR
                self.jumping = False
                self.on_ground = True
                self.current_frame = 0  # Reset frame after landing

            if self.y < 0:  # Prevent jumping above the screen's top boundary
                self.y = 0

            self.animate_jump()

    def animate_walk(self):
        self.current_frame += 0.03  # Adjust animation speed for walking
        if self.current_frame >= NUM_WALK_FRAMES:
            self.current_frame = 0  # Ensure the frame resets when walking

    def animate_jump(self):
        self.current_frame += 0.005  # Slow down the frame switch rate during jump for smoother effect
        if self.current_frame >= NUM_JUMP_FRAMES:
            self.current_frame = NUM_JUMP_FRAMES - 1  # Cap the index to the last jump frame

    def draw(self, screen):
        if self.jumping:  # Draw jumping animation if jumping
            frame = jump_frames[int(self.current_frame)]
        elif self.walking:  # Draw walking animation if walking
            frame = walk_frames[int(self.current_frame)]
        else:  # Draw idle image if not walking
            frame = idle_image

        if self.direction == "left":
            frame = pygame.transform.flip(frame, True, False)  # Flip for left movement

        screen.blit(frame, (self.x, self.y))

# Initialize the player
player = Player(50, screen_height - (SPRITE_HEIGHT * SCALE_FACTOR) - 10)  # Start near the bottom left with a little space

# Main game loop
running = True
while running:
    screen.fill(BLACK)
    keys = pygame.key.get_pressed()  # Get the keys pressed

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move and draw the player
    player.move(keys, screen_width, screen_height)
    player.jump(screen_height)  # Apply jump logic
    player.draw(screen)

    # Update the display
    pygame.display.flip()

pygame.quit()

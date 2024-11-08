import pygame

# Initialize Pygame
pygame.init()

###
pygame.display.set_mode((1, 1)) #can be used later to diplay the character inside any level!!! 
###

# Load the spritesheets
walk_spritesheet = pygame.image.load('2D_Game_Images/Heros/With_Rock/Tiny_Dude_Hero_With_Rock/Walk.png').convert_alpha()
idle_spritesheet = pygame.image.load('2D_Game_Images/Heros/With_Rock/Tiny_Dude_Hero_With_Rock/Idle.png').convert_alpha()
jump_spritesheet = pygame.image.load('2D_Game_Images/Heros/With_Rock/Tiny_Dude_Hero_With_Rock/Jump.png').convert_alpha()
run_spritesheet = pygame.image.load('2D_Game_Images/Heros/With_Rock/Tiny_Dude_Hero_With_Rock/Run.png').convert_alpha()

# Define some constants
SPRITE_WIDTH = walk_spritesheet.get_width() // 6  # There are 6 frames in the walk spritesheet
SPRITE_HEIGHT = walk_spritesheet.get_height()  # Height of each frame in the spritesheet
RUN_SPRITE_WIDTH = run_spritesheet.get_width() // 6  # 6 frames in the running spritesheet
RUN_SPRITE_HEIGHT = run_spritesheet.get_height()  # Full height of the running spritesheet
IDLE_SPRITE_WIDTH = idle_spritesheet.get_width() // 4  # 4 frames in the idle spritesheet
IDLE_SPRITE_HEIGHT = idle_spritesheet.get_height()  # Full height of the idle spritesheet
NUM_WALK_FRAMES = 6  # Number of frames in the walking animation
NUM_RUN_FRAMES = 6  # Number of frames in the running animation
NUM_JUMP_FRAMES = 8  # Number of frames in the jumping animation
NUM_IDLE_FRAMES = 4  # Number of frames in the idle animation
SCALE_FACTOR = 3  # Scale the character by 3x
GRAVITY = 0.03  # Lower gravity for an even slower fall
JUMP_STRENGTH = -5  # Reduced jump strength for slower upward motion, like Mario
WALK_SPEED = 0.3  # Normal walking speed
RUN_SPEED = 0.6  # Faster running speed when holding Shift

# Function to slice the spritesheet into individual frames
def load_frames(spritesheet, num_frames, width, height):
    frames = []
    for i in range(num_frames):
        frame = spritesheet.subsurface(pygame.Rect(i * width, 0, width, height))
        frame = pygame.transform.scale(frame, (width * SCALE_FACTOR, height * SCALE_FACTOR))
        frames.append(frame)
    return frames

# Load all the frames for walking, jumping, running, and idling
walk_frames = load_frames(walk_spritesheet, NUM_WALK_FRAMES, SPRITE_WIDTH, SPRITE_HEIGHT)
run_frames = load_frames(run_spritesheet, NUM_RUN_FRAMES, RUN_SPRITE_WIDTH, RUN_SPRITE_HEIGHT)
jump_frames = load_frames(jump_spritesheet, NUM_JUMP_FRAMES, SPRITE_WIDTH, SPRITE_HEIGHT)
idle_frames = load_frames(idle_spritesheet, NUM_IDLE_FRAMES, IDLE_SPRITE_WIDTH, IDLE_SPRITE_HEIGHT)

# Player class to handle movement, animation, jumping, running, and idle state
class Player:
    def __init__(self, x, y, speed=WALK_SPEED):
        self.x = x
        self.y = y
        self.speed = speed
        self.current_frame = 0
        self.walking = False
        self.jumping = False
        self.running = False  
        self.direction = "right"
        self.velocity_y = 0  # Vertical velocity for jumping
        self.on_ground = True  # To check if the player is on the ground

    def move(self, keys, screen_width, screen_height):
        self.walking = False
        self.running = False
        self.speed = WALK_SPEED  
        
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:  # Run if Shift is held
            self.speed = RUN_SPEED
            self.running = True

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
            if self.running:
                self.animate_run()  # Animate running if running
            else:
                self.animate_walk()  # Animate walking if not running

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

    def animate_run(self):
        self.current_frame += 0.04  # Adjust animation speed for running (a bit faster than walking)
        if self.current_frame >= NUM_RUN_FRAMES:
            self.current_frame = 0  # Ensure the frame resets when running

    def animate_jump(self):
        self.current_frame += 0.005  # Slow down the frame switch rate during jump for smoother effect
        if self.current_frame >= NUM_JUMP_FRAMES:
            self.current_frame = NUM_JUMP_FRAMES - 1  # Cap the index to the last jump frame

    def animate_idle(self):
        self.current_frame += 0.01  # Slower animation speed for idling
        if self.current_frame >= NUM_IDLE_FRAMES:
            self.current_frame = 0  # Ensure the frame resets when idling

    def draw(self, screen):
        if self.jumping:  # Draw jumping animation if jumping
            frame = jump_frames[int(self.current_frame)]
        elif self.walking:  # Draw walking or running animation
            if self.running:
                frame = run_frames[int(self.current_frame)]  # Use run frames if running
            else:
                frame = walk_frames[int(self.current_frame)]  # Use walk frames if walking
        else:  # Draw idle animation immediately when not walking or jumping
            self.animate_idle()  # Advance idle frames
            frame = idle_frames[int(self.current_frame)]

        if self.direction == "left":
            frame = pygame.transform.flip(frame, True, False)  # Flip for left movement

        screen.blit(frame, (self.x, self.y))

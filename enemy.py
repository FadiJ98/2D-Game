    import pygame
    import time



    # Global debug flag
    DEBUG_MODE = False # Set this to True to enable rectangle debugging

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    # Initialize some constants
    SCREEN_WIDTH = 1920
    SCREEN_HEIGHT = 1080
    SCALE_FACTOR = 1  # Adjust scale for proper display
    SCALE = (SCREEN_WIDTH, SCREEN_HEIGHT)



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

    # Initialize animations dictionary by loading frames for each action
    animations = {state: load_frames(spritesheets[state], frame_counts[state]) for state in spritesheets}


    class Enemy:
        """Enemy class with animations, gravity, and basic AI."""
        def __init__(self, x, y, screen_size=(SCREEN_WIDTH, SCREEN_HEIGHT)):
            self.x = x
            self.y = y
            self.state = "walk"  # Start moving immediately
            self.direction = "right"  # Initial direction
            self.current_frame = 0  # Current animation frame
            self.width = animations["idle"][0].get_width()
            self.height = animations["idle"][0].get_height()
            self.mov_speed = 5  # Movement speed
            self.alive = True  # Whether the enemy is alive
            self.player_detected = False  # Whether a player is in range
            self.screen_width, self.screen_height = screen_size
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
            self.velocity_y = 0  # Vertical velocity for gravity
            self.on_ground = False  # Whether the enemy is on the ground

        def update(self, delta_time, terrain_dict):
            """Updates the enemy's state, position, and gravity."""
            # Apply gravity
            self.velocity_y += 0.3  # Gravity acceleration
            self.y += self.velocity_y

            # Reset ground state
            self.on_ground = False

            # Check for collisions with terrain
            for rect in terrain_dict.values():
                if self.rect.colliderect(rect):
                    # Vertical collision (ground or ceiling)
                    if self.rect.bottom > rect.top and self.rect.centery < rect.centery:
                        # Colliding with ground
                        self.y = rect.top - self.height
                        self.velocity_y = 0  # Stop downward movement
                        self.on_ground = True
                    elif self.rect.top < rect.bottom and self.rect.centery > rect.centery:
                        # Colliding with ceiling
                        self.y = rect.bottom
                        self.velocity_y = 0  # Stop upward movement

                    # Horizontal collision (walls)
                    if self.rect.right > rect.left and self.rect.centerx < rect.centerx:
                        # Colliding with the left side of a wall
                        self.x = rect.left - self.width
                        self.direction = "left"
                    elif self.rect.left < rect.right and self.rect.centerx > rect.centerx:
                        # Colliding with the right side of a wall
                        self.x = rect.right
                        self.direction = "right"

            # Horizontal movement
            if self.state == "walk":
                if self.direction == "right":
                    self.x += self.mov_speed
                elif self.direction == "left":
                    self.x -= self.mov_speed

                # Reverse direction if hitting screen bounds
                if self.x < 0:
                    self.x = 0
                    self.direction = "right"
                elif self.x + self.width > self.screen_width:
                    self.x = self.screen_width - self.width
                    self.direction = "left"

            # Update rect for collision detection
            self.rect.x = self.x
            self.rect.y = self.y

            # Update animation frame
            self.current_frame += 0.2
            if self.current_frame >= len(animations[self.state]):
                self.current_frame = 0

        def draw(self, screen):
            """Draws the enemy on the screen."""
            if DEBUG_MODE:
                # Draw the rectangle in debug mode
                pygame.draw.rect(screen, RED, self.rect, 2)  # Draw a red rectangle for debugging
            else:
                # Draw the sprite
                frame = animations[self.state][int(self.current_frame)]
                if self.direction == "left":
                    frame = pygame.transform.flip(frame, True, False)
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





    # Helper function to initialize a screen
    def init_screen(fullscreen=False):
        """Initializes a Pygame screen."""
        if fullscreen:
            screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            screen_width, screen_height = screen.get_size()
        else:
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Enemy Animation Test")
        return screen

    # Main function for testing
    def main():
        """Runs the main loop for testing the Enemy class."""
        screen = init_screen()
        enemy = Enemy(500, 500)

        # Fake player position for testing
        player_x, player_y = 800, 500

        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Update enemy logic
            enemy.detect_player(player_x, player_y)
            enemy.update()

            # Draw everything
            screen.fill((0, 0, 0))  # Clear the screen
            enemy.draw(screen)  # Draw the enemy
            pygame.display.flip()  # Update the display

            # Cap the frame rate
            clock.tick(60)

        pygame.quit()

    if __name__ == "__main__":
        main()

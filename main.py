import pygame
import sys
import os
import Option
import LevelSelector

# Center the window on the screen
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Initialize Pygame and the mixer for music
pygame.init()
pygame.mixer.init()

# Define global SFX volume
sfx_volume = 0.5  # Initial SFX volume (50%)

# Load the button sound effect
button_sound = pygame.mixer.Sound('OST/Buttons.mp3')
button_sound.set_volume(sfx_volume)  # Set initial SFX volume

# Set up the game window (width, height)
window_size = (1920, 1080)
screen = pygame.display.set_mode(window_size, pygame.RESIZABLE)
pygame.display.set_caption("TINY ADVENTURE")

# Define colors for the buttons
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HOVER_COLOR = (255, 255, 255)  # Color when hovering
START_COLOR = (0, 191, 255)  # Blue
OPTIONS_COLOR = (255, 165, 0)  # Orange
EXIT_COLOR = (0, 206, 209)  # Teal

# Load background music
pygame.mixer.music.load('OST/Menu-Music.wav')  # Replace with the actual music file path
pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely

# Set up fonts
font = pygame.font.Font(None, 80)

# Load the sword and handle images
sword_image = pygame.image.load('2D Game Images/Title/Sword.png')
SHandle_image = pygame.image.load('2D Game Images/Title/SHandle.png')

# Load and pre-scale GIF frames
gif_folder = "gif_frames"  # Folder containing individual frames of the GIF
gif_frames = []
for filename in sorted(os.listdir(gif_folder)):
    if filename.endswith(".gif"):
        img_path = os.path.join(gif_folder, filename)
        original_frame = pygame.image.load(img_path)
        scaled_frame = pygame.transform.scale(original_frame, window_size)
        gif_frames.append(scaled_frame)

# Define the frame rate for the main loop and GIF animation
current_frame = 0
frame_rate = 60  # Set frame rate to 60 for smoother performance
clock = pygame.time.Clock()

# Function to draw rounded rectangles
def draw_rounded_rect(surface, color, rect, corner_radius):
    pygame.draw.rect(surface, color, rect, border_radius=corner_radius)

# Calculate the center of the screen
def get_centered_rect(button_width, button_height, screen_width, screen_height, offset_y):
    return pygame.Rect((screen_width // 2 - button_width // 2), (screen_height // 2 - button_height // 2 + offset_y), button_width, button_height)

def render_title_with_sword(screen, x, y):
    sword_width, sword_height = 1800, 600
    scaled_sword_image = pygame.transform.scale(sword_image, (sword_width, sword_height))

    SHandle_width, SHandle_height = 800, 600
    scaled_SHandle_image = pygame.transform.scale(SHandle_image, (SHandle_width, SHandle_height))

    sword_x_offset, sword_y_offset = -220, 350
    sword_x, sword_y = x + sword_x_offset, y + sword_y_offset
    
    SHandle_x_offset, SHandle_y_offset = -320, 350
    SHandle_x, SHandle_y = x + SHandle_x_offset, y + SHandle_y_offset

    sword_rect = scaled_sword_image.get_rect(center=(sword_x, sword_y))
    screen.blit(scaled_sword_image, sword_rect)

    SHandle_rect = scaled_SHandle_image.get_rect(center=(SHandle_x, SHandle_y))
    screen.blit(scaled_SHandle_image, SHandle_rect)

# Function to render the title with "Tiny" and "Adventure" separately
def render_title(screen, x, y):
    tiny_font = pygame.font.Font(None, 300)
    adventure_font = pygame.font.Font(None, 200)

    tiny_shadow = tiny_font.render("TINY", True, (139, 69, 19))
    tiny_shadow_rect = tiny_shadow.get_rect(center=(x + 10, y + 120))
    screen.blit(tiny_shadow, tiny_shadow_rect)

    tiny_text = tiny_font.render("TINY", True, (255, 165, 0))
    tiny_text_rect = tiny_text.get_rect(center=(x, y + 110))
    screen.blit(tiny_text, tiny_text_rect)

    tiny_green = tiny_font.render("TINY", True, (34, 139, 34))
    tiny_green_rect = tiny_green.get_rect(center=(x, y + 130))
    screen.blit(tiny_green, tiny_green_rect)

    adventure_shadow = adventure_font.render("ADVENTURE", True, (139, 69, 19))
    adventure_shadow_rect = adventure_shadow.get_rect(center=(x + 10, y + 260))
    screen.blit(adventure_shadow, adventure_shadow_rect)

    adventure_text = adventure_font.render("ADVENTURE", True, (255, 165, 0))
    adventure_text_rect = adventure_text.get_rect(center=(x, y + 250))
    screen.blit(adventure_text, adventure_text_rect)

    adventure_green = adventure_font.render("ADVENTURE", True, (34, 139, 34))
    adventure_green_rect = adventure_green.get_rect(center=(x, y + 270))
    screen.blit(adventure_green, adventure_green_rect)

# Function to create a fade-in effect
def fade_in(screen, duration=2):
    fade_overlay = pygame.Surface(screen.get_size())
    fade_overlay.fill((0, 0, 0))
    for alpha in range(255, -1, -10):  # Decrease alpha from 255 to 0
        fade_overlay.set_alpha(alpha)
        screen.blit(gif_frames[current_frame], (0, 0))  # Background
        render_title(screen, screen.get_width() // 2, 200)  # Title
        render_title_with_sword(screen, screen.get_width() // 2, 200)  # Sword
        screen.blit(fade_overlay, (0, 0))
        pygame.display.flip()
        pygame.time.delay(int(duration * 10 / 255))

# Main menu function
def main_menu():
    global current_frame, sfx_volume

    # Trigger fade-in effect at the beginning
    fade_in(screen)

    while True:
        screen_width, screen_height = screen.get_size()
        mouse_pos = pygame.mouse.get_pos()

        # Button dimensions
        button_width, button_height = 300, 80
        button_offset_y = 250

        start_button_rect = get_centered_rect(button_width, button_height, screen_width, screen_height, -100 + button_offset_y)
        options_button_rect = get_centered_rect(button_width, button_height, screen_width, screen_height, 0 + button_offset_y)
        exit_button_rect = get_centered_rect(button_width, button_height, screen_width, screen_height, 100 + button_offset_y)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Update SFX volume and play sound
                button_sound.set_volume(sfx_volume)
                button_sound.play()

                # Check which button was clicked
                if start_button_rect.collidepoint(mouse_pos):
                    LevelSelector.level_selector(screen)
                elif options_button_rect.collidepoint(mouse_pos):
                    Option.options_menu(screen)
                    sfx_volume = Option.sfx_volume  # Update sfx_volume from Option module after returning
                elif exit_button_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        # Display the current frame of the pre-scaled GIF
        screen.blit(gif_frames[current_frame], (0, 0))  # Display scaled GIF frame
        current_frame = (current_frame + 1) % len(gif_frames)  # Update GIF frame

        # Render the title text at the adjusted position
        render_title(screen, screen_width // 2, 200)
        render_title_with_sword(screen, screen_width // 2, 200)

        # Draw buttons and their hover effect
        if start_button_rect.collidepoint(mouse_pos):
            draw_rounded_rect(screen, HOVER_COLOR, start_button_rect, 40)
        else:
            draw_rounded_rect(screen, START_COLOR, start_button_rect, 40)

        if options_button_rect.collidepoint(mouse_pos):
            draw_rounded_rect(screen, HOVER_COLOR, options_button_rect, 40)
        else:
            draw_rounded_rect(screen, OPTIONS_COLOR, options_button_rect, 40)

        if exit_button_rect.collidepoint(mouse_pos):
            draw_rounded_rect(screen, HOVER_COLOR, exit_button_rect, 40)
        else:
            draw_rounded_rect(screen, EXIT_COLOR, exit_button_rect, 40)

        start_text = font.render('Start', True, BLACK)
        options_text = font.render('Options', True, BLACK)
        exit_text = font.render('Exit', True, BLACK)

        screen.blit(start_text, (start_button_rect.x + 80, start_button_rect.y + 10))
        screen.blit(options_text, (options_button_rect.x + 40, options_button_rect.y + 10))
        screen.blit(exit_text, (exit_button_rect.x + 90, exit_button_rect.y + 10))

        pygame.display.flip()
        clock.tick(frame_rate)

# Run the menu
main_menu()

import pygame
import sys
import os
import Option
import LevelSelector

# testing changes in this code
print("making a change")
print("change was made succsefully ")



# Sam can now officially work with github.

# Initialize Pygame and the mixer for music
pygame.init()
pygame.mixer.init()

# Load background music
pygame.mixer.music.load('Menu-Music.wav')  # Replace with the actual music file path
pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely

# Set up the game window (width, height)
window_size = (1920, 1080)
screen = pygame.display.set_mode(window_size, pygame.RESIZABLE)
pygame.display.set_caption("2D Game with GIF")

# Define colors for the buttons
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HOVER_COLOR = (255, 255, 255)  # Color when hovering
START_COLOR = (0, 191, 255)  # Blue
OPTIONS_COLOR = (255, 165, 0)  # Orange
EXIT_COLOR = (0, 206, 209)  # Teal

# Set up fonts
font = pygame.font.Font(None, 80)

# Load the GIF frames dynamically from a folder
gif_folder = "gif_frames"  # Folder that contains individual frames of the GIF
gif_frames = []
for filename in sorted(os.listdir(gif_folder)):
    if filename.endswith(".gif"):  # Assuming the frames are GIF files
        img_path = os.path.join(gif_folder, filename)
        gif_frames.append(pygame.image.load(img_path))

# Define the frame rate for GIF animation
current_frame = 0
frame_rate = 20  # Speed of GIF animation (frames per second)
clock = pygame.time.Clock()

# Create a function to draw rounded rectangles
def draw_rounded_rect(surface, color, rect, corner_radius):
    pygame.draw.rect(surface, color, rect, border_radius=corner_radius)

# Calculate the center of the screen
def get_centered_rect(button_width, button_height, screen_width, screen_height, offset_y):
    return pygame.Rect((screen_width // 2 - button_width // 2), (screen_height // 2 - button_height // 2 + offset_y), button_width, button_height)

# Main menu function
def main_menu():
    global current_frame
    while True:
        screen_width, screen_height = screen.get_size()  # Dynamically get the window size
        mouse_pos = pygame.mouse.get_pos()  # Get the current mouse position

        # Button dimensions
        button_width = 300
        button_height = 80

        # Get centered positions for buttons
        start_button_rect = get_centered_rect(button_width, button_height, screen_width, screen_height, -100)
        options_button_rect = get_centered_rect(button_width, button_height, screen_width, screen_height, 0)
        exit_button_rect = get_centered_rect(button_width, button_height, screen_width, screen_height, 100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Check for mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(mouse_pos):
                    #LevelSelector.level_selector() #Takes the player
                    print("Start the game")

                elif options_button_rect.collidepoint(mouse_pos):
                    Option.options_menu(screen) #Takes the player to 
                    print("Options menu")

                elif exit_button_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        # Display the current frame of the GIF scaled to the window size
        gif_frame = pygame.transform.scale(gif_frames[current_frame], (screen_width, screen_height))
        screen.blit(gif_frame, (0, 0))  # Display scaled GIF

        # Update the GIF frame
        current_frame = (current_frame + 1) % len(gif_frames)

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

        # Render the button text
        start_text = font.render('Start', True, BLACK)
        options_text = font.render('Options', True, BLACK)
        exit_text = font.render('Exit', True, BLACK)

        # Draw the text on top of the buttons
        screen.blit(start_text, (start_button_rect.x + 70, start_button_rect.y + 10))  # Adjust text centering
        screen.blit(options_text, (options_button_rect.x + 40, options_button_rect.y + 10))  # Adjust text centering
        screen.blit(exit_text, (exit_button_rect.x + 70, exit_button_rect.y + 10))  # Adjust text centering

        # Update the display
        pygame.display.flip()

        # Control the frame rate for the GIF animation
        clock.tick(frame_rate)

# Run the menu
main_menu()

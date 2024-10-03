import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window (width, height)
window_size = (1920, 1080)
screen = pygame.display.set_mode(window_size, pygame.RESIZABLE)
pygame.display.set_caption("2D Game")

# Define colors for the buttons
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HOVER_COLOR = (180, 180, 180)  # Color when hovering
START_COLOR = (0, 191, 255)  # Blue
OPTIONS_COLOR = (255, 165, 0)  # Orange
EXIT_COLOR = (0, 206, 209)  # Teal
BUTTON_COLOR = (100, 100, 100)

# Set up fonts
font = pygame.font.Font(None, 80)

# Create a function to draw rounded rectangles
def draw_rounded_rect(surface, color, rect, corner_radius):
    pygame.draw.rect(surface, color, rect, border_radius=corner_radius)

# Calculate the center of the screen
def get_centered_rect(button_width, button_height, screen_width, screen_height, offset_y):
    # Center the button horizontally and place it with a y-offset
    return pygame.Rect((screen_width // 2 - button_width // 2), (screen_height // 2 - button_height // 2 + offset_y), button_width, button_height)

# Main menu function
def main_menu():
    while True:
        screen_width, screen_height = screen.get_size()  # Dynamically get the window size
        mouse_pos = pygame.mouse.get_pos()  # Get the current mouse position

        # Button dimensions
        button_width = 300
        button_height = 80

        # Get centered positions for buttons
        start_button_rect = get_centered_rect(button_width, button_height, screen_width, screen_height, -100)  # Offset for vertical spacing
        options_button_rect = get_centered_rect(button_width, button_height, screen_width, screen_height, 0)
        exit_button_rect = get_centered_rect(button_width, button_height, screen_width, screen_height, 100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Check for mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(mouse_pos):
                    print("Start the game")
                    # Call the start_game() function here

                elif options_button_rect.collidepoint(mouse_pos):
                    print("Options menu")
                    # Call the options_menu() function here

                elif exit_button_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        # Fill the background
        screen.fill(WHITE)

        # Draw and highlight buttons when hovering
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

# Run the menu
main_menu()

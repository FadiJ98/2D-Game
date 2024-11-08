import pygame
import sys
import Option

# Define pause menu colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HOVER_COLOR = (255, 255, 255)  # Color when hovering
RESUME_COLOR = (0, 191, 255)  # Blue
SETTINGS_COLOR = (255, 165, 0)  # Orange
MAIN_MENU_COLOR = (0, 206, 209)  # Teal
PAUSE_BACKGROUND_COLOR = (0, 0, 0, 180)  # Semi-transparent black

# Set up fonts
font = pygame.font.Font(None, 80)

def draw_rounded_rect(surface, color, rect, corner_radius):
    pygame.draw.rect(surface, color, rect, border_radius=corner_radius)

def get_centered_rect(button_width, button_height, screen_width, screen_height, offset_y):
    return pygame.Rect((screen_width // 2 - button_width // 2), (screen_height // 2 - button_height // 2 + offset_y), button_width, button_height)

# Pause menu function
def pause_menu(screen):
    paused = True
    clock = pygame.time.Clock()
    
    while paused:
        screen_width, screen_height = screen.get_size()  # Dynamically get the window size
        mouse_pos = pygame.mouse.get_pos()

        # Set up pause menu options dimensions
        button_width = 300
        button_height = 80

        # Center buttons on the screen
        resume_button_rect = get_centered_rect(button_width, button_height, screen_width, screen_height, -100)
        settings_button_rect = get_centered_rect(button_width, button_height, screen_width, screen_height, 0)
        main_menu_button_rect = get_centered_rect(button_width, button_height, screen_width, screen_height, 100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return  # Resume game if ESC is pressed again
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if resume_button_rect.collidepoint(mouse_pos):
                    return  # Resume game
                elif settings_button_rect.collidepoint(mouse_pos):
                    Option.options_menu(screen)  # Open settings
                elif main_menu_button_rect.collidepoint(mouse_pos):
                    from main import main_menu  # Import main_menu dynamically to avoid circular import issues
                    main_menu()  # Go to main menu
                    return

        # Darken the background for the pause menu
        overlay = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
        overlay.fill(PAUSE_BACKGROUND_COLOR)
        screen.blit(overlay, (0, 0))

        # Draw buttons and hover effect
        if resume_button_rect.collidepoint(mouse_pos):
            draw_rounded_rect(screen, HOVER_COLOR, resume_button_rect, 40)
        else:
            draw_rounded_rect(screen, RESUME_COLOR, resume_button_rect, 40)

        if settings_button_rect.collidepoint(mouse_pos):
            draw_rounded_rect(screen, HOVER_COLOR, settings_button_rect, 40)
        else:
            draw_rounded_rect(screen, SETTINGS_COLOR, settings_button_rect, 40)

        if main_menu_button_rect.collidepoint(mouse_pos):
            draw_rounded_rect(screen, HOVER_COLOR, main_menu_button_rect, 40)
        else:
            draw_rounded_rect(screen, MAIN_MENU_COLOR, main_menu_button_rect, 40)

        # Render the button text
        resume_text = font.render('Resume', True, BLACK)
        settings_text = font.render('Settings', True, BLACK)
        main_menu_text = font.render('Main Menu', True, BLACK)

        # Draw text on top of buttons
        screen.blit(resume_text, (resume_button_rect.x + 70, resume_button_rect.y + 10))
        screen.blit(settings_text, (settings_button_rect.x + 50, settings_button_rect.y + 10))
        screen.blit(main_menu_text, (main_menu_button_rect.x + 20, main_menu_button_rect.y + 10))

        # Update the display
        pygame.display.flip()
        clock.tick(30)  # Limit the pause menu frame rate


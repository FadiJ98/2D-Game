import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Define global variables
current_frame = 0  # Initialize current_frame globally for GIF handling

# Load the GIF frames dynamically from a folder (same as in your main menu)
gif_folder = "gif_frames"  # Folder that contains individual frames of the GIF
gif_frames = []
for filename in sorted(os.listdir(gif_folder)):
    if filename.endswith(".gif"):  # Assuming the frames are GIF files
        img_path = os.path.join(gif_folder, filename)
        gif_frames.append(pygame.image.load(img_path))

# Define the frame rate for GIF animation
frame_rate = 20  # Speed of GIF animation (frames per second)
clock = pygame.time.Clock()

# Define colors for the wooden theme
LIGHT_BROWN = (205, 133, 63)
DARK_BROWN = (139, 69, 19)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HIGHLIGHT_COLOR = (240, 128, 128)

# Set up fonts
font = pygame.font.Font(None, 60)  # You can load a custom font for a playful theme
button_font = pygame.font.Font(None, 50)

# Global settings to retain between visits to the options menu
music_volume = 0.5  # Initial volume is 50%
sfx_volume = 0.5  # Initial SFX volume is 50%
max_volume = 1.0  # Max volume in pygame is 1.0
effects_enabled = True  # Initial state of effects
fullscreen_enabled = False  # Initial state of fullscreen

# Set the initial music volume
pygame.mixer.music.set_volume(music_volume)

# Create a function to draw rounded rectangles (for buttons, sliders, etc.)
def draw_rounded_rect(surface, color, rect, border_radius):
    pygame.draw.rect(surface, color, rect, border_radius=border_radius)

# Create a function to draw sliders with arrow buttons and wooden theme
def draw_slider(surface, rect, value, max_value, left_arrow, right_arrow):
    # Draw rounded background for the slider
    draw_rounded_rect(surface, LIGHT_BROWN, rect, border_radius=15)

    # Draw the slider handle based on the current value
    handle_position = (rect.x + int((value / max_value) * rect.width), rect.y + 5)
    handle_rect = pygame.Rect(handle_position[0], rect.y + 5, 30, rect.height - 10)  # Adjust handle size
    draw_rounded_rect(surface, DARK_BROWN, handle_rect, border_radius=10)

    # Draw arrows on each side of the slider
    pygame.draw.polygon(surface, DARK_BROWN, left_arrow)
    pygame.draw.polygon(surface, DARK_BROWN, right_arrow)

# Create a function to draw toggle buttons with rounded edges
def draw_toggle(surface, rect, state):
    color = LIGHT_BROWN if state else DARK_BROWN
    draw_rounded_rect(surface, color, rect, border_radius=15)
    # Draw an indicator to show if it is enabled or disabled
    indicator_rect = pygame.Rect(rect.x + (rect.width - 60 if state else 10), rect.y + 10, 40, rect.height - 20)
    draw_rounded_rect(surface, WHITE, indicator_rect, border_radius=10)

# Create a function to draw buttons with rounded corners
def draw_button(surface, rect, text, font, mouse_pos):
    if rect.collidepoint(mouse_pos):
        draw_rounded_rect(surface, HIGHLIGHT_COLOR, rect, border_radius=20)
    else:
        draw_rounded_rect(surface, LIGHT_BROWN, rect, border_radius=20)

    text_surf = font.render(text, True, BLACK)
    surface.blit(text_surf, (rect.x + (rect.width - text_surf.get_width()) // 2, 
                             rect.y + (rect.height - text_surf.get_height()) // 2))

# Main options menu function
def options_menu(screen):
    global current_frame, music_volume, sfx_volume, effects_enabled, fullscreen_enabled  # Use global variables to retain the values

    # Variables to track dragging state
    dragging_music = False
    dragging_sfx = False

    # Get screen dimensions
    screen_width, screen_height = screen.get_size()

    # Calculate position offsets to center the menu on the left side
    left_offset_x = 100  # Left-aligned offset
    vertical_spacing = 120  # Space between each option

    while True:
        # Display the current frame of the GIF as the background
        gif_frame = pygame.transform.scale(gif_frames[current_frame], (screen_width, screen_height))
        screen.blit(gif_frame, (0, 0))  # Display the GIF

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Start dragging the music slider
                if music_slider_rect.collidepoint(mouse_pos):
                    dragging_music = True
                # Start dragging the SFX slider
                if sfx_slider_rect.collidepoint(mouse_pos):
                    dragging_sfx = True
                # Toggle effects
                if effects_toggle_rect.collidepoint(mouse_pos):
                    effects_enabled = not effects_enabled
                # Toggle fullscreen
                if fullscreen_toggle_rect.collidepoint(mouse_pos):
                    fullscreen_enabled = not fullscreen_enabled
                    if fullscreen_enabled:
                        screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE)
                # Back to main menu (replace with check/cross buttons later)
                if back_button_rect.collidepoint(mouse_pos):
                    return  # Exit the options menu and go back to the main menu

            if event.type == pygame.MOUSEBUTTONUP:
                # Stop dragging when mouse is released
                dragging_music = False
                dragging_sfx = False

            if event.type == pygame.MOUSEMOTION:
                # Adjust music volume slider if dragging
                if dragging_music:
                    music_volume = (mouse_pos[0] - music_slider_rect.x) / music_slider_rect.width
                    music_volume = max(0.0, min(music_volume, 1.0))  # Clamp value between 0 and 1
                    pygame.mixer.music.set_volume(music_volume)  # Adjust music volume
                # Adjust SFX volume slider if dragging
                if dragging_sfx:
                    sfx_volume = (mouse_pos[0] - sfx_slider_rect.x) / sfx_slider_rect.width
                    sfx_volume = max(0.0, min(sfx_volume, 1.0))  # Clamp value between 0 and 1

        # Button dimensions and positions (centered to the left)
        music_slider_rect = pygame.Rect(left_offset_x, 100, 400, 50)  # Left-aligned
        sfx_slider_rect = pygame.Rect(left_offset_x, 100 + vertical_spacing, 400, 50)
        effects_toggle_rect = pygame.Rect(left_offset_x, 100 + 2 * vertical_spacing, 200, 50)
        fullscreen_toggle_rect = pygame.Rect(left_offset_x, 100 + 3 * vertical_spacing, 200, 50)
        back_button_rect = pygame.Rect(left_offset_x, 100 + 4 * vertical_spacing, 200, 50)

        # Draw sliders with arrows
        left_arrow_music = [(left_offset_x - 30, 125), (left_offset_x - 10, 110), (left_offset_x - 10, 140)]
        right_arrow_music = [(left_offset_x + 400 + 30, 125), (left_offset_x + 400 + 10, 110), (left_offset_x + 400 + 10, 140)]
        draw_slider(screen, music_slider_rect, music_volume, max_volume, left_arrow_music, right_arrow_music)

        left_arrow_sfx = [(left_offset_x - 30, 125 + vertical_spacing), (left_offset_x - 10, 110 + vertical_spacing), (left_offset_x - 10, 140 + vertical_spacing)]
        right_arrow_sfx = [(left_offset_x + 400 + 30, 125 + vertical_spacing), (left_offset_x + 400 + 10, 110 + vertical_spacing), (left_offset_x + 400 + 10, 140 + vertical_spacing)]
        draw_slider(screen, sfx_slider_rect, sfx_volume, max_volume, left_arrow_sfx, right_arrow_sfx)

        # Draw toggle buttons
        draw_toggle(screen, effects_toggle_rect, effects_enabled)
        draw_toggle(screen, fullscreen_toggle_rect, fullscreen_enabled)

        # Render text for labels
        music_text = font.render("Music Volume", True, WHITE)
        sfx_text = font.render("SFX Volume", True, WHITE)
        effects_text = font.render("Effects Enabled", True, WHITE)
        fullscreen_text = font.render("Fullscreen", True, WHITE)

        # Draw labels (aligned to the right of the sliders and toggles)
        screen.blit(music_text, (left_offset_x + 450, 110))  # Labels positioned to the right of the sliders
        screen.blit(sfx_text, (left_offset_x + 450, 110 + vertical_spacing))
        screen.blit(effects_text, (left_offset_x + 450, 110 + 2 * vertical_spacing))
        screen.blit(fullscreen_text, (left_offset_x + 450, 110 + 3 * vertical_spacing))

        # Draw the Back button (temporary placeholder for check/cross buttons)
        draw_button(screen, back_button_rect, "Back", button_font, mouse_pos)

        # Update the GIF frame
        current_frame = (current_frame + 1) % len(gif_frames)

        # Update the display
        pygame.display.flip()

        # Control the frame rate for the GIF animation
        clock.tick(frame_rate)


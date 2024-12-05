import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Define global variables
current_frame = 0
music_volume = 0.2  # Initial music volume (50%)
sfx_volume = 0.5  # Initial SFX volume (50%)
max_volume = 1.0  # Maximum volume in pygame is 1.0
effects_enabled = True  # Initial state of effects
fullscreen_enabled = False  # Initial state of fullscreen

# Load the GIF frames dynamically from a folder
gif_folder = "gif_frames"  # Folder containing individual frames of the GIF
gif_frames = []
for filename in sorted(os.listdir(gif_folder)):
    if filename.endswith(".gif"):
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
font = pygame.font.Font(None, 60)
button_font = pygame.font.Font(None, 50)

# Set the initial music volume
pygame.mixer.music.set_volume(music_volume)

# Function to draw rounded rectangles (for buttons, sliders, etc.)
def draw_rounded_rect(surface, color, rect, border_radius):
    pygame.draw.rect(surface, color, rect, border_radius=border_radius)

# Function to draw sliders with arrow buttons
def draw_slider(surface, rect, value, max_value, left_arrow, right_arrow, dragging, mouse_pos):
    draw_rounded_rect(surface, LIGHT_BROWN, rect, border_radius=15)

    if dragging:
        value = (mouse_pos[0] - rect.x) / rect.width
        value = max(0.0, min(value, 1.0))
    
    handle_position = (rect.x + int(value * (rect.width - 30)), rect.y + 5)
    handle_rect = pygame.Rect(handle_position[0], rect.y + 5, 30, rect.height - 10)
    draw_rounded_rect(surface, DARK_BROWN, handle_rect, border_radius=10)

    pygame.draw.polygon(surface, DARK_BROWN, left_arrow)
    pygame.draw.polygon(surface, DARK_BROWN, right_arrow)

    return value

# Function to draw toggle buttons with rounded edges
def draw_toggle(surface, rect, state):
    color = LIGHT_BROWN if state else DARK_BROWN
    draw_rounded_rect(surface, color, rect, border_radius=15)
    indicator_rect = pygame.Rect(rect.x + (rect.width - 60 if state else 10), rect.y + 10, 40, rect.height - 20)
    draw_rounded_rect(surface, WHITE, indicator_rect, border_radius=10)

# Function to draw buttons with rounded corners
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
    global current_frame, music_volume, sfx_volume, effects_enabled, fullscreen_enabled

    dragging_music = False
    dragging_sfx = False

    screen_width, screen_height = screen.get_size()

    left_offset_x = 100
    vertical_spacing = 120

    while True:
        # Display the current frame of the GIF as the background
        gif_frame = pygame.transform.scale(gif_frames[current_frame], (screen_width, screen_height))
        screen.blit(gif_frame, (0, 0))

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if music_slider_rect.collidepoint(mouse_pos):
                    dragging_music = True
                if sfx_slider_rect.collidepoint(mouse_pos):
                    dragging_sfx = True
                if effects_toggle_rect.collidepoint(mouse_pos):
                    effects_enabled = not effects_enabled
                if fullscreen_toggle_rect.collidepoint(mouse_pos):
                    fullscreen_enabled = not fullscreen_enabled
                    if fullscreen_enabled:
                        screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE)
                if back_button_rect.collidepoint(mouse_pos):
                    return

            if event.type == pygame.MOUSEBUTTONUP:
                dragging_music = False
                dragging_sfx = False

            if event.type == pygame.MOUSEMOTION:
                if dragging_music:
                    music_volume = (mouse_pos[0] - music_slider_rect.x) / music_slider_rect.width
                    music_volume = max(0.0, min(music_volume, 1.0))
                    pygame.mixer.music.set_volume(music_volume)
                if dragging_sfx:
                    sfx_volume = (mouse_pos[0] - sfx_slider_rect.x) / sfx_slider_rect.width
                    sfx_volume = max(0.0, min(sfx_volume, 1.0))

        # Define button and slider dimensions and positions
        music_slider_rect = pygame.Rect(left_offset_x, 100, 400, 50)
        sfx_slider_rect = pygame.Rect(left_offset_x, 100 + vertical_spacing, 400, 50)
        effects_toggle_rect = pygame.Rect(left_offset_x, 100 + 2 * vertical_spacing, 200, 50)
        fullscreen_toggle_rect = pygame.Rect(left_offset_x, 100 + 3 * vertical_spacing, 200, 50)
        back_button_rect = pygame.Rect(left_offset_x, 100 + 4 * vertical_spacing, 200, 50)

        # Draw sliders with arrows
        left_arrow_music = [(left_offset_x - 30, 125), (left_offset_x - 10, 110), (left_offset_x - 10, 140)]
        right_arrow_music = [(left_offset_x + 400 + 30, 125), (left_offset_x + 400 + 10, 110), (left_offset_x + 400 + 10, 140)]
        music_volume = draw_slider(screen, music_slider_rect, music_volume, max_volume, left_arrow_music, right_arrow_music, dragging_music, mouse_pos)

        left_arrow_sfx = [(left_offset_x - 30, 125 + vertical_spacing), (left_offset_x - 10, 110 + vertical_spacing), (left_offset_x - 10, 140 + vertical_spacing)]
        right_arrow_sfx = [(left_offset_x + 400 + 30, 125 + vertical_spacing), (left_offset_x + 400 + 10, 110 + vertical_spacing), (left_offset_x + 400 + 10, 140 + vertical_spacing)]
        sfx_volume = draw_slider(screen, sfx_slider_rect, sfx_volume, max_volume, left_arrow_sfx, right_arrow_sfx, dragging_sfx, mouse_pos)

        # Draw toggle buttons
        draw_toggle(screen, effects_toggle_rect, effects_enabled)
        draw_toggle(screen, fullscreen_toggle_rect, fullscreen_enabled)

        # Render text for labels
        music_text = font.render("Music Volume", True, WHITE)
        sfx_text = font.render("SFX Volume", True, WHITE)
        effects_text = font.render("Effects Enabled", True, WHITE)
        fullscreen_text = font.render("Fullscreen", True, WHITE)

        screen.blit(music_text, (left_offset_x + 450, 110))
        screen.blit(sfx_text, (left_offset_x + 450, 110 + vertical_spacing))
        screen.blit(effects_text, (left_offset_x + 450, 110 + 2 * vertical_spacing))
        screen.blit(fullscreen_text, (left_offset_x + 450, 110 + 3 * vertical_spacing))

        draw_button(screen, back_button_rect, "Back", button_font, mouse_pos)

        current_frame = (current_frame + 1) % len(gif_frames)

        pygame.display.flip()
        clock.tick(frame_rate)

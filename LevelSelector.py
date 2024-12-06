import pygame
import sys
from LevelNode import LevelNode


# Initialize Pygame
pygame.init()

# Colors
LIGHT_BROWN = (205, 133, 63)
DARK_BROWN = (139, 69, 19)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
HIGHLIGHT_COLOR = (240, 128, 128)

# Global running variable
running = True

# Helper functions
def draw_button(surface, rect, text, font, mouse_pos, locked=False, is_selected=False):
    """Draw a button with hover, locked, and selected states."""
    if is_selected:
        color = (144, 238, 144)  # Light Green for selected level
    elif locked:
        color = GRAY
    else:
        color = HIGHLIGHT_COLOR if rect.collidepoint(mouse_pos) else LIGHT_BROWN

    pygame.draw.rect(surface, color, rect, border_radius=20)

    text_color = BLACK if not locked else WHITE
    text_surf = font.render(text, True, text_color)
    surface.blit(text_surf, (rect.x + (rect.width - text_surf.get_width()) // 2,
                             rect.y + (rect.height - text_surf.get_height()) // 2))

def draw_world(screen, levels, mouse_pos, font, center_x, center_y, selected_level):
    """Draw level buttons, centered horizontally and vertically."""
    button_width, button_height = 150, 75  # Adjusted button size
    padding_x, padding_y = 30, 30
    total_width = (button_width + padding_x) * 3 - padding_x
    total_height = (button_height + padding_y) * 2 - padding_y

    start_x = center_x - total_width // 2
    start_y = center_y - total_height // 2

    for idx, level in enumerate(levels):
        col = idx % 3
        row = idx // 3
        button_rect = pygame.Rect(
            start_x + col * (button_width + padding_x),
            start_y + row * (button_height + padding_y),
            button_width, button_height
        )
        level.button_rect = button_rect
        is_selected = (level == selected_level)  # Check if this level is selected
        draw_button(screen, button_rect, level.levelName, font, mouse_pos, locked=not level.availability, is_selected=is_selected)


# Main Level Selector function
def level_selector(screen):
    global running  # Use the global `running` variable to control the program state
    font = pygame.font.SysFont(None, 36)  # Adjusted font size

    # Define UI elements
    screen_width, screen_height = screen.get_size()
    button_width, button_height = 160, 80  # Smaller button size
    back_button_rect = pygame.Rect(20, 20, button_width, button_height)
    play_button_rect = pygame.Rect(screen_width // 2 - button_width, screen_height - 150, button_width * 2, button_height)
    left_button_rect = pygame.Rect(20, screen_height - 150, button_width * 2, button_height)
    right_button_rect = pygame.Rect(screen_width - 350, screen_height - 150, button_width * 2, button_height)

    # Initialize levels
    levels_by_world = {
        1: [LevelNode(1, i, f"Level {i+1}") for i in range(6)],
        2: [LevelNode(2, i, f"Level {i+7}") for i in range(6)],
        3: [LevelNode(3, i, f"Level {i+13}") for i in range(6)]
    }
    levels_by_world[1][0].setAvailability(True)  # Unlock the first level
    levels_by_world[1][0].setLevelMap([[1,1,1,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,1,2,2,2,1,1,2,2,2,2,2],
                                      [0,0,0,0,0,0,0,2.1,2,2.2,0,0,0,0,0,0,0,0,0,0,2.1,2,2.2,0,0,2.1,2,2,2,2],
                                      [0,0,0,0,0,0,0,1.1,1,1.2,0,0,0,0,0,0,0,0,0,0,1.1,1,1.2,0,0,2.1,2,2,2,2],
                                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2.1,2,2,2,2],
                                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1.1,1,1,1,1],
                                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,99,0])
    current_world = 1
    selected_level = None

    while running:  # Use the global `running` variable
        mouse_pos = pygame.mouse.get_pos()

        # Draw background
        screen.fill(DARK_BROWN)

        # Draw UI elements
        draw_button(screen, back_button_rect, "Back", font, mouse_pos)
        draw_button(screen, play_button_rect, "Play", font, mouse_pos)
        draw_button(screen, left_button_rect, "Prev", font, mouse_pos)
        draw_button(screen, right_button_rect, "Next", font, mouse_pos)

        # Draw levels for the current world
        # Draw levels for the current world
        draw_world(screen, levels_by_world[current_world], mouse_pos, font, screen_width // 2, screen_height // 2,
                   selected_level)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Stop the main loop
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(mouse_pos):
                    return  # Exit the level selector
                if play_button_rect.collidepoint(mouse_pos) and selected_level:
                    print(f"Starting {selected_level.levelName}")
                    selected_level.StartLevel(screen)
                if left_button_rect.collidepoint(mouse_pos):
                    current_world = max(1, current_world - 1)
                if right_button_rect.collidepoint(mouse_pos):
                    current_world = min(3, current_world + 1)

                # Check if any level button is clicked
                for level in levels_by_world[current_world]:
                    if hasattr(level, 'button_rect') and level.button_rect.collidepoint(
                            mouse_pos) and level.availability:
                        selected_level = level
                        print(f"Selected {selected_level.levelName}")

        # Update display
        pygame.display.flip()

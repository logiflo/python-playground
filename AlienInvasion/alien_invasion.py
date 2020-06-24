import sys
import pygame
from settings import Settings


def run_game():
    """Initialize game and create a screen object
    """
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.width, ai_settings.height))
    pygame.display.set_caption("Alien Invasion")

    # Start the main loop for the game.
    running = True
    while running:

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

        if not running:
            break

        # Redrawn the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)
        pygame.display.update()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == "__main__":
    run_game()

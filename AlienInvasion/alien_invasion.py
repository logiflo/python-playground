import sys
import pygame


def run_game():
    """Initialize game and create a screen object
    """
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    # Set the background color.
    bg_color = (0, 0, 100)

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
        screen.fill(bg_color)
        pygame.display.update()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == "__main__":
    run_game()

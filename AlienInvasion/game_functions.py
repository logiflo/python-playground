import sys
import pygame
from ship import Ship


def check_KEYDOWN(event, ship):
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        # Move the ship to the left
        ship.moving_left = True


def check_KEYUP(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    """Respond to keypresses and mouse events
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return False

        elif event.type == pygame.KEYDOWN:
            check_KEYDOWN(event, ship)

        elif event.type == pygame.KEYUP:
            check_KEYUP(event, ship)

    return True


def draw_screen(ai_settings, screen, ship):
    """Update image screen and flip to the new screen
    """
    # Redrawn the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()

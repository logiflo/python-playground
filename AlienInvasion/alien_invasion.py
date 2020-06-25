import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group


def run_game():
    """Initialize game and create a screen object
    """
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the ship a gruop of bullet and aliens
    ship = Ship(ai_settings, screen)
    # Make a Group to store bullets
    bullets = Group()
    aliens = Group()

    # Create a fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)


    # Start the main loop for the game.
    running = True
    while running:
        # Watch for keyboard and mouse events.
        running = gf.check_events(ai_settings, screen, ship, bullets)
        if not running:
            break
        ship.update_moving()
        gf.bullet_update(bullets)
        gf.draw_screen(ai_settings, screen, ship, aliens, bullets)


if __name__ == "__main__":
    run_game()

import sys
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from button import Button


def run_game():
    """Initialize game and create a screen object
    """
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the play button
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store the game statistics
    stat = GameStats(ai_settings)

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
        running = gf.check_events(ai_settings, screen, stat, ship, aliens, bullets, play_button)
        if not running:
            break

        if stat.game_active:
            ship.update_moving()
            gf.bullet_update(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stat, screen, ship, aliens, bullets)

        gf.draw_screen(ai_settings, screen, stat ,ship, aliens, bullets, play_button)


if __name__ == "__main__":
    run_game()

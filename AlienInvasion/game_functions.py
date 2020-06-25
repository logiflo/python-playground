import sys
import pygame
from ship import Ship
from bullet import Bullet


def check_KEYDOWN(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        # Move the ship to the left
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def check_KEYUP(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return False

        elif event.type == pygame.KEYDOWN:
            check_KEYDOWN(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_KEYUP(event, ship)

    return True


def draw_screen(ai_settings, screen, ship, bullets):
    """Update image screen and flip to the new screen
    """
    # Redrawn the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)

    # Redraw the bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.blitbullet()

    ship.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()


def bullet_update(bullets):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.image_rect.bottom <= 0 or bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
            if len(bullets) < ai_settings.bullet_allowed:
                # Create a new bullet
                new_bullet = Bullet(ai_settings, screen, ship)
                bullets.add(new_bullet)

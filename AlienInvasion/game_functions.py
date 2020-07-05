import sys
import pygame
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep


def check_KEYDOWN(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        # Move the ship to the left
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

    elif event.key == pygame.K_ESCAPE:
        return False

    return True

def check_KEYUP(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, stat, sb, ship, aliens, bullets, play_button):
    """Respond to keypresses and mouse events
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return False

        elif event.type == pygame.KEYDOWN:
            return check_KEYDOWN(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_KEYUP(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen ,stat, sb, ship, aliens, bullets, play_button, mouse_x, mouse_y)

    return True


def check_play_button(ai_settings, screen ,stat, sb, ship, aliens, bullets, play_button, mouse_x, mouse_y):
    """Start a new game when the user clicks play
    """
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if  button_clicked and not stat.game_active:
        # Reset the settings
        ai_settings.initialize_dynamic_settings()

        # Hide the mouse cursor
        pygame.mouse.set_visible(False)
        # Reset the game statistisc
        stat.reset_stat()
        stat.game_active = True

        # Reset scoreboard image
        sb.prep_score()
        sb.prep_highscore()
        sb.prep_level()
        sb.prep_ship()

        # Empty the list of aliens and bullets
        bullets.empty()
        aliens.empty()

        # Create a new fleet
        create_fleet(ai_settings, screen, ship, aliens)
        ship.ship_center()


def draw_screen(ai_settings, screen, stat, sb, ship, aliens, bullets, play_button):
    """Update image screen and flip to the new screen
    """
    # Redrawn the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)

    # Redraw the bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.blitbullet()

    ship.blitme()
    aliens.draw(screen)

    # Draw the scoreboard
    sb.draw_score()

    # Draw the play button is the game is unactive
    if not stat.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible.
    pygame.display.flip()


def bullet_update(ai_settings, screen, stat, sb, ship, aliens, bullets):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.image_rect.bottom <= 0 or bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullets_colisions(ai_settings, screen, stat, sb, ship, aliens, bullets)


def check_bullets_colisions(ai_settings, screen, stat, sb, ship, aliens, bullets):
    """Check for any bullets that have hit any aliens
    """
    colisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if colisions:
        for aliens in colisions.values():
            stat.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stat, sb)

    if len(aliens) == 0:
        # Destroy existing bullets and create a new fleet
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)

        # Increase level
        stat.level += 1
        sb.prep_level()


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullet_allowed:
        # Create a new bullet
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit the row
    """
    available_space_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(available_space_x / (2*alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """ Determine the number of rows
    """
    available_space_y = ai_settings.screen_height - 3*alien_height - ship_height
    number_rows = int(available_space_y / (3*alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create a sigle alien
    """
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = 3*alien_width + 1.5*alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien_height + 1.5*alien_height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens
    """
    # Create the first row of aliens
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(
        ai_settings, ship.rect.height, alien.rect.width)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x + 1):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def update_aliens(ai_settings, stat, screen, sb, ship, aliens, bullets):
    """Update the position of all the fleet
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Check colision alien-ship
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stat, screen, sb, ship, aliens, bullets)

    # Looks for aliens at the bottom on the screen
    check_aliens_bottom(ai_settings, stat, screen, sb, ship, aliens, bullets)


def check_fleet_edges(ai_settings, aliens):
    """Check if aliens are in the edges of the screen and change direction
    """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Change direction of the fleet
    """
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stat, screen, sb, ship, aliens, bullets):
    """Respond to ship being hit by aliens
    """
    if stat.ship_left > 0:
        # Decrement ship_left
        stat.ship_left -= 1

        # Update scoreboard
        sb.prep_ship()

        # Delete bullets and aliens
        bullets.empty()
        aliens.empty()

        # Create a new fleet and initian position of the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.ship_center()

        # Pause
        sleep(0.5)

    else:
        stat.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stat, screen, sb, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat that the same as if the ship got hit
            ship_hit(ai_settings, stat, screen, sb, ship, aliens, bullets)
            break


def check_high_score(stat, sb):
    """Check to see if there is a new high score
    """
    if stat.score > stat.high_score:
        stat.high_score = stat.score
        sb.prep_highscore()

def write_high_score(stat):
    arch = open ('highscore.txt','w')
    arch.write(str(stat.high_score))
    arch.close()

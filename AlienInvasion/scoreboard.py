import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard():
    """A class to report the scoring information
    """
    def __init__(self, ai_settings, screen, stat):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stat = stat

        # Font settings
        self.text_color = (230, 230, 230)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score image
        self.prep_score()
        self.prep_highscore()
        self.prep_level()
        self.prep_ship()

    def prep_score(self):
        """Turn the score into a rendered image
        """
        rounded_score = int(round(self.stat.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_highscore(self):
        rounded_highscore = int(round(self.stat.high_score, -1))
        highscore_str = "{:,}".format(rounded_highscore)
        self.highscore_image = self.font.render(highscore_str, True, self.text_color, self.ai_settings.bg_color)

        # Center the score at the top right of the screen
        self.highscore_rect = self.score_image.get_rect()
        self.highscore_rect.centerx = self.screen_rect.centerx
        self.highscore_rect.top = self.score_rect.top

    def prep_level(self):
        self.level_image = self.font.render(str(self.stat.level), True, self.text_color, self.ai_settings.bg_color)

        # Center the score at the top right of the screen
        self.level_rect = self.score_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10


    def prep_ship(self):
        """Show how many ships left
        """
        self.ships = Group()

        for ship_number in range(self.stat.ship_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.image = pygame.transform.scale(ship.image, (40, int(135*40/124)))
            ship.image_rect = ship.image.get_rect()
            ship.rect.x = 10 + ship_number * (ship.image_rect.width + 3)
            ship.rect.y = 10
            self.ships.add(ship)


    def draw_score(self):
        """Draw the score on the screen
        """
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.highscore_image, self.highscore_rect)
        self.screen.blit(self.level_image, self.level_rect)

        # Draw ships
        self.ships.draw(self.screen)
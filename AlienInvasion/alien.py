import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet
    """

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and get its rect.
        self.scale = 50
        self.path = 'images/8B.png'
        self.image = pygame.image.load(self.path)
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(
            self.image, (self.scale, int(self.rect.height*self.scale/self.rect.width)))
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height/3
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current position.
        """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Alien movement to the right
        """
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """Return True if alien is at edge of the screen
        """
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0

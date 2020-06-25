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
        self.image = pygame.image.load('images/8B.png')
        self.image = pygame.transform.scale(
            self.image, (50, int(232*50/182)))
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height/3
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current position.
        """
        self.screen.blit(self.image, self.rect)

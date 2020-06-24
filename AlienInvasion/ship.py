import pygame


class Ship():
    """The Ship class
    """

    def __init__(self, screen):
        """Initialize ship and set its starting position
        """
        self.screen = screen

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship3.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the ship at its current position.
        """
        self.screen.blit(self.image, self.rect)

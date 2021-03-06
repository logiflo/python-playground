import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """The Ship class
    """

    def __init__(self, ai_settings, screen):
        """Initialize ship and set its starting position
        """
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect.
        self.scale = 80
        self.path = 'images/ship3.png'
        self.image = pygame.image.load(self.path)
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(
            self.image, (self.scale, int(self.rect.height*self.scale/self.rect.width)))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value of the ship's center.
        self.center = float(self.rect.centerx)

        # Movement flag.
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw the ship at its current position.
        """
        self.screen.blit(self.image, self.rect)

    def update_moving(self):
        """Update the position of the ship based on the movement flag
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect object from self.center
        self.rect.centerx = self.center

    def ship_center(self):
        """Center the ship on the screen
        """
        self.center = self.screen_rect.centerx

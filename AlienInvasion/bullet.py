import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage the bullet fired from the ship
    """

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the current position of the ship
        """
        super().__init__()
        self.screen = screen

        # Create a bullet rect at (0, 0) and then set the correct position.
        self.rect = pygame.Rect(
            0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Create a bullet from an image
        self.image = pygame.image.load('images/mybullet.png')
        self.image = pygame.transform.scale(self.image, (15, 15))
        self.image_rect = self.image.get_rect()
        self.image_rect.centerx = ship.rect.centerx
        self.image_rect.top = ship.rect.top

        # Store the bullet position
        self.y = float(self.rect.y)
        self.image_y = float(self.image_rect.y)

        # Set the bullet color and speed
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen
        """
        # Update the postion of the bullet
        self.y -= self.speed_factor
        self.image_y -= self.speed_factor
        # Update de rect position
        self.rect.y = self.y
        self.image_rect.y = self.image_y

    def draw_bullet(self):
        """Draw the bullet on the screen
        """
        pygame.draw.rect(self.screen, self.color, self.rect)

    def blitbullet(self):
        self.screen.blit(self.image, self.image_rect)
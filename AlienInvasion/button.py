import pygame.font

class Button ():

    def __init__(self, ai_settings, screen, msg):
        """Initialize button attributes
        """
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimenensions and properties of the bottom
        self.width, self.height = 200, 50
        self.button_color = (130, 130, 130)
        self.text_color = (230, 230, 230)
        self.font = pygame.font.SysFont(None, 48)

        # Built the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button mesage needs to be prepped only one.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn the msg into a rendered image and center text on the button
        """
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


    def draw_button(self):
        """Draw blank button and then draw mesage
        """
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
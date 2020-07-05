class GameStats():
    """Track statistics for Alien Invasion
    """

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stat()
        #self.high_score = 0

        # Start Alien Invasion inactive
        self.game_active = False

    def reset_stat(self):
        """Initialize statistics that can change during the game
        """
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        arch = open ('highscore.txt','r')
        lectura = arch.read()
        self.high_score = int(lectura)
        arch.close()

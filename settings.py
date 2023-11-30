class Settings:
    """A class to store all settings for Snake Game."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Snake settings
        self.snake_speed = 15
        self.snake_color = (0, 255, 0)
        self.snake_size = 15

        # Food settings
        self.food_color = (255, 0, 0)
        self.food_size = 15
import pygame

class GameUI:
    """A class to manage game UI elements."""

    def __init__(self, screen, settings):
        """Initialize UI elements."""
        self.screen = screen
        self.settings = settings
        self.score = 0
        self.font = pygame.font.SysFont(None, 48)

    def show_score(self):
        """Draw the score to the screen."""
        score_str = str(self.score)
        score_image = self.font.render(score_str, True, (30, 30, 30))
        self.screen.blit(score_image, (20, 20))

    def show_start_screen(self):
        """Display the start screen."""
        # Implementation for the start screen goes here

    def show_game_over_message(self):
        """Display the game over message."""
        # Implementation for the game over message goes here
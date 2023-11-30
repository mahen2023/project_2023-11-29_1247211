import pygame
from pygame.sprite import Sprite
import random

class Food(Sprite):
    """A class to represent the food in the game."""

    def __init__(self, screen, game_settings):
        """Initialize the food and set its random position."""
        super(Food, self).__init__()
        self.screen = screen
        self.settings = game_settings
        self.color = game_settings.food_color
        self.size = game_settings.food_size
        self.rect = pygame.Rect(0, 0, self.size, self.size)
        self.place_food()

    def place_food(self):
        """Place the food in a random position on the screen."""
        self.rect.x = random.randint(0, self.settings.screen_width - self.size)
        self.rect.y = random.randint(0, self.settings.screen_height - self.size)

    def draw_food(self):
        """Draw the food to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
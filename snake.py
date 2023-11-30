import pygame
from pygame.sprite import Sprite

class Snake(Sprite):
    """A class to represent a single segment of the snake."""

    def __init__(self, screen, game_settings):
        """Initialize the snake and set its starting position."""
        super(Snake, self).__init__()
        self.screen = screen
        self.settings = game_settings
        self.segments = []
        self.create_snake()
        self.direction = pygame.K_RIGHT

    def create_snake(self):
        """Create a new snake with a few segments."""
        for i in range(3):
            self.add_segment((self.settings.screen_width / 2, self.settings.screen_height / 2))

    def add_segment(self, position):
        """Add a new segment to the snake at the given position."""
        segment = pygame.Rect(position[0], position[1], self.settings.snake_size, self.settings.snake_size)
        self.segments.append(segment)

    def update(self):
        """Update the position of the snake."""
        # Move all segments except the head
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].x = self.segments[i - 1].x
            self.segments[i].y = self.segments[i - 1].y
        # Move the head
        if self.direction == pygame.K_RIGHT:
            self.segments[0].x += self.settings.snake_size
        elif self.direction == pygame.K_LEFT:
            self.segments[0].x -= self.settings.snake_size
        elif self.direction == pygame.K_UP:
            self.segments[0].y -= self.settings.snake_size
        elif self.direction == pygame.K_DOWN:
            self.segments[0].y += self.settings.snake_size

    def draw_snake(self):
        """Draw the snake to the screen."""
        for segment in self.segments:
            pygame.draw.rect(self.screen, self.settings.snake_color, segment)

    def grow(self):
        """Increase the length of the snake."""
        tail = self.segments[-1]
        if self.direction == pygame.K_RIGHT:
            new_segment = pygame.Rect(tail.x - self.settings.snake_size, tail.y, self.settings.snake_size, self.settings.snake_size)
        elif self.direction == pygame.K_LEFT:
            new_segment = pygame.Rect(tail.x + self.settings.snake_size, tail.y, self.settings.snake_size, self.settings.snake_size)
        elif self.direction == pygame.K_UP:
            new_segment = pygame.Rect(tail.x, tail.y + self.settings.snake_size, self.settings.snake_size, self.settings.snake_size)
        elif self.direction == pygame.K_DOWN:
            new_segment = pygame.Rect(tail.x, tail.y - self.settings.snake_size, self.settings.snake_size, self.settings.snake_size)
        self.segments.append(new_segment)
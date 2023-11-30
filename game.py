import pygame
from settings import Settings
from snake import Snake
from food import Food
import game_functions as gf
from game_ui import GameUI

def run_game():
    # Initialize game and create a screen object
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Snake Game")

    # Create an instance of the GameUI, Snake, and Food
    game_ui = GameUI(screen, game_settings)
    snake = Snake(screen, game_settings)
    food = Food(screen, game_settings)

    # Start the main loop for the game
    while True:
        gf.check_events(snake)
        snake.update()
        gf.check_snake_food_collision(snake, food)
        gf.update_screen(game_settings, screen, snake, food, game_ui)

if __name__ == '__main__':
    run_game()
import sys
import pygame

def check_events(snake):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.direction != pygame.K_LEFT:
                snake.direction = pygame.K_RIGHT
            elif event.key == pygame.K_LEFT and snake.direction != pygame.K_RIGHT:
                snake.direction = pygame.K_LEFT
            elif event.key == pygame.K_UP and snake.direction != pygame.K_DOWN:
                snake.direction = pygame.K_UP
            elif event.key == pygame.K_DOWN and snake.direction != pygame.K_UP:
                snake.direction = pygame.K_DOWN

def check_snake_food_collision(snake, food):
    """Check for collisions between the snake and the food."""
    if snake.segments[0].colliderect(food.rect):
        food.place_food()
        snake.grow()

def update_screen(settings, screen, snake, food, game_ui):
    """Update images on the screen and flip to the new screen."""
    screen.fill(settings.bg_color)
    snake.draw_snake()
    food.draw_food()
    game_ui.show_score()
    pygame.display.flip()
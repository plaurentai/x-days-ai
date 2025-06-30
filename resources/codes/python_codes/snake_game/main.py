import pygame
import time
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH = 600
HEIGHT = 400
BLOCK_SIZE = 20
SPEED = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
LIGHT_DARK_BLUE = (30, 30, 60)

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game by ChatGPT")

clock = pygame.time.Clock()

# Score display
def show_score(score):
    value = score_font.render("Score: " + str(score), True, WHITE)
    screen.blit(value, [0, 0])

# Snake drawing
def draw_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], block_size, block_size])

# Game Over message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])

# Main function
def game_loop():
    game_over = False
    game_close = False

    x = WIDTH / 2
    y = HEIGHT / 2
    x_change = 0
    y_change = 0

    snake_list = []
    length_of_snake = 1

    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    while not game_over:

        while game_close:
            screen.fill(LIGHT_DARK_BLUE)
            message("Game Over! Press Q to Quit or C to Play Again", RED)
            show_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Movement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -BLOCK_SIZE
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = BLOCK_SIZE
                    x_change = 0

        # Check boundaries
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        x += x_change
        y += y_change
        screen.fill(LIGHT_DARK_BLUE)
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Self collision
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(BLOCK_SIZE, snake_list)
        show_score(length_of_snake - 1)

        pygame.display.update()

        # Eat food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            length_of_snake += 1

        clock.tick(SPEED)

    pygame.quit()
    quit()

# Start the game
game_loop()

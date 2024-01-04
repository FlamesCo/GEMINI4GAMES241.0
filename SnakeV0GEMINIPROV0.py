import pygame
import random
# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

# Snake settings
snake_block = 10
snake_speed = 15

# Snake initial position
snake_position = [screen_width // 2, screen_height // 2]
snake_body = [[snake_position[0], snake_position[1]]]

# Food position
food_position = [round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0,
                 round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0]

# Game over flag
game_over = False

# Clock for game speed
clock = pygame.time.Clock()

# Define font for text
font_style = pygame.font.SysFont(None, 30)

# Function to display score
def display_score(score):
    value = font_style.render("Your Score: " + str(score), True, white)
    screen.blit(value, [0, 0])

# Main game loop
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_position[0] -= snake_block
            elif event.key == pygame.K_RIGHT:
                snake_position[0] += snake_block
            elif event.key == pygame.K_UP:
                snake_position[1] -= snake_block
            elif event.key == pygame.K_DOWN:
                snake_position[1] += snake_block

    # Check for collisions with walls or snake itself
    if snake_position[0] < 0 or snake_position[0] >= screen_width or snake_position[1] < 0 or snake_position[1] >= screen_height or snake_position in snake_body[1:]:
        game_over = True

    # Update snake body
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        food_position = [round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0,
                         round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0]
    else:
        snake_body.pop()

    # Fill screen with black color
    screen.fill(black)

    # Draw snake
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], snake_block, snake_block))

    # Draw food
    pygame.draw.rect(screen, white, pygame.Rect(food_position[0], food_position[1], snake_block, snake_block))

    # Display score
    display_score(len(snake_body) - 1)

    # Update the screen
    pygame.display.update()

    # Set game speed
    clock.tick(snake_speed)

# Quit Pygame
pygame.quit()

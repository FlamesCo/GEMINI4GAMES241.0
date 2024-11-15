# Version: 1.0 and 1.1
# Pong4KPORTs the original Pong game to Pygame
# Importing the necessary modules
import pygame
import sys

# Initializing Pygame
pygame.init()

# Defining some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Setting up some constants
WIDTH = 400
HEIGHT = 300
BALL_RADIUS = 20
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60

# Setting up the display
win = pygame.display.set_mode((WIDTH, HEIGHT))

# Title of the window
pygame.display.set_caption("Pong Game")

# Paddle class
class Paddle(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)

    def draw(self, win):
        pygame.draw.rect(win, WHITE, self)

# Ball class
class Ball:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2

    def draw(self, win):
        pygame.draw.circle(win, WHITE, (self.x, self.y), BALL_RADIUS)

    def move(self, speed_x, speed_y):
        self.x += speed_x
        self.y += speed_y

# Initialize variables
clock = pygame.time.Clock()
fps = 60

paddle1 = Paddle(0, HEIGHT // 2 - PADDLE_HEIGHT // 2)
paddle2 = Paddle(WIDTH - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2)

ball = Ball()

speed_x = 5
speed_y = 5

# Initialize scores
score1 = 0
score2 = 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1.y -= 5
    if keys[pygame.K_s]:
        paddle1.y += 5
    if keys[pygame.K_UP]:
        paddle2.y -= 5
    if keys[pygame.K_DOWN]:
        paddle2.y += 5

    # Boundary check for paddles
    if paddle1.top < 0:
        paddle1.top = 0
    elif paddle1.bottom > HEIGHT:
        paddle1.bottom = HEIGHT

    if paddle2.top < 0:
        paddle2.top = 0
    elif paddle2.bottom > HEIGHT:
        paddle2.bottom = HEIGHT

    ball.move(speed_x, speed_y)

    # Collision check for paddles and balls
    if (ball.x <= paddle1.width and
            ball.y >= paddle1.top and
            ball.y <= paddle1.bottom):
        speed_x = -speed_x
    elif (ball.x + BALL_RADIUS >= WIDTH - paddle2.width and
          ball.y >= paddle2.top and
          ball.y <= paddle2.bottom):
        speed_x = -speed_x

    # Collision check for top and bottom walls
    if ball.y < 0 or ball.y > HEIGHT:
        speed_y = -speed_y

    # Collision check for left and right walls
    if (ball.x < 0 or ball.x + BALL_RADIUS > WIDTH):
        if ball.x < 0:
            score2 += 1
        else:
            score1 += 1
        ball.x = WIDTH // 2
        ball.y = HEIGHT // 2

    win.fill(BLACK)
    paddle1.draw(win)
    paddle2.draw(win)
    ball.draw(win)

    # Draw scores
    font = pygame.font.Font(None, 36)
    text1 = font.render(str(score1), True, WHITE)
    win.blit(text1, (WIDTH // 4, HEIGHT - 50))
    text2 = font.render(str(score2), True, WHITE)
    win.blit(text2, (WIDTH * 3 // 4, HEIGHT - 50))

    pygame.display.update()

    clock.tick(fps)

    # Prompt user to quit or continue
    if score1 == 5 or score2 == 5:
        print("Game over! Final scores: Player 1 -", score1, "Player 2 -", score2)
        run_game = False

print("Do you want to play again? (Y/N)")
play_again = input().upper()
if play_again == 'Y':
    # Reset game state
    score1 = 0
    score2 = 0
else:
    pygame.quit()
 #  sys.exit()

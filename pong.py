import pygame
import random

# Initialize pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_SIZE = 20
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
PADDLE_SPEED = 6
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

# Font for the score
font = pygame.font.SysFont("comicsansms", 36)

# Paddles and Ball
player_paddle = pygame.Rect(SCREEN_WIDTH - PADDLE_WIDTH - 10, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ai_paddle = pygame.Rect(10, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Initial ball speed and score
ball_speed_x = BALL_SPEED_X * random.choice((-1, 1))
ball_speed_y = BALL_SPEED_Y * random.choice((-1, 1))
player_score = 0
ai_score = 0

# AI movement function
def ai_movement():
    if ai_paddle.centery < ball.centery:
        ai_paddle.y += PADDLE_SPEED
    elif ai_paddle.centery > ball.centery:
        ai_paddle.y -= PADDLE_SPEED
    # Prevent the paddle from moving out of bounds
    ai_paddle.y = max(ai_paddle.y, 0)
    ai_paddle.y = min(ai_paddle.y, SCREEN_HEIGHT - PADDLE_HEIGHT)

# Ball movement function
def ball_movement():
    global ball_speed_x, ball_speed_y, player_score, ai_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with top and bottom walls
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y *= -1

    # Ball collision with paddles
    if ball.colliderect(player_paddle) or ball.colliderect(ai_paddle):
        ball_speed_x *= -1

    # Ball goes off the screen (scoring)
    if ball.left <= 0:
        player_score += 1
        reset_ball()
    if ball.right >= SCREEN_WIDTH:
        ai_score += 1
        reset_ball()

# Reset ball position and speed after scoring
def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    ball_speed_x *= random.choice((-1, 1))
    ball_speed_y *= random.choice((-1, 1))

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_paddle.top > 0:
        player_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player_paddle.bottom < SCREEN_HEIGHT:
        player_paddle.y += PADDLE_SPEED

    # Move AI paddle
    ai_movement()

    # Move ball
    ball_movement()

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.rect(screen, WHITE, ai_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))

    # Render the score
    player_text = font.render(str(player_score), True, WHITE)
    ai_text = font.render(str(ai_score), True, WHITE)
    screen.blit(player_text, (SCREEN_WIDTH // 2 + 20, 10))
    screen.blit(ai_text, (SCREEN_WIDTH // 2 - 40, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
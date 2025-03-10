import sys
import pygame


from pygame.examples.go_over_there import screen, running

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Теннис")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

clock = pygame.time.Clock()
fps = 60

paddle_width, paddle_height = 100, 10
paddle1_x = (screen_width - paddle_width)//2
paddle1_y = screen_height - paddle_height - 20
paddle1_speed = 6

paddle2_x = (screen_width - paddle_width)//2
paddle2_y = paddle_height + 20
paddle2_speed = 6

ball_radius = 8
ball_x = screen_width //2
ball_y = paddle1_y - ball_radius
ball_speed_x = 4
ball_speed_y = -4

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle1_x > 0:
        paddle1_x -= paddle1_speed

    if keys[pygame.K_RIGHT] and paddle1_x < screen_width-paddle_width:
        paddle1_x += paddle1_speed

    if keys[pygame.K_a] and paddle2_x > 0:
        paddle2_x -= paddle2_speed

    if keys[pygame.K_d] and paddle2_x < screen_width-paddle_width:
        paddle2_x += paddle2_speed

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_x <= 0 or ball_x >= screen_width:
        ball_speed_x = -ball_speed_x
    if ball_y <= 0:
        ball_speed_y = -ball_speed_y
    if ball_y >= screen_height:
        ball_x , ball_y = screen_width//2, screen_height//2
        ball_speed_y = -ball_speed_y

    if paddle1_x <= ball_x <= paddle1_x+paddle_width and paddle1_y <= ball_y+ball_radius <= paddle1_y + paddle_height:
        ball_speed_y = -ball_speed_y

    if paddle2_x <= ball_x <= paddle2_x+paddle_width and paddle2_y <= ball_y+ball_radius <= paddle2_y + paddle_height:
        ball_speed_y = -ball_speed_y

    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE,  (paddle1_x, paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (paddle2_x, paddle2_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, GREEN, (ball_x, ball_y), ball_radius)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
sys.exit()
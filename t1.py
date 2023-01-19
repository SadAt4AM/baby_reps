import pygame, sys, time, random

#Render setup
pygame.init()
width = 1200
height = 600
win1 = pygame.display.set_mode((width, height))
pygame.display.set_caption('My pong')
vel = 7
clock = pygame.time.Clock()
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

def ball_restart():
    global ball_speed_y, ball_speed_x
    ball.center = (width/2, height/2)
    ball_speed_y *=random.choice((1,-1))
    ball_speed_x *= random.choice((1, -1))

#Paddle 1
Paddle_1 = pygame.Rect(0, 0, 30, 100)
Paddle_1.centery = win1.get_height() / 2
Paddle_1.centerx = win1.get_width() - 1170

#Paddle 2
Paddle_2 = pygame.Rect(0, 0, 30, 100)
Paddle_2.centery = win1.get_height() / 2
Paddle_2.centerx = win1.get_width() - 30

#Ball
ball = pygame.Rect(width/2 - 15, height/2 - 15, 30, 30)
ball_speed_x = vel
ball_speed_y = vel


#Game loop
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
#Imput
    keys = pygame.key.get_pressed()
    Paddle_1.y += (keys[pygame.K_s] - keys[pygame.K_w]) * vel #wow
    Paddle_2.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * vel
#Ball speed

    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= width:
        ball_restart()
#Collisions
    if ball.colliderect(Paddle_1) or ball.colliderect(Paddle_2):
        ball_speed_x *= -1
#Draw
    win1.fill(bg_color)
    pygame.draw.rect(win1, (255, 255, 255), Paddle_1)
    pygame.draw.rect(win1, (255, 255, 255), Paddle_2)
    pygame.draw.ellipse(win1, (255, 255, 255), ball)
    pygame.draw.aaline(win1, light_grey, (width / 2, 0), (width / 2, height))
    pygame.display.flip()

pygame.quit()
exit()



import pygame
import sys
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

pygame.init()
clock = pygame.time.Clock()

screen_width = 1000
screen_height = 700

ball_speed_x = 5
ball_speed_y = 5
player1_speed = 0
player2_speed = 0

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')


ball = pygame.Rect(screen_width/2-15, screen_height/2-15, 30,30)
player1 = pygame.Rect(screen_width-20, screen_height/2-70, 10, 140)
player2 = pygame.Rect(10, screen_height/2 - 70, 10, 140)

bg_image = pygame.image.load(r'C:/Users/User/Downloads/ping-pong2.jpg')

def ball_details():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.left <= 0:
        print("Player1 won!!!")
        pygame.quit()

    elif ball.right >= screen_width:
        print("Player2 won!!!")
        pygame.quit()

    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1

    if ball.right == 0:
        print("You Lost")

def player1_details():
    player1.y += player1_speed

    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= screen_height:
        player1.bottom = screen_height

def player2_details():
    player2.y += player2_speed

    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= screen_height:
        player2.bottom = screen_height

while 1:

    screen.blit(bg_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player1_speed += 5
            if event.key == pygame.K_UP:
                player1_speed -= 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player1_speed -= 5
            if event.key == pygame.K_UP:
                player1_speed += 5


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player2_speed -= 5
            if event.key == pygame.K_s:
                player2_speed += 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player2_speed += 5
            if event.key == pygame.K_s:
                player2_speed -= 5


    ball_details()
    player1_details()
    player2_details()

    pygame.draw.rect(screen, (255,0,0), player1)
    pygame.draw.rect(screen, (255,0,0), player2)
    pygame.draw.ellipse(screen, (255,0,0), ball)


    pygame.display.update()
    clock.tick(60)


pygame.quit()

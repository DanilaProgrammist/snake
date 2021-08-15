import pygame
import random
import sys
import time

width = 600
heigh = 600
blue = (0,0,255)
snake = (0, 255, 0)
moon_field = (255, 255, 255)
score_clr = (0,0,0)
text_color = (255,0,0)
food_color = (255,0,0)
first_time = pygame.time.get_ticks()
score = 0
snake_blok = 10

pygame.font.init()
pygame.init()
screen = pygame.display.set_mode((width, heigh))
pygame.display.update()
pygame.display.set_caption("Snake")
game_over = False
#x_pos = round(random.randint(0, width))
#y_pos = round(random.randint(0, heigh))
snake_headx_pos = width/2
snake_heady_pos = heigh/2

food_x_pos = round(random.randint(0, width - snake_blok)/10.0)*10.0
food_y_pos = round(random.randint(0, heigh - snake_blok)/10.0)*10.0

x_new = 0
y_new = 0
fps = pygame.time.Clock()
last_down = None
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont("Arial", 35)


def our_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, snake, [x[0], x[1], 30, 30])

def our_score(score):
    val = score_font.render("Счёт: "+ str(score), True,blue)
    screen.blit(val, [0,0])

def message(msg, color):
    msg_text = font_style.render(msg, True, color)
    screen.blit(msg_text, [230, 230])
while not game_over:
    snake_list = []
    snake_len = 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key == pygame.K_LEFT and last_down != "right":
                x_new = -10
                y_new = 0
                last_down = "left"
            elif event.key == pygame.K_RIGHT and last_down != "left":
                x_new = 10
                y_new = 0
                last_down = "right"
            elif event.key == pygame.K_UP and last_down != "down":
                x_new = 0
                y_new = -10
                last_down = "up"
            elif event.key == pygame.K_DOWN and last_down != "up":
                x_new = 0
                y_new = 10
                last_down = "down"
    snake_headx_pos= snake_headx_pos + x_new
    snake_heady_pos = snake_heady_pos + y_new
    screen.fill(moon_field)
    pygame.draw.rect(screen, snake, [snake_headx_pos, snake_heady_pos, 30, 30])
    food = pygame.draw.rect(screen, food_color, [food_x_pos, food_y_pos, 30, 30])
    pygame.display.update()
    our_score(score)
    PERSONNEL_COUNT = 25
    if snake_headx_pos >= width or snake_headx_pos < 0 or snake_heady_pos >= heigh or snake_heady_pos < 0:
        game_over = True
    snake_Head = []
    snake_Head.append(snake_headx_pos)
    snake_Head.append(snake_heady_pos)
    if len(snake_list) > snake_len:
        del snake_list[0]
    if snake_headx_pos == food_x_pos and snake_heady_pos == food_y_pos:
        food_x_pos = round(random.randint(0, width - snake_blok) / 10.0) * 10.0
        food_y_pos = round(random.randint(0, heigh - snake_blok) / 10.0) * 10.0
        snake_len = snake_len + 1
        score = score + 1
        PERSONNEL_COUNT = PERSONNEL_COUNT + 1
        our_snake(snake_list)
        print("НЯМ!!!")
    fps.tick(PERSONNEL_COUNT)

message("Вы ЛОХ!!!", text_color)
pygame.display.update()
time.sleep(2)
pygame.quit()
quit()




import pygame
import random

pygame.init()

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)
yellow = (255, 255, 155)

x = 600
y = 400

dis = pygame.display.set_mode((x, y))
pygame.display.set_caption("Snake")

game_over = False

x1 = x / 2
y1 = y / 2

x1_change = 0
y1_change = 0

snake_List = []
Length_of_snake = 1

clock = pygame.time.Clock()

snake_block = 10

score_font = pygame.font.SysFont("comicsansms", 35)


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, blue)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for i in snake_list:
        pygame.draw.rect(dis, black, [i[0], i[1], snake_block, snake_block])


foodx = round(random.randrange(0, x - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, y - snake_block) / 10.0) * 10.0

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -snake_block
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = snake_block

    if x1 >= x or x1 < 0 or y1 >= y or y1 < 0:
        game_over = True

    x1 += x1_change
    y1 += y1_change
    dis.fill(yellow)

    pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
    snake_Head = []
    snake_Head.append(x1)
    snake_Head.append(y1)
    snake_List.append(snake_Head)
    if len(snake_List) > Length_of_snake:
        del snake_List[0]

    for j in snake_List[:-1]:
        if j == snake_Head:
            game_over = True

    our_snake(snake_block, snake_List)
    Your_score(Length_of_snake - 1)

    pygame.display.update()

    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, x - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, y - snake_block) / 10.0) * 10.0
        Length_of_snake += 1

    clock.tick(15)

pygame = quit()
quit()

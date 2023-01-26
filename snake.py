import random
from time import sleep
import pygame

resolution = 800
size = 50

x, y = random.randrange(0, resolution - size, size), random.randrange(0, resolution - size, size)
x_apple, y_apple = random.randrange(0, resolution - size, size), random.randrange(0, resolution - size, size)

snake = [(x, y)]
length = 1
dir_x = 0
dir_y = 0

speed = 0.11
pygame.init()
screen = pygame.display.set_mode([resolution, resolution])
clock = pygame.time.Clock()

score = 0

my_font = pygame.font.SysFont('Comic Sans MS', 30)

while True:
    screen.fill(pygame.Color('pink'))
    text_surface = my_font.render(f'Score: {score}', False, (0, 0, 0))
    screen.blit(text_surface, (0, 0))
    for i, j in snake:
        pygame.draw.rect(screen, pygame.Color('blue'), (i, j, size, size))
    pygame.draw.rect(screen, pygame.Color('red'), (x_apple, y_apple, size, size))
    pygame.display.flip()

    x += size * dir_x
    y += size * dir_y
    snake.append((x, y))

    snake = snake[-length:]
    sleep(speed)
    keyword = pygame.key.get_pressed()
    if keyword[pygame.K_w] and dir_y != 1:
        dir_x = 0
        dir_y = -1
    elif keyword[pygame.K_s] and dir_y != -1:
        dir_x = 0
        dir_y = 1
    elif keyword[pygame.K_d] and dir_x != -1:
        dir_x = 1
        dir_y = 0
    elif keyword[pygame.K_a] and dir_x != 1:
        dir_x = -1
        dir_y = 0
    if x == x_apple and y == y_apple:
        length += 1
        speed -= 0.005
        score += 1
        x_apple, y_apple = random.randrange(0, resolution - size, size), random.randrange(0, resolution - size, size)
        if (x_apple, y_apple) in snake:
            x_apple, y_apple = random.randrange(0, resolution - size, size), random.randrange(0, resolution - size, size)

    if (x < 0) or (y < 0) or (x > resolution - size) or (y > resolution - size) or len(snake) != len(set(snake)):
        text_surface1 = my_font.render('You lose!', False, (0, 0, 0))
        screen.blit(text_surface1, (350, 350))
        pygame.display.flip()
        sleep(2)
        exit()
    for el in pygame.event.get():
        if el.type == pygame.QUIT:
            exit()
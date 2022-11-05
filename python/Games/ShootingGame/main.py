import pygame
import object
import math

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

SIZE = [600, 600]

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Shooting Game")

playing = True
clock = pygame.time.Clock()

player = object.Player(300, 500, 30, 30, GREEN, 5)

bullets = []

enemy = object.Box(200, 200, 30, 30, RED, 5)

while playing:

    clock.tick(120)

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        playing = False

    if event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()

        bullet = object.Bullet(player.center_x, player.center_y, 4, 4, BLACK, 10)

        bullet.set_direction(pos[0], pos[1])
        bullets.append(bullet)

    player.move(pygame.key.get_pressed(), screen.get_size())

    screen.fill(WHITE)
    player.draw(screen)

    for bullet in bullets:
        bullet.move()
        bullet.draw(screen)

    bullets = list(filter(lambda b: b.check_hit_wall(screen), bullets))

    enemy.draw(screen)

    pygame.display.update()

    for bullet in bullets:
        if bullet.check_collision(enemy):
            playing = False

pygame.quit()

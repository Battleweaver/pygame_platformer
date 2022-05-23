import sys
import time
import pygame
from pygame.locals import *
from constants import *
from sprite_groups import P1, all_sprites, platforms, plat_gen

pygame.init()

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

# Game Loop
while True:

    if P1.rect.top > HEIGHT:
        for entity in all_sprites:
            entity.kill()
            time.sleep(1)
            displaysurface.fill((255,0,0))
            time.sleep(2)
            pygame.display.update()
            pygame.quit()
            sys.exit()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                P1.jump(platforms)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                P1.jump_cancel()

    if P1.rect.top <= HEIGHT / 3:
        P1.pos.y += abs(P1.vel.y)
        for plat in platforms:
            plat.rect.y += abs(P1.vel.y)
            if plat.rect.top >= HEIGHT:
                plat.kill()

    displaysurface.fill((0, 0, 0))
    P1.move()
    P1.update(platforms)
    plat_gen()
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)

    score_font = pygame.font.SysFont("Verdana", 20)
    score_display = score_font.render(str(P1.score), True, (123, 255, 0))
    displaysurface.blit(score_display, (WIDTH / 2, 10))

    pygame.display.update()
    FramePerSec.tick(FPS)

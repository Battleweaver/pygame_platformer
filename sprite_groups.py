import random

import pygame

from constants import WIDTH, HEIGHT
from ground_platform import GroundPlatform
from player import Player

P1 = Player()
PT1 = GroundPlatform()

PT1.surf = pygame.Surface((WIDTH, 20))
PT1.surf.fill((240, 200, 0))
PT1.rect = PT1.surf.get_rect(center=(WIDTH / 2, HEIGHT - 10))
PT1.point = False

all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)

platforms = pygame.sprite.Group()
platforms.add(PT1)


def check(platform, groupies):
    if pygame.sprite.spritecollideany(platform, groupies):
        return True
    else:
        for entity in groupies:
            if entity == platform:
                continue
            if abs(platform.rect.top - entity.rect.bottom) < 40 and abs(platform.rect.bottom - entity.rect.top) < 40:
                return True
        return False


for x in range(random.randint(5, 6)):
    check_platform = True
    pl = GroundPlatform()
    while check_platform:
        pl = GroundPlatform()
        check_platform = check(pl, platforms)

    platforms.add(pl)
    all_sprites.add(pl)


def plat_gen():
    while len(platforms) < 7:
        check_gened_platform = True
        gap_width = random.randrange(50, 100)
        pl = GroundPlatform()

        while check_gened_platform:
            pl = GroundPlatform()
            pl.rect.center = (random.randrange(0, WIDTH - gap_width),
                              random.randrange(-50, 0))
            check_gened_platform = check(pl, platforms)

        platforms.add(pl)
        all_sprites.add(pl)

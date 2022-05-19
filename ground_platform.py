import random

import pygame.sprite
from constants import WIDTH, HEIGHT


class GroundPlatform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((random.randint(50, 100), 15))
        self.surf.fill((238, 255, 0))
        self.rect = self.surf.get_rect(center=(random.randint(0, WIDTH-10), random.randint(0, HEIGHT - 30)))

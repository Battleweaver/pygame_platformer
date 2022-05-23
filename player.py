import pygame.sprite
from constants import ACC, FRIC, WIDTH, vec
from pygame.locals import K_LEFT, K_RIGHT


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((123, 167, 82))
        self.rect = self.surf.get_rect(center=(25, 415))

        self.pos = vec((10, 385))
        self.vel = vec((0, 0))
        self.acc = vec((0, 0))

        self.jumping = False
        self.score = 0

    def move(self):
        self.acc = vec((0, 0.5))

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos

    def jump(self, platforms):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = -15

    def jump_cancel(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3

    def update(self, platforms):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if self.vel.y > 0:
            if hits:
                if self.pos.y < hits[0].rect.bottom:
                    if hits[0].point == True:
                        hits[0].point = False
                        self.score += 1

                    self.jumping = False
                    self.pos.y = hits[0].rect.top + 1
                    self.vel.y = 0

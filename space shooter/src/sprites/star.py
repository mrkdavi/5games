import pygame
from random import randint

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

class Star(pygame.sprite.Sprite):
  def __init__(self, groups, star_surf):
    super().__init__(groups)
    self.image = star_surf
    self.rect = self.image.get_frect(center = (randint(1, WINDOW_WIDTH), randint(1,WINDOW_HEIGHT)))
    self.speed = 600

  def update(self, dt, surf, surf_2, sprites, sound):
      self.rect.centery += self.speed * dt

      if self.rect.top > WINDOW_HEIGHT:
        self.rect = self.image.get_frect(midbottom = (randint(1, WINDOW_WIDTH), 0))
import pygame
from random import randint, uniform

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

class Meteor(pygame.sprite.Sprite):
  def __init__(self, surf, pos, groups):
    super().__init__(groups)
    self.original_surf = surf
    self.image = self.original_surf
    self.rect = self.image.get_frect(midbottom = pos)
    self.direction = pygame.Vector2(uniform(-0.5, 0.5), 1)
    self.speed = randint(400, 500)
    self.rotate = 0
    self.rotate_speed = randint(50, 100)
 
  def update(self, dt, surf, surf_2, sprites, sound):
    self.rect.center += self.direction * self.speed * dt

    # rotate
    self.rotate += self.rotate_speed * dt
    self.image = pygame.transform.rotozoom(self.original_surf, self.rotate, 1)
    self.rect = self.image.get_frect(midbottom = self.rect.midbottom)

    if self.rect.top > WINDOW_HEIGHT:
      self.kill()

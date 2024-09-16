import pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

class Laser(pygame.sprite.Sprite):
  def __init__(self, surf, pos, groups):
    super().__init__(groups)
    self.image = surf
    self.rect = self.image.get_frect(midbottom = pos)
    self.speed = 600
 
  def update(self, dt, surf, surf_2, sprites, sound):
    recent_keys = pygame.key.get_pressed()
    if recent_keys[pygame.K_f] and self.speed == 10:
      self.speed = 600
    if recent_keys[pygame.K_e] and self.speed == 600:
      self.speed = 10

    self.rect.centery -= self.speed * dt

    if self.rect.bottom < 0:
      self.kill()

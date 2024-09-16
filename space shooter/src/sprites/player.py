import pygame
from os.path import join
from src.sprites.laser import Laser

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

class Player(pygame.sprite.Sprite):
  def __init__(self, groups, p2 = False):
    super().__init__(groups)
    self.groups = groups
    self.original_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
    self.image = self.original_surf
    self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 4 * 3))
    self.direction = pygame.math.Vector2()
    self.speed = 500
    self.p2 = p2

    #cooldown
    self.can_shoot = True
    self.laser_shoot_time = 0
    self.cooldown_duration = 400
    self.image = pygame.transform.rotate(self.image, 360)

    #mask
    self.mask = pygame.mask.from_surface(self.image)

  def laser_timer(self):
    if not self.can_shoot:
      current_time = pygame.time.get_ticks()
      if current_time - self.laser_shoot_time >= self.cooldown_duration:
        self.can_shoot = True

  def update(self, dt, laser_surface, meteor_surface, laser_sprites, laser_sound):
    up = pygame.K_UP if self.p2 else pygame.K_w
    down = pygame.K_DOWN if self.p2 else pygame.K_s
    left = pygame.K_LEFT if self.p2 else pygame.K_a
    right = pygame.K_RIGHT if self.p2 else pygame.K_d

    keys = pygame.key.get_pressed()
    self.direction.x = int(keys[right]) - int(keys[left])
    self.direction.y = int(keys[down]) - int(keys[up])
    self.direction = self.direction.normalize() if self.direction else self.direction
    self.rect.center += self.direction * self.speed * dt

    recent_keys = pygame.key.get_pressed()
    
    if recent_keys[pygame.K_SPACE] and self.can_shoot:
      Laser(laser_surface, self.rect.midtop, (self.groups, laser_sprites))
      self.can_shoot = False
      self.laser_shoot_time = pygame.time.get_ticks()
      laser_sound.play()
    
    
    self.laser_timer()

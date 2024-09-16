import pygame


class AnimatedExplosion(pygame.sprite.Sprite):
    def __init__(self, frames, pos, groups):
        super().__init__(groups)
        self.frames = frames
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_frect(center = pos)

    def update(self, dt, surf, surf_2, sprites, sound):
      if self.frame_index >= len(self.frames) -1:
        self.kill()

      self.image = self.frames[int(self.frame_index) % len(self.frames)]
      self.frame_index += 75 * dt
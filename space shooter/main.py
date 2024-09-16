import pygame
from os.path import join
from src.sprites.player import Player
from src.sprites.star import Star
from src.sprites.meteor import Meteor
from src.sprites.animated_explosion import AnimatedExplosion
from random import randint

def collisions():
  global running
  global meteor_destroyed

  if pygame.sprite.spritecollide(player, meteor_sprites, False, pygame.sprite.collide_mask):
    print('Game Over!')
    # damage_sound.play()
    running = False

  for laser in laser_sprites:
    if pygame.sprite.spritecollide(laser, meteor_sprites, True):
      laser.kill()
      AnimatedExplosion(explosion_frames, laser.rect.midtop, all_sprites)
      explosion_sound.play()
      meteor_destroyed += 1

meteor_destroyed = 0

def display_score():
  global meteor_destroyed

  current_time = pygame.time.get_ticks() // 1000
  text_surf = font.render(str((meteor_destroyed*100) + (current_time*10)), True, (222, 222, 222))
  text_rect = text_surf.get_frect(midbottom = (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 50))
  display_surface.blit(text_surf, text_rect)
  pygame.draw.rect(display_surface, 'white',  text_rect.inflate(30, 10).move(0, -5), 3, 10)

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space Shooter')
pygame.display.set_icon(pygame.image.load(join('images','player.png')))

running = True

clock = pygame.time.Clock()

# imports
star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
meteor_surf = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
laser_surf = pygame.image.load(join('images', 'laser.png')).convert_alpha()
font = pygame.font.Font(join('images', 'Oxanium-Bold.ttf'), 36)
explosion_frames = [pygame.image.load(join('images', 'explosion', f'{i}.png')).convert_alpha() for i in range(21)]

pygame.mixer.init()
laser_sound = pygame.mixer.Sound(join('audio', 'laser.wav'))
explosion_sound = pygame.mixer.Sound(join('audio', 'explosion.wav'))
damage_sound = pygame.mixer.Sound(join('audio', 'damage.ogg'))
game_music = pygame.mixer.Sound(join('audio', 'game_music.wav'))

game_music.set_volume(0.1)
laser_sound.set_volume(0.2)
explosion_sound.set_volume(0.2)

game_music.play(-1)

# sprites
all_sprites = pygame.sprite.Group()
meteor_sprites = pygame.sprite.Group()
laser_sprites = pygame.sprite.Group()

for i in range(40):
  Star(all_sprites, star_surf)
player = Player(all_sprites)
# player2 = Player(all_sprites, True)

# custom events -> meteor event
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 800)

while running:
  dt = clock.tick(120) / 1000
  
  # event loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == meteor_event:
      Meteor(meteor_surf, (randint(1, WINDOW_WIDTH), -300), (all_sprites, meteor_sprites))
      
  
  # update
  all_sprites.update(dt, laser_surf, meteor_surf, laser_sprites, laser_sound)

  collisions()

  # draw the game
  display_surface.fill('#3a2e3f')
  all_sprites.draw(display_surface)
  
  display_score()

  pygame.display.update()

pygame.quit()
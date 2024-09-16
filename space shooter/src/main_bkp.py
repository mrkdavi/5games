import pygame
from os.path import join
from random import randint

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space Shooter')

running = True

clock = pygame.time.Clock()


# plain surface
surf = pygame.Surface((100, 200))
surf.fill('purple')
surf_x, surf_y = 100, 150

# player surface image
player_sprite_path = join('images', 'player.png')
player_surface = pygame.image.load(player_sprite_path).convert_alpha()
player_rect = player_surface.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 4 * 3) )
player_x, player_y = 100, 150
player_direction = pygame.math.Vector2(0, 0)
player_speed = 500

def get_sign():
  sign = randint(0, 1)
  return 1 if sign else -1


# meteor surface image
meteor_x, meteor_y = 100, 150
meteor_sprite_path = join('images', 'meteor.png')
meteor_surface = pygame.image.load(meteor_sprite_path).convert_alpha()
meteor_rect = meteor_surface.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
meteor_direction = pygame.math.Vector2(-2, 3)
meteor_speed = 200
meteors_direction = [pygame.math.Vector2(2 * get_sign(), 3 * get_sign()) for i in range(5)]
meteors_positions = [pygame.math.Vector2(randint(0, WINDOW_WIDTH), randint(0,WINDOW_HEIGHT)) for i in range(5)]

# laser surface image
laser_x, laser_y = 100, 150
laser_sprite_path = join('images', 'laser.png')
laser_surface = pygame.image.load(laser_sprite_path).convert_alpha()
laser_rect = laser_surface.get_frect(bottomleft = player_rect.center)
laser_direction = pygame.math.Vector2(0, -1)
laser_speed = 900
lasers_positions = []

# star surface image
star_x, star_y = [], []
star_sprite_path = join('images', 'star.png')
star_surface = pygame.image.load(star_sprite_path).convert_alpha()
star_rect = star_surface.get_frect(bottomleft = player_rect.center)
star_direction = pygame.math.Vector2(0, 1)
star_speed = 500
stars_positions = [pygame.math.Vector2(randint(1, WINDOW_WIDTH), randint(1,WINDOW_HEIGHT)) for i in range(40)]


while running:
  dt = clock.tick(60) / 1000
  display_surface.fill('gray12')
# event loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
      lasers_positions.append(pygame.Vector2(player_rect.center))
  
  # input
  # player_rect.center = pygame.mouse.get_pos()
  keys = pygame.key.get_pressed()

  player_direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
  player_direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])

  if player_rect.top < 0:
    player_rect.top = 0
  if player_rect.bottom > WINDOW_HEIGHT:
    player_rect.bottom = WINDOW_HEIGHT
  if player_rect.right > WINDOW_WIDTH:
    player_rect.right = WINDOW_WIDTH
  if player_rect.left < 0:
    player_rect.left = 0

  player_direction = player_direction.normalize() if player_direction else player_direction

  player_rect.center += player_direction * player_speed * dt


  # print((player_direction * player_speed).magnitude())

  # draw the game
  
  # if keys[pygame.K_SPACE]:
  #   lasers_positions.append(pygame.Vector2(player_rect.center))

  # for index, position in meteors_positions:
  #   display_surface.blit(meteor_surface, position)
  #   position += meteors_direction[index] * meteor_speed * dt
  for index, position in enumerate(meteors_positions):
    # Desenhe o meteoro na posição atual
    display_surface.blit(meteor_surface, position)
    
    # Atualize a posição com base na direção e velocidade
    position += meteors_direction[index] * meteor_speed * dt
    
    # Atualize a posição na lista original (opcional, dependendo do seu caso)
    meteors_positions[index] = position
    if meteors_positions[index].x > WINDOW_WIDTH :
      meteors_positions[index].x = WINDOW_WIDTH
      meteors_direction[index].x *= -1

    if meteors_positions[index].x < 0:
      meteors_positions[index].x = 0
      meteors_direction[index].x *= -1

    if meteors_positions[index].y > WINDOW_HEIGHT:
      meteors_positions[index].y = WINDOW_HEIGHT
      meteors_direction[index].y *= -1

    if meteors_positions[index].y < 0:
      meteors_positions[index].y = 0
      meteors_direction[index].y *= -1

  for position in lasers_positions:
    display_surface.blit(laser_surface, position)
    position += laser_direction * laser_speed * dt

  for position in stars_positions:
    display_surface.blit(star_surface, position)
    position += star_direction * star_speed * dt
    if position.y > WINDOW_HEIGHT:
      position.y = 0
      position.x = randint(1, WINDOW_WIDTH)

  # display_surface.blit(meteor_surface, meteor_rect)
  display_surface.blit(player_surface, player_rect)

  # player movement

  # meteor movement
  meteor_rect.center += meteor_speed * meteor_direction * dt

  

  pygame.display.update()

pygame.quit()  
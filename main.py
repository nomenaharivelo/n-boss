import pygame, sys

pygame.init()

size = (500, 500)

screen = pygame.display.set_mode(size)

while 1:
  for evt in pygame.event.get():
    if evt.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

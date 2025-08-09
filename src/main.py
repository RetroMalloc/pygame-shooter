import pygame, sys

pygame.init()

display_surface = pygame.display.set_mode((1280, 720))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    display_surface.fill('white')

    pygame.display.update()
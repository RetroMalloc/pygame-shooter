import pygame, sys

pygame.init()

display_surface = pygame.display.set_mode((1280, 720))

background_surface = pygame.image.load("assets/background.png").convert_alpha()
stall_surface = pygame.image.load("assets/stall.png").convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    display_surface.fill('white')

    display_surface.blit(background_surface)

    display_surface.blit(stall_surface)

    pygame.display.update()
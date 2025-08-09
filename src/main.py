import pygame, sys

pygame.init()

display_surface = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

crosshair_surface = pygame.image.load("assets/crosshair.png").convert_alpha()
crosshair_rect = crosshair_surface.get_frect()

background_surface = pygame.image.load("assets/background.png").convert_alpha()
stall_surface = pygame.image.load("assets/stall.png").convert_alpha()

while True:
    deltaTime = clock.tick() / 1000
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    display_surface.fill('white')

    display_surface.blit(background_surface)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    crosshair_rect.centerx = mouse_x
    crosshair_rect.centery = mouse_y
    display_surface.blit(crosshair_surface, crosshair_rect)

    display_surface.blit(stall_surface)

    pygame.display.update()
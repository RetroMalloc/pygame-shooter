import pygame, sys

from random import choice, randint

pygame.init()

score = 0

font = pygame.font.Font(None, 40)

display_surface = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

duck_surface = pygame.image.load("assets/duck.png").convert_alpha()
ducks = []
duck_timer = pygame.USEREVENT + 1
pygame.time.set_timer(duck_timer, 1000)

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
        if event.type == duck_timer:
            duck_x, duck_y = choice([-40, 1280 + 40]), randint(350, 500)
            duck_rect = duck_surface.get_frect(center = (duck_x, duck_y))

            if duck_x == -40:
                duck_direction = pygame.math.Vector2(1, 0)
            else:
                duck_direction = pygame.math.Vector2(-1, 0)
            
            duck_speed = randint(200, 600)

            ducks.append({
                'rect': duck_rect,
                'direction': duck_direction,
                'speed': duck_speed,
                'kill': False
            })
    
    display_surface.fill('white')

    display_surface.blit(background_surface)

    if ducks:
        for duck in ducks:
            duck['rect'].center += duck['direction'] * duck['speed'] * deltaTime
            
            if duck['direction'].x == 1:
                display_surface.blit(duck_surface, duck['rect'])
            else:
                display_surface.blit(pygame.transform.flip(duck_surface, True, False), duck['rect'])

        ducks = [duck for duck in ducks if -100 <= duck['rect'].x < 1280 + 100]

    mouse_x, mouse_y = pygame.mouse.get_pos()
    crosshair_rect.centerx = mouse_x
    crosshair_rect.centery = mouse_y
    display_surface.blit(crosshair_surface, crosshair_rect)

    if ducks:
        mouse_click = pygame.mouse.get_pressed()[0]
        for duck in ducks:
            if not mouse_click:
                continue
            
            if duck['rect'].collidepoint(crosshair_rect.center):
                duck['kill'] = True
                score += 1
        
        ducks = [duck for duck in ducks if not duck['kill']]

    display_surface.blit(stall_surface)

    text_surf = font.render(f'Your score: {score}', True, 'White')
    text_rect = text_surf.get_rect(center = (1280 / 2, 20))
    display_surface.blit(text_surf, text_rect)

    pygame.display.update()
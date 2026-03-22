

import pygame

pygame.init()

WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))

zone_rect1 = pygame.Rect(0, 0, 50, 100)  # x=50, y=100, 100px large, 20px haut

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        print(pygame.event.event_name(event.type))
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), zone_rect1)  # rectangle rouge
    pygame.display.flip()

pygame.quit()




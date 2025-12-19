import pygame

def deplacement():
    x = 400
    y = 300
    speed = 1
    size = 40

    keys = pygame.key.get_pressed()

    if keys[pygame.K_z]:  # haut
        y -= speed
    if keys[pygame.K_s]:  # bas
        y += speed
    if keys[pygame.K_q]:  # gauche
        x -= speed
    if keys[pygame.K_d]:  # droite
        x += speed

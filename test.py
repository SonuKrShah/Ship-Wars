import pygame
WIN = pygame.display.set_mode((600, 700))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        print("Lu Naz")

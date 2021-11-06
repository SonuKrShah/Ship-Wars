import pygame

WIN = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Ship Wars")
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

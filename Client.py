import pygame
from Network import Network
from Player import Player
import os

# Setting up the pygame window.

# Variables and Values.
WIDTH = 450
HEIGHT = 300
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BORDER = (WIDTH//2 - 4, 0, 8, HEIGHT)
SPACE = pygame.image.load(os.path.join('Assets', 'background2.jpg'))
SPACE = pygame.transform.scale(SPACE, (WIDTH, HEIGHT))


# Setting the window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ship Wars")

clientNumber = 0


def redrawWindow(WIN, player, p2):
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    player.draw(WIN)
    p2.draw(WIN)
    pygame.display.update()


def main():
    run = True
    n = Network()
    p = n.get_p()
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        p2 = n.send(p)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                p.SetDefaults()
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    p.Handle_Bullets()
        p.move(WIDTH, HEIGHT)

        redrawWindow(WIN, p, p2)
    pygame.quit()


main()

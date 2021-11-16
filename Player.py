import pygame


class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (self.x, self.y, self.width, self.height)
        self.vel = 3
        self.bullet_color = (255, 255, 0)
        self.bullet_speed = 8
        self.bullets = []
        self.health = 10

    def SetDefaults(self):
        self.bullets = []
        self.health = 10

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
        for bullet in self.bullets:
            pygame.draw.rect(win, self.bullet_color, bullet)

    def updateRect(self):
        self.rect = (self.x, self.y, self.width, self.height)

    def Handle_Bullets(self):
        if len(self.bullets) < 3:
            bullet = pygame.Rect(
                self.x, self.y + self.height//2 - 2, 10, 5)
            self.bullets.append(bullet)

    def LeftPlayer(self, width, height):
        for bullet in self.bullets:
            bullet.x += self.bullet_speed
        keys = pygame.key.get_pressed()
        # Also handling the corner conditions
        if keys[pygame.K_LEFT] and self.x - self.vel > 0:
            self.x -= self.vel
        if keys[pygame.K_RIGHT] and self.x + self.width + self.vel + 5 < width // 2:
            self.x += self.vel
        if keys[pygame.K_UP] and self.y - self.vel > 0:
            self.y -= self.vel
        if keys[pygame.K_DOWN] and self.y + self.height + self.vel < height:
            self.y += self.vel

    def RightPlayer(self, width, height):
        keys = pygame.key.get_pressed()
        # Also handling the corner conditions
        if keys[pygame.K_LEFT] and self.x - self.vel - 5 > width//2:
            self.x -= self.vel
        if keys[pygame.K_RIGHT] and self.x + self.width + self.vel < width:
            self.x += self.vel
        if keys[pygame.K_UP] and self.y - self.vel > 0:
            self.y -= self.vel
        if keys[pygame.K_DOWN] and self.y + self.height + self.vel < height:
            self.y += self.vel

        for bullet in self.bullets:
            bullet.x -= self.bullet_speed

    def move(self, width, height):
        if self.x > width//2:
            self.RightPlayer(width, height)
        else:
            self.LeftPlayer(width, height)
        self.updateRect()

import pygame
import random
pygame.init()

r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)

red = [r,g,b]
lBlue = [153, 204, 255]

screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Klaviatuuriga juhtimine")
screen.fill(lBlue)
clock = pygame.time.Clock()

ristkülik = pygame.Rect(10, 10, 640, 100)
pygame.draw.rect(screen, red, ristkülik)

posX, posY = screenX/2, screenY/2
speedX, speedY = 0, 0
gameover = False
while not gameover:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            posX, posY = pygame.mouse.get_pos()

    ruut = pygame.draw.rect(screen, red, [posX, posY, 30, 30])
    pygame.display.flip()
    screen.fill(lBlue)

pygame.quit()

import pygame
import random

pygame.init()

r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)

red = [r, g, b]
lBlue = [153, 204, 255]
black = [0, 0, 0]

screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Klaviatuuriga ja hiirega juhtimine")
screen.fill(lBlue)

clock = pygame.time.Clock()

ristkülik = pygame.Rect(10, 10, 640, 100)
pygame.draw.rect(screen, red, ristkülik)

posX, posY = screenX / 2, screenY / 2
speedX, speedY = 0, 0
directionX, directionY = 0, 0

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    mouseX, mouseY = pygame.mouse.get_pos()
    posX, posY = mouseX, mouseY

    if pygame.Rect(posX, posY, 30, 30).colliderect(ristkülik):
        if posY + 15 < ristkülik.top + 5:
            posY = ristkülik.top - 30
        elif posY + 15 > ristkülik.bottom - 5:
            posY = ristkülik.bottom
    
    if pygame.Rect(posX, posY, 30, 30).colliderect(pygame.Rect(0, 110, 10, screenY - 110)):
        if posX < 5:
            posX = 0
        else:
            posX = 35

    if pygame.Rect(posX, posY, 30, 30).colliderect(pygame.Rect(screenX - 10, 110, 10, screenY - 110)):
        if posX > screenX - 35:
            posX = screenX - 30
        else:
            posX = screenX - 65
    
    ruut = pygame.draw.rect(screen, red, [posX, posY, 30, 30])
    pygame.display.flip()
    screen.fill(lBlue)

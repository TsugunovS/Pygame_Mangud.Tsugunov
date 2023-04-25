import pygame, random
pygame. init()
red = [255, 0, 0]
green = [0, 255, 0]
blue = [6, 6, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]

screenX = 640
screenY = 480
screen=pygame.display. set_mode([screenX, screenY])
pygame.display.set_caption("mmm")
screen.fill(lBlue)
clock=pygame.time.Clock()
posX,posY=0,0
speedX,speedY=3,4
#player
player = pygame.Rect(posX, posY, 120, 120)
playerImage = pygame.image.load("123.png")
playerImage = pygame.transform.scale(playerImage, [player.width, player.height])




pygame.display.flip()
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        break
pygame.quit()

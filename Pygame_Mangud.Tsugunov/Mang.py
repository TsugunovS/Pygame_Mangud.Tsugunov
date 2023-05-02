import pygame
import random

pygame.init()

r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)

red = [r,g,b]
lBlue = [153, 204, 255]
black = [0, 0, 0]

screenX= 640
screenY = 480
screen=pygame.display.set_mode([screenX,screenY])
pygame.display.set_caption("Klaviatuuriga juhtimine")
screen.fill(lBlue)
clock = pygame.time.Clock()

posX,posY=screenX/2, screenY/2
speedX,speedY = 0,0
directionX, directionY = random.choice([-1,1]), random.choice([-1,1])

#создание переменных для полосок
stripe1_x = 0
stripe2_x = screenX - 100
stripe_speed = 3
stripe_direction = 1 

gameover = False
while not gameover:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
        elif event.type == pygame.KEYDOWN: #klahviajutuse vabastamine
            if event.key == pygame.K_RIGHT:
                stripe_direction = 1
            elif event.key == pygame.K_LEFT:
                stripe_direction = -1

    posX += speedX * directionX
    posY += speedY * directionY

    #проверка столкновения с границами
    if posX <= 0:
        posX = 0
        directionX = random.choice([1, 1])
    elif posX + 30 >= screenX:
        posX = screenX - 30
        directionX = random.choice([-1, -1])
    if posY <= 0:
        posY = 0
        directionY = random.choice([1, 1])
    elif posY + 30 >= screenY:
        posY = screenY - 30
        directionY = random.choice([-1, -1])

    #обновление координат полосок
    stripe1_x += stripe_speed * stripe_direction
    stripe2_x -= stripe_speed * stripe_direction
    if stripe1_x < 0 or stripe1_x > screenX - 100:
        stripe_direction *= -1

    if random.randint(0, 639) == 0:
        speedX, speedY = random.randint(1,1), random.randint(1,1)
        directionX, directionY = random.choice([1,1]), random.choice([1,1])

    #отрисовка полосок и квадрата
    pygame.draw.rect(screen, black, [stripe1_x, 10, 150, 20])
    pygame.draw.rect(screen, black, [stripe2_x, 450, 150, 20])
    ruut = pygame.draw.rect(screen, red, [posX, posY, 30, 30])

    pygame.display.flip()
    screen.fill(lBlue)

pygame.quit()



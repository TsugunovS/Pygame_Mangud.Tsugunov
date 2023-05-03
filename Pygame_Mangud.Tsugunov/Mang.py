import pygame
import random

pygame.init()

#настройки экрана
screenX = 640
screenY = 480
screen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption("Pingpong")

pilt = pygame.image.load("123.png")


#цвета
lBlue = (173, 216, 230)
black = (0, 0, 0)
red = (255, 0, 0)

#квадрат
posX = screenX / 2
posY = screenY / 2
speedX = 1
speedY = 1
directionX = random.choice([1, -1])
directionY = random.choice([1, -1])

#полосоки
polosa1 = screenX / 2 - 75
polosa2 = screenX / 2 - 75
polosa_speed = 5
polosa_direction = 0

clock = pygame.time.Clock()

#выбор уровня сложности
while True:
    valik = input("Valige raskusaste (1 - Lihtne/ 2 - Keskmine/ 3 - Raske/ 4 - Väga raske/ 5 - ???): ")
    if valik in ["1", "2", "3", "4", "5"]:
        break
    else:
        print("Valige loendist tase!")

score=0

#запуск игры
gameover = False
while not gameover:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
        elif event.type == pygame.KEYDOWN: #klahviajutuse vabastamine
            if event.key == pygame.K_RIGHT:
                polosa_direction = 1
            elif event.key == pygame.K_LEFT:
                polosa_direction = -1

    #различные уровни сложности
    if valik == "1":
        speedX, speedY = 1,1
    elif valik == "2":
        speedX, speedY = 2,2
    elif valik == "3":
        speedX, speedY = 3,3
    elif valik == "4":
        speedX, speedY = 5,5
    elif valik == "5":
        speedX, speedY = 8,8
    else:
        print("Valige loendist tase!")

    posX += speedX * directionX
    posY += speedY * directionY

    #отталкивание от бортиков
    if posX <= 0:
        posX = 0
        directionX = random.choice([1, 1])
   
    elif posX + 30 >= screenX:
        posX = screenX - 30
        directionX = random.choice([-1, -1])
       
    if posY <= 0:
        posY = 0
        directionY = random.choice([1, 1])
        score -=1
    elif posY + 30 >= screenY:
        posY = screenY - 30
        directionY = random.choice([-1, -1])
        score -=1

    #квадрат отталкивается от полосок
    if posY <= 30 and (posX + 30 >= polosa1 and posX <= polosa1 + 150):
        directionY = 1
        score +=1
    elif posY + 30 >= screenY - 30 and (posX + 30 >= polosa2 and posX <= polosa2 + 150):
        directionY = -1
        score +1

    #координаты полосок
    polosa1 += polosa_speed * polosa_direction
    polosa2 -= polosa_speed * polosa_direction
    if polosa1 < 0 or polosa1 > screenX - 150:
        polosa_direction *= -1

    if random.randint(0, 639) == 0:
        directionX, directionY = random.choice([1, -1]), random.choice([1, -1])


    #полоски и квадрат
    pygame.draw.rect(screen, black, [polosa1, 10, 150, 20])
    pygame.draw.rect(screen, black, [polosa2, 450, 150, 20])
    pilt = pygame.draw.rect(screen, red, [posX, posY, 30, 30])

    font = pygame.font.SysFont(None, 25)
    text = font.render("Счет: " + str(score), True, black)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    screen.fill(lBlue)
    распиши
pygame.quit()



import pygame
import random

#Инициализация библиотек
pygame.init()

#Задание размеров окна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
#И создание этого окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#Название заголовка окна
pygame.display.set_caption('Тир')
#Определение локальных изображений для главного окна и мишени
icon = pygame.image.load('img/duckhunt.jpg')
target_img = pygame.image.load('img/duck.png')
#Определение размеров и координат мишени
target_width = 50
target_height = 50
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
#Задание цвета фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

#Игровой цикл
running = True
while running:
    #Заполнение фона
    screen.fill(color)
    #Дальше идёт обработка событий
    for event in pygame.event.get():
        #Условие выхода из игры - закрытие окна
        if event.type == pygame.QUIT: running = False
        #Обработка нажатий кнопок мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Считывание координат мыши и сравнение с положением мишени
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
    screen.blit(target_img, (target_x, target_y))
    #Обновление экрана
    pygame.display.update()


#Завершение игры
pygame.quit()
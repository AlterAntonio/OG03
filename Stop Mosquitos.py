import pygame, random #Импорт библиотек
pygame.init() #Инициализация модулей PyGame

#Создание игрового экрана
background = pygame.image.load('img\\background.bmp') #Загрузка фоновой картинки
#Сопоставление сторон игрового экрана к фоновой картинке
SCREEN_WIDTH = background.get_width()
SCREEN_HEIGHT = background.get_height()
screen = pygame.display.set_mode((background.get_width(), background.get_height())) #Установка его размеров

#Создание счётчика count и шрифта
count = 0 #переменная-счётчик
font = pygame.font.Font(None, 36) #шрифт для сообщения про сбитых комаров

pygame.display.set_caption('No Mosquitos!') #Оглавление игрового окна
icon = pygame.image.load('img\\mosquito7.png') #Загрузка изображения для иконки
pygame.display.set_icon(icon) #И его установка

#Создание спрайтов, рандомный выбор, и указание их размеров
targets = [pygame.image.load(f'img\\mosquito{i}.png').convert_alpha() for i in range(1, 9)]
target = random.choice(targets)
target_width = 80
target_height = 80

#Теперь работа с курсором. Определение функции, изменяющей размер картинки курсора
def scale_sprite(image, scale):
    width = int(image.get_width() * scale) #Функция int() на тот случай, когда результат float
    height = int(image.get_height() * scale)
    return pygame.transform.scale(image, (width, height)) #Возврат изменённого изображения

cursor_img = pygame.image.load('img\\flyswatter.png').convert_alpha() #Загрузка изображения курсора по умолчанию
cursor_scaled = scale_sprite(cursor_img, 0.5) #Копируем обработанное функцией scale_sprite() изображение
pygame.mouse.set_visible(False) #Убираем видимость системного курсора в игровом окне
cursor = cursor_img #Определяем изображение курсора по умолчанию

#Определение начальных координат цели
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

#Определяем функцию движения комаров
def move(target_x, target_y, speed_x, speed_y, target_width, target_height, SCREEN_WIDTH, SCREEN_HEIGHT):
    #Изменение координат
    target_x += speed_x
    target_y += speed_y

    #Переопределение направления движения комаров с учётом границ игрового экрана
    if target_x < 0 or target_x > SCREEN_WIDTH - target_width: speed_x = -speed_x
    if target_y < 0 or target_y > SCREEN_HEIGHT - target_height: speed_y = -speed_y

    return target_x, target_y, speed_x, speed_y #Возврат значений координат цели и её скорости

#Определение начальной скорости и направления комаров
speed_x = random.uniform(-2, 2)
speed_y = random.uniform(-2, 2)

running = True #Создание переменной с условием выполнения игрового цикла

while running: #Игровой цикл
    mouse_x, mouse_y = pygame.mouse.get_pos()  # Получение координат, на которых клацнул
    for event in pygame.event.get(): #Цикл обработки игровых событий
        if event.type == pygame.QUIT: #Условие завершения игры - закрыть окно
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN: #Обработка нажатий клавиш мыши
            cursor = cursor_scaled #Изменение размера изображения курсора
            #Сопоставление координат мыши с целью
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target = random.choice(targets) #Выбор следующего рисунка цели
                #Новые рандомные координаты цели
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                #Новые параметры скорости цели
                speed_x = random.uniform(-2, 2)
                speed_y = random.uniform(-2, 2)
                count += 1 #Обновление счётчика подбитых комаров
        #Действие по отжатию кнопки мыши - изображение курсора по умолчанию
        if event.type == pygame.MOUSEBUTTONUP:
            cursor = cursor_img

    #Переопределение переменных: позиция и скорость комаров
    target_x, target_y, speed_x, speed_y = move(target_x, target_y, speed_x, speed_y, target_width, target_height, SCREEN_WIDTH, SCREEN_HEIGHT)

    #Отрисовка фона
    screen.blit(background, (0, 0))
    #Отображение подбитых комаров
    screen.blit(font.render(f'Mosquitos down: {count}', True, (255, 255, 255)), (50, 50))  #
    #Отображение цели на экране согласно направлению движения
    if speed_x > 0:
        target_flipped = pygame.transform.flip(target, True, False)
        screen.blit(target_flipped, (target_x, target_y))
    else: screen.blit(target, (target_x, target_y))

    cursor_rect = cursor.get_rect(center=(mouse_x, mouse_y)) #Позиционирование изображения относительно курсора мыши
    screen.blit(cursor, cursor_rect.topleft) #И его отрисовка
    pygame.display.update() #Обновление игрового экрана с изменениями

pygame.quit() #Завершение работы модулей PyGame. Фух, было не просто!